# Phishing Email Analysis

Manual analysis of five real-world phishing and scam emails, with one report per email and a small Python helper that extracts key indicators from .eml files.

## Scope

- 5 emails taken from a public phishing training collection (phishing_pot)
- Static analysis only: headers, authentication results, URLs, attachments
- No link was opened and no attachment was executed
- Raw samples are not included in this repository

## Summary

| # | Verdict | Key indicators | Domains checked (VirusTotal, 2026-11-06) |
|---|---------|----------------|------------------------------------------|
| 1 | Phishing: prize scam (retail brand lure) | From domain differs from Return-Path domain; SPF, DKIM, DMARC all none | not checked |
| 2 | Suspicious spam / scam | Sent through a bulk-mail service with authentication passing; attachment with empty-content SHA-256 | internetcampus[.]org: 11/92 |
| 3 | Phishing / scam: betting bonus | Sent via a cloud-app domain; Reply-To on a placeholder domain; unrelated link domains | choplosmso[.]biz: 0/92; euromaillinnk[.]com: 11/92 |
| 4 | Phishing: health insurer impersonation | Unicode look-alike domain; SPF passes only for the Return-Path domain, not the visible sender | kyrkligfornyelse[.]org: 0/92; emailservicesnetau[.]com: 11/92 |
| 5 | Phishing / scam: auto-protection brand impersonation | Emoji TLD in From; SPF, DKIM, DMARC all none; unrelated HELO domain; Reply-To on a mailing platform; links wrapped by Microsoft Safe Links | stylenewharbor[.]shop: 0/92; lokquickorbit[.]site: 0/92 |

Detailed reports are in the reports/ folder. Each report contains: verdict, indicators, MITRE ATT&CK mapping, recommended action, limitations.

## Method

1. Extract headers, authentication results, URLs and attachment hashes with analyze_eml.py
2. Compare From, Reply-To and Return-Path; check SPF, DKIM and DMARC alignment
3. Defang every indicator (hxxp, [.]) before writing it down
4. Unwrap redirect wrappers such as Safe Links to find the real destination domain
5. Check domain reputation on VirusTotal
6. Write the verdict with a confidence level and explicit limitations

## Tool

Usage: python3 analyze_eml.py samples/FILE.eml

Prints From, Reply-To, Return-Path, Subject, Date, Authentication-Results, Received hops, defanged URLs, and attachment names with SHA-256.

## Lessons learned

- Passing SPF, DKIM or DMARC does not make an email legitimate. Attackers send through authenticated bulk-mail and cloud services.
- A visible sender name proves nothing. Compare it with Return-Path, Reply-To and the authenticated domain.
- Security gateways rewrite links (for example Safe Links). The wrapper is not the destination; decode the real URL.
- A 0/92 reputation result means "no detections at time of check", not "safe". New domains are often not flagged yet.
- Some findings are hypotheses (tracking-path meaning, sender IP ownership) and are marked as such in the reports.

## Safety notes

- Analysis was done inside an isolated Linux VM
- Emails were never opened in a mail client
- All indicators are defanged

## Disclaimer

For educational purposes only. The samples come from a public training set and are not redistributed here.
