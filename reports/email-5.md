Email #5 (sample-12300.eml)
Verdict: Phishing / scam lure with brand impersonation (high confidence it is deceptive; end goal unconfirmed)
Indicators:
  - Display name impersonates Endurance (auto protection); From domain is random string with emoji TLD (invalid)
  - SPF, DKIM, DMARC all none; HELO domain stylenewharbor[.]shop unrelated to the brand
  - Reply-To routes to getdrip.com while From is a different domain
  - Empty Return-Path, stray "#" in subject (template artifact)
  - Discount and seasonal urgency lure ("Save $300")
  - Links point to lokquickorbit[.]site (random .site domain), wrapped by Microsoft Safe Links (wrapper does not imply safety)
MITRE: T1566.002 (Phishing: Spearphishing Link)
Action: block lokquickorbit[.]site and stylenewharbor[.]shop, delete message, report
Limitations: landing page not visited; sender IP ownership not verified
VirusTotal (stylenewharbor[.]shop): 0/92, no detections at time of check, checked 2026-11-06
VirusTotal (lokquickorbit[.]site): 0/92, no detections at time of check, checked 2026-11-06
