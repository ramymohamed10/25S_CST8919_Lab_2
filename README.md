# CST8919 Lab 2: Building a Web App with Threat Detection using Azure Monitor and KQL


## Objective

In this lab, you will:
- Create a simple Demo Python Flask app
- Deploy a the app to Azure App Service
- Enable diagnostic logging with Azure Monitor
- Use Kusto Query Language (KQL) to analyze logs
- Create an alert rule to detect suspicious activity and send it to your email
---
## Scenario
As a cloud security engineer, you're tasked with securing a simple web application. The app logs login attempts. You must detect brute-force login behavior and configure an automatic alert when it occurs.

## Tasks

### Part 1: Deploy the Flask App to Azure
1. Develop a Python Flask app with a `/login` route that logs both successful and failed login attempts.
2. Deploy the app using **Azure Web App**.

### Part 2: Enable Monitoring
1. Create a **Log Analytics Workspace** in the same region.
2. In your Web App, go to **Monitoring > Diagnostic settings**:
   - Enable:
     - `AppServiceConsoleLogs`
     - `AppServiceHTTPLogs` (optional)
   - Send to the Log Analytics workspace.
3. Interact with the app to generate logs (e.g., failed `/login` attempts).


You must test your app using a .http file (compatible with VS Code + REST Client) and include that file in your GitHub repo as test-app.http.

### Part 3: Query Logs with KQL
1. Create a KQL query to find failed login attempts.
2. Test it

### Part 4: Create an Alert Rule
1. Go to Azure Monitor > Alerts > + Create > Alert Rule.
2. Scope: Select your Log Analytics Workspace.
3. Condition: Use the query you created in the last step.
4. Set:
    - Measure: Table rows
    - Threshold: Greater than 5
    - Aggregation granularity: 5 minutes
    - Frequency of evaluation: 1 minute
    - Add an Action Group to send an email notification.
    - Name the rule and set Severity (2 or 3).
    - Save the alert.

## Submission
### GitHub Repository
- Initialize a Git repository for your project.
- Make **frequent commits** with meaningful commit messages.
- Push your code to a **public GitHub repository**.
- Include  **YouTube demo link in the README.md**.

Include a `README.md` with:
  - Briefly describe what you learned during this lab, challenges you faced, and how you’d improve the detection logic in a real-world scenario.
  - Your KQL query with explanation

- **A link to a 5-minute YouTube video demo** showing:
  - App deployed
  - Log generation and inspection in Azure Monitor
  - KQL query usage
  - Alert configuration and triggering

You must test your app using a .http file (compatible with VS Code + REST Client) and include that file in your GitHub repo as test-app.http.


---

## Submission Instructions

Submit your **GitHub repository link** via Brightspace.

**Deadline**: Wednesday, 18 June 2025

---

