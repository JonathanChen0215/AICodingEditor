# Known Issues — V0.2.99-01a Alpha 1

1. **Unsigned Windows executable**  
   `AICodingEditor.exe` may trigger Microsoft Defender SmartScreen until a trusted code-signing certificate is applied.

2. **Java runtime required**  
   The EXE is a launcher for `AICodingEditor.jar`; Java 17+ must be installed and available through `JAVA_HOME` or `PATH`.

3. **AI services require separate accounts and quota**  
   OpenAI or Gemini requests can fail because of an invalid key, insufficient quota, rate limits, network restrictions, or a model name that is unavailable to the account.

4. **Python packages are environment-specific**  
   Streamlit, TensorFlow, Keras, pandas and other packages must be installed in the currently selected Python or uv virtual environment.

5. **Toolchain paths are Windows-oriented by default**  
   Java, MinGW, Arduino CLI and SQL Driver paths may need to be changed under Settings → Preference.

6. **Alpha stability**  
   This build has compile and GUI startup smoke testing, but full regression testing on all Windows versions, DPI settings, toolchains, databases and AI models is still required.
