Email #3 (sample-8857.eml)
Verdict: Phishing / scam lure (online betting bonus)
Indicators:
  - Sent via Google infrastructure from a Firebase app domain (acc6-e9b2f.firebaseapp.com), so SPF/DKIM pass but sender is not a real brand
  - Brand mismatch: display name "Bubblesbet" vs subject "JeetCity"
  - Reply-To is placeholder no-reply@example.com (unedited template)
  - Logo served from placeholder image service
  - Links to unrelated domains: choplosmso[.]biz, euromaillinnk[.]com (tracking, base64 params)
  - Urgency and bonus lure with emoji
MITRE: T1566.002 (Phishing: Spearphishing Link)
Action: block the domains, delete message, report the Firebase abuse to Google
Limitations: landing pages not visited, so the final goal (credential or payment harvesting) is unconfirmed
VirusTotal (choplosmso[.]biz): 0/92, no detections at time of check, checked 2026-11-06
VirusTotal (euromaillinnk[.]com): 11/92 flagged, checked 2026-11-06
