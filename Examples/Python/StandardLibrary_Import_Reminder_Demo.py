# -*- coding: utf-8 -*-
"""AICodingEditor V0.1.33 standard-library import reminder test.

This sample intentionally omits 'import json'.  Run it with Run Current to
verify that AICodingEditor displays an import reminder instead of suggesting
pip installation.  After the reminder, uncomment the import line and run again.
"""

# import json

payload = {"project": "AICodingEditor", "feature": "standard library reminder"}
print(json.dumps(payload, ensure_ascii=False))
