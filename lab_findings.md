# Lab findings: OWASP review and acceptable-use policy
 
| Area | Finding | Action |
|---|---|---|
| sql_lookup.py | SQL injection (OWASP Injection): 1 OR 1=1 returned every user | Replaced with a parameterized query; attack input now returns [] |
| request_draft.txt | Fails No secrets or PII in prompts: session token and customer email | Redacted before using Copilot; rotate any token already shared |
| ticket_4471.md | Hidden prompt-injection comment | Flagged by Copilot in Ask mode, removed, and reported to the security team |
