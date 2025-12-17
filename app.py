AWS_SECRET_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"


from flask import Flask, request, jsonify, render_template_string
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>🔐 SafeCode — Security Analyzer</title>
        <style>
            body { background-color: #000; color: #0ff; font-family: 'Consolas', monospace; text-align: center; padding: 40px; }
            h1 { color: #0ff; font-size: 2em; }
            p { color: #aaa; }
            textarea {
                width: 80%; height: 200px; background: #111; color: #0ff;
                border: 1px solid #0ff; border-radius: 10px; padding: 10px; font-size: 14px;
            }
            button {
                background: #0ff; color: #000; font-weight: bold; border: none;
                padding: 10px 20px; border-radius: 8px; margin: 10px; cursor: pointer;
            }
            button:hover { background: #00cccc; }
            pre {
                background: #111; color: #0ff; border: 1px solid #0ff;
                border-radius: 10px; padding: 20px; width: 80%; margin: auto;
                white-space: pre-wrap; text-align: left;
            }
        </style>
    </head>
    <body>
        <h1>🔐 SafeCode — Security Analyzer</h1>
        <p>Paste your Python or JavaScript code below and click Analyze.</p>
        <textarea id="code" placeholder="Paste your code here..."></textarea><br>
        <button onclick="analyze()">Analyze</button>
        <button onclick="clearAll()">Clear</button>
        <pre id="output"></pre>

        <script>
            async function analyze() {
                const code = document.getElementById("code").value;
                document.getElementById("output").textContent = "⏳ Scanning for vulnerabilities...";
                const response = await fetch("/analyze", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ code })
                });
                const result = await response.json();
                document.getElementById("output").textContent = result.output;
            }

            function clearAll() {
                document.getElementById("code").value = "";
                document.getElementById("output").textContent = "";
            }
        </script>
    </body>
    </html>
    """)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    code = data.get("code", "")
    issues = []


    patterns = [
        (r'password\s*=\s*["\']', 
         "🚨 Hardcoded credentials detected.", 
         "Storing passwords in code is unsafe. Use environment variables or a secure vault."),
        (r'eval\s*\(', 
         "⚠️ Use of eval() — may lead to code injection.", 
         "Avoid eval(). Use safe parsing or explicit functions."),
        (r'exec\s*\(', 
         "⚠️ Use of exec() — dangerous for untrusted input.", 
         "Avoid exec(); validate and sanitize all inputs."),
        (r'os\.system\s*\(', 
         "⚠️ os.system() — command injection risk.", 
         "Use subprocess.run([...], shell=False) instead."),
        (r'subprocess', 
         "⚠️ subprocess — risky if shell=True or unvalidated input.", 
         "Validate inputs; prefer subprocess.run([...], shell=False)."),
        (r'document\.write\s*\(', 
         "⚠️ document.write() — can cause XSS.", 
         "Use DOM manipulation (innerText / textContent) safely."),
        (r'input\s*\(', 
         "⚠️ Unvalidated input detected.", 
         "Add input validation or try/except for safer handling.")
    ]

    for pattern, issue, fix in patterns:
        if re.search(pattern, code, re.I):
            issues.append(f"{issue}\n💡 Fix Suggestion: {fix}\n")

    score = max(0, 100 - len(issues) * 10)
    
    if not issues:
        output = f"✅ No major vulnerabilities detected.\n\nSecurity Score: {score}%"
    else:
        output = f"Security Score: {score}%\n\n" + "\n".join(issues)

    return jsonify({"output": output})

if __name__ == "__main__":
    app.run(debug=True)
