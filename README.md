# SafeCode Project

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
