# SafeCode Project 


## Web Interface

- Built a simple HTML/CSS-based UI for the SafeCode analyzer
- Allows users to paste Python or JavaScript code
- Displays detected insecure patterns and recommendations
- Purpose: Demonstrate how SafeCode checks can be surfaced to developers


## CodeQL Findings

- High severity issue detected
- Flask application is running in debug mode
- File: app.py
- Risk: Debug mode exposes internal stack traces and sensitive information
- Status: Will be fixed later
## Secret Scanning (Gitleaks)

- Gitleaks workflow successfully runs on every push
- No secrets were detected in the current codebase
- This indicates no exposed credentials matching default detection rules
- Status: Monitoring enabled
