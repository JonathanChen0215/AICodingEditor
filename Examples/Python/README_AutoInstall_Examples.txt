AICodingEditor V0.2.99-01a Alpha 1 package note
======================================================
Based on V0.2.37-33. Existing examples are retained for GitHub end-user testing.

AICodingEditor V0.1.33 Python auto-install examples
====================================================

1) AutoInstall_Humanize_Demo.py
   - Run this file with Run Current.
   - If humanize is not installed, AICodingEditor detects ModuleNotFoundError.
   - Choose OK to install the suggested PyPI package into the selected Python
     / uv environment. The editor automatically runs the file again when the
     install succeeds.

2) StandardLibrary_Import_Reminder_Demo.py
   - It intentionally does not import json.
   - The run reports a NameError for json.
   - AICodingEditor tells you that json is part of Python's standard library
     and recommends adding: import json
   - Do not use pip to install Python standard-library modules.

Notes
-----
- Automatic installation requires an Internet connection and a working pip.
- AICodingEditor asks for confirmation before installing a missing third-party
  package. It does not install anything silently after a Python run fails.
- Use Settings -> Preference -> General -> Python Interpreter to select the
  Python environment used for installation and execution.


3) sinx_cosinx_streamlit_2.py
   - Streamlit real-time sin/cosin waveform sample.
   - Open this file and click Streamlit, or run:
       python -m streamlit run Examples\Python\sinx_cosinx_streamlit_2.py
   - Requires streamlit, numpy and matplotlib in the active Python / uv environment.
   - The sample keeps an approximately 360-point moving x-window; the leftmost
     points disappear and new points are appended on the right.
   - Stop with the Streamlit Stop Simulation button, or from the console using
     ESC / Ctrl+C.
