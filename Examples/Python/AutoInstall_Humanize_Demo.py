# -*- coding: utf-8 -*-
"""AICodingEditor V0.1.33 missing site-package auto-install test.

Run this file with Run Current.
If the third-party package 'humanize' is not installed, AICodingEditor detects
ModuleNotFoundError, asks for permission, runs uv pip install humanize (or
python -m pip install humanize), and runs this file again after installation.
"""

import humanize

number = 1_234_567
print("humanize package is ready.")
print("Formatted number:", humanize.intcomma(number))
