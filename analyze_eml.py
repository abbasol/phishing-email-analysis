import re
import sys
import hashlib
from email import policy
from email.parser import BytesParser


def defang(u):
    return u.replace("http", "hxxp").replace(".", "[.]")


for path in sys.argv[1:]:
    with open(path, "rb") as f:
        m = BytesParser(policy=policy.default).parse(f)
    print("=" * 60)
    print("File:", path)
    for h in ("From", "Reply-To", "Return-Path", "To", "Subject", "Date"):
        print(f"{h}: {m[h]}")
    print("Authentication-Results:", m["Authentication-Results"])
    print("Received-SPF:", m["Received-SPF"])
    print("Received hops:", len(m.get_all("Received", [])))
    body = m.get_body(preferencelist=("html", "plain"))
    text = body.get_content() if body else ""
    urls = sorted(set(re.findall(r'https?://[^\s"\'<>)]+', text)))
    print("URLs (defanged):")
    for u in urls:
        print("  ", defang(u))
    print("Attachments (sha256):")
    for part in m.iter_attachments():
        data = part.get_payload(decode=True) or b""
        print("  ", part.get_filename(), hashlib.sha256(data).hexdigest())
