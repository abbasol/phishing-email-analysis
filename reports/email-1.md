Email #1 (sample-4035.eml)
Verdict: Phishing / prize scam (likely survey or affiliate lure)
Indicators:
  - Display name (Fressnapf) does not match From domain (stayfriends.de)
  - Return-Path domain (sportwitness.co.uk) differs from From domain
  - SPF, DKIM and DMARC all "none"
  - "You have been selected" prize lure in German
  - Links to unrelated domains: pcapps[.]store, CloudFront-hosted page, trk2[.]de tracker
MITRE: T1566.002 (Phishing: Spearphishing Link)
Action: block sender and domains, delete message, report to security team
