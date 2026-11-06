Email #2 (sample-7761.eml)
Verdict: Suspicious, likely spam/scam lure (not confirmed phishing)
Indicators:
  - Unsolicited freebie lure ("Safety Kit For You"), odd display name
  - Authentication passes (SPF/DKIM/DMARC via SendGrid): sender is configured, not spoofed
  - Links point to an unrelated domain (internetcampus[.]org), tracking tokens per recipient
  - Image-only style content hosted on imgchest
  - Attachment AAA-CarKit.pdf: sha256 is the hash of an empty file, could not be analyzed
MITRE: T1566.002 (link); T1566.001 possible if the PDF carried a payload
Action: check domains in urlscan/VirusTotal, block internetcampus[.]org, treat as spam
Limitations: pages and attachment not analyzed

VirusTotal (internetcampus[.]org): 11/92 flagged, checked 2026-11-06
