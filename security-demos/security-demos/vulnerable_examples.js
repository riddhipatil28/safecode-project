// vulnerable_examples.js
// This file intentionally contains insecure patterns for Snyk-style analysis.
// These issues are documented and will be fixed in a later phase.

// SNYK-ISSUE: Hardcoded secret
const API_KEY = "123456-FAKE-SECRET";

// SNYK-ISSUE: Use of eval()
function runCode(userInput) {
  eval(userInput); // Code injection risk
}

// SNYK-ISSUE: Command injection risk
const { exec } = require("child_process");
function cleanup(path) {
  exec("rm -rf " + path); // Dangerous
}

// SNYK-ISSUE: Insecure HTTP usage
const http = require("http");
http.get("http://example.com", (res) => {
  res.on("data", () => {});
});
