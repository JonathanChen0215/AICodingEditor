AICodingEditor V0.2.99-01a Alpha 1 package note
======================================================
Based on V0.2.37-33. Existing examples are retained for GitHub end-user testing.

AICodingEditor V0.1.32 bundled examples
========================================

1. Streamlit_SinCos_App.py
   Open this Python file and click Streamlit. AICodingEditor checks / installs
   streamlit and pandas in the active Python environment when necessary.

2. Live_Variable_Monitor/SinCos_LiveVariableMonitor.py
   Enable VARIABLES / CHARTS -> Enable Live Monitor, select time_s, x, y1 and y2,
   then Run Current. It emits one AICE_VAR sample every 0.2 seconds.

3. C/Hello_input_test.c
   Interactive C stdin example. The prompt calls fflush(stdout) so it appears
   before input is entered in Embedded Console.

4. Cpp/First_meet_greeting.cpp
   Interactive C++ name input example.

5. Java/HelloInputTest.java
   Interactive Java stdin example.


6. Python/sinx_cosinx_streamlit_2.py
   Streamlit real-time sin/cosin waveform demo. Open the file and click Streamlit
   to see a moving 360-point waveform window.

The application also stores a fallback copy of these files inside its JAR.
Use ? -> Open Example Files Folder... to open the external folder, or the
extracted built-in folder when the external folder has been moved.

V0.1.33 additions
-----------------
Python/AutoInstall_Humanize_Demo.py demonstrates confirmed automatic PyPI package installation after ModuleNotFoundError.
Python/StandardLibrary_Import_Reminder_Demo.py demonstrates the standard-library import reminder; it intentionally needs import json.
Streamlit_Infinite_SinCos_Monitor.py demonstrates a continuous 0-359 degree loop until Stop / Ctrl+C / Esc in the Streamlit page.

V0.2.37-33 addition
--------------------
Python/sinx_cosinx_streamlit_2.py is now permanently kept in the Python sample folder and documented in all three user manuals.
