# Changelog

## V0.2.99-01a — 2026-07-16

### Language-default distribution update

- Added separate English, Traditional Chinese and Simplified Chinese default-language Windows packages.
- Added `AICodingEditor_Default_Language.properties` as the package-level default-language resource.
- Added stable language-distribution IDs so switching packages applies the selected package default once while later user changes remain persistent.
- Set English as the public-source fallback/default.
- Added scripts to build all three language JAR variants.

### Alpha release preparation

- Rebuilt from `AICodingEditor V0.2.37-33` as **Alpha 1** for end-user testing.
- Updated application version, About information, build date, manuals, launcher script, and release documentation.
- Added GitHub-ready README, release body, issue template, security guidance, test-feedback template, known issues, build scripts, and checksum workflow.
- Preserved existing AIC30 30-day and AIC1Y 365-day serial whitelist compatibility.
- Preserved the permanent Python sample `Examples/Python/sinx_cosinx_streamlit_2.py`.
- No real OpenAI or Gemini API key is included.

### Base functionality retained from V0.2.37-33

- OpenAI and Gemini AI Assistant with provider/model display.
- Safe generated-file, Preview/Diff, and Apply Patch workflows.
- Explicit AI file/image/folder/uv-project attachments.
- Python uv, Streamlit and Jupyter workflows.
- SQL Driver tabs for MS SQL, MySQL and PostgreSQL.
- Multiple embedded consoles, smart indentation and code folding.
- Opt-in Variable Monitor and bounded Workbench project context.
- Traditional Chinese, Simplified Chinese and English manuals.
