Email #4 (sample-9247.eml)
Verdict: Phishing / scam lure with brand impersonation (high confidence)
Indicators:
  - Display name impersonates Zilveren Kruis (Dutch health insurer)
  - From domain written with Unicode lookalike characters and a non-valid TLD (.zn)
  - SPF pass applies to Return-Path domain (kyrkligfornyelse.org), unrelated to From; DKIM none, DMARC none (no alignment)
  - HELO hostname (moatads.com) unrelated to sender
  - Brand mismatch: health insurer offering a Verkade chocolate bar
  - Seven per-recipient tracking links to emailservicesnetau[.]com
  - Link structure resembles Email #2 (possible shared campaign tooling, unconfirmed)
MITRE: T1566.002 (Phishing: Spearphishing Link)
Action: block emailservicesnetau[.]com and kyrkligfornyelse.org, delete message, notify the impersonated brand
Limitations: landing pages not visited
VirusTotal (kyrkligfornyelse[.]org): 0/92, no detections at time of check, checked 2026-11-06
VirusTotal (emailservicesnetau[.]com): 11/92 flagged, checked 2026-11-06
