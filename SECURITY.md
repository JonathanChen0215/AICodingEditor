# Security Policy

## Reporting a security issue

Do not publish API keys, product serial numbers, credentials, private source code, code-signing keys, or exploitable security details in a public GitHub Issue. Use the project owner's private contact channel for security-sensitive reports.

## Repository safety rules

Never commit:

- `.env` files
- `OPENAI_API_KEY`, `GEMINI_API_KEY`, or `GOOGLE_API_KEY` values
- Java Preferences exports containing encrypted local secrets
- Code-signing certificates, private keys, or passwords
- Serial-number generators or private licensing keys
- Database passwords or production connection strings
- Private customer source code or logs

The application should read AI credentials from environment variables at request time. Public test files must use placeholders only.
