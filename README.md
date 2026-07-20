# AICodingEditor V0.2.99-01a — Alpha 1

> **GitHub Pre-release / End-user Alpha test build**  
> Based on **AICodingEditor V0.2.37-33**. This is not a final stable release.

## Release identity

- Application version: `V0.2.99-01a`
- Recommended Git tag: `v0.2.99-alpha.1`
- GitHub Release type: **Pre-release**
- Build date: `2026-07-16`
- Publisher: `陳志強 / Jonathan Chen, PMI-PMP`

## Choose a default-language package

The Windows release is published as three functionally identical ZIP assets. They differ only in the language applied when that package is first detected:

| Package | First-launch default |
|---|---|
| `..._Windows_English_Default.zip` | English |
| `..._Windows_Traditional_Chinese_Default.zip` | 中文（繁體，台灣） |
| `..._Windows_Simplified_Chinese_Default.zip` | 简体中文 |

After launch, the user can change the interface under **Settings → Preference → General → Language**. The selected language is preserved on later launches. Switching to another default-language package applies that package's default once, after which the user may change it again.

The public source tree and normal build scripts use **English** as the fallback/default. See `LANGUAGE_VARIANTS.md`.

## Main features

- OpenAI + Gemini AI Assistant
- Chat / Explain Code / Fix Error / Generate Code / Review Code
- AI file, image, folder and uv-project attachments
- Preview / Diff / Apply Patch and confirmed AI-generated file creation
- Python, uv virtual environments, Streamlit and Jupyter
- Java, C, C++, C#, JavaScript, PHP, Rust, Arduino and SQL
- MS SQL, MySQL and PostgreSQL Driver setting tabs
- Multiple embedded consoles
- Live Variable Monitor, XLSX and PNG execution reports
- Code folding, smart indentation and trilingual manuals
- Permanent sample: `Examples/Python/sinx_cosinx_streamlit_2.py`

## Windows run instructions

1. Install Java 17 or newer; JDK 26.0.1 is recommended.
2. Keep `AICodingEditor.exe` and `AICodingEditor.jar` in the same folder.
3. Run `AICodingEditor.exe` or `Run_AICodingEditor_V0.2.99-01a.bat`.

You may also run:

```bat
java -jar AICodingEditor.jar
```

## AI API keys

No real API key is bundled. Recommended Windows environment variables:

```text
OPENAI_API_KEY
GEMINI_API_KEY
```

When the default Gemini variable name is used, `GOOGLE_API_KEY` can also be used as a fallback.

## Alpha test priorities

Test startup/close, language selection, dark high-contrast UI, OpenAI/Gemini settings, Generate Code, new-file creation, Diff/Apply Patch, Python uv, Streamlit, compile/run workflows, multiple consoles, Program stdin, Live Variable Monitor, reports, Workbench/File Browser, attachments, manuals and examples.

Use `ALPHA_TEST_FEEDBACK.md` for reports. Never post API keys, serial numbers, passwords or private source code in a public issue.

## Build from source

English-default JAR:

```bat
build_windows.bat
```

```bash
./build_linux_mac.sh
```

All three language-default JARs:

```bat
build_all_language_variants_windows.bat
```

```bash
./build_all_language_variants_linux_mac.sh
```

## Important notices

- The Windows EXE is currently unsigned and Microsoft Defender SmartScreen may display a warning.
- Do not commit `.env`, API keys, signing private keys, AES master keys or serial-generation tools.
- The repository does not yet declare a final open-source license. Review `ALPHA_EVALUATION_NOTICE.md` before making it public.
