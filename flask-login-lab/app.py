from flask import Flask, request, jsonify
import logging
import datetime
import os

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('app.log')
    ]
)

logger = logging.getLogger(__name__)

# Simple in-memory user store (for demo purposes)
USERS = {
    'admin': 'password123',
    'user1': 'mypassword',
    'testuser': 'test123'
}

@app.route('/')
def home():
    return jsonify({
        'message': 'Cloud Security Lab - Login Monitor',
        'endpoints': {
            'login': '/login (POST)',
            'health': '/health (GET)'
        }
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'timestamp': datetime.datetime.utcnow().isoformat()})

@app.route('/login', methods=['POST'])
def login():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            logger.warning(f"LOGIN_ATTEMPT_FAILED: No data provided from IP {request.remote_addr}")
            return jsonify({'error': 'No data provided'}), 400
        
        username = data.get('username')
        password = data.get('password')
        client_ip = request.remote_addr
        user_agent = request.headers.get('User-Agent', 'Unknown')
        
        # Log the login attempt with detailed information
        log_data = {
            'timestamp': datetime.datetime.utcnow().isoformat(),
            'ip_address': client_ip,
            'username': username,
            'user_agent': user_agent,
            'endpoint': '/login'
        }
        
        if not username or not password:
            logger.warning(f"LOGIN_ATTEMPT_FAILED: Missing credentials - IP: {client_ip}, Username: {username}")
            return jsonify({'error': 'Username and password required'}), 400
        
        # Check credentials
        if username in USERS and USERS[username] == password:
            logger.info(f"LOGIN_SUCCESS: User '{username}' logged in successfully from IP {client_ip}")
            return jsonify({
                'message': 'Login successful',
                'username': username,
                'timestamp': log_data['timestamp']
            }), 200
        else:
            # This is the key log entry for brute force detection
            logger.warning(f"LOGIN_FAILED: Invalid credentials for user '{username}' from IP {client_ip} - User-Agent: {user_agent}")
            return jsonify({'error': 'Invalid credentials'}), 401
    
    except Exception as e:
        logger.error(f"LOGIN_ERROR: Exception during login attempt from IP {request.remote_addr}: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/admin')
def admin():
    # Protected route for testing
    return jsonify({'message': 'Admin area - authentication required'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)