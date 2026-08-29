# 🎣 Heuristic Phishing Email Detector

An automated defensive tool developed in **Python** designed to audit and analyze email content for social engineering signatures. It parses plain text to compute a dynamic risk assessment score based on indicators of compromise (IoCs), high-pressure keywords, and typosquatted or unsafe URLs.

## 🔍 Analytical Detection Framework

The detection engine scans corporate and personal communication templates against two high-risk rulesets:

1. **Heuristic Keyword Analysis:** Evaluates email body copy for urgent, high-pressure, or coercive phrasing (e.g., *security alerts, immediate action, account suspension, verify credentials*) often used by threat actors to induce fear.
2. **Technical URL/Domain Inspection:** Inspects embedded links for deceptive patterns, capturing malicious string injections (such as spoofed verification routes) and tracking signatures linked to known typosquatting techniques.

---

## 🛠️ Architecture & Specifications

* **Language:** Python 3
* **Parsing Engine:** Native Regular Expressions (`re` module)
* **Target Framework:** Standalone script optimized for localized SOC triage or user awareness simulation.

### ⚙️ How to Run the Assessment

To test the automated parsing engine against simulated email inputs, execute the primary script from your console:

```bash
python3 phishing_detector.py
```

---
*Legal Disclaimer: This software is built strictly for educational research, threat hunting methodologies, and secure simulation testing. No operational phishing campaigns are supported or facilitated by this code.*
