"""Checks that your machine is ready for the workshop.

    python check_setup.py          checks Python, ADK and your API key
    python check_setup.py --live   also sends one tiny request to Gemini
"""
import os
import sys
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

MODEL = os.environ.get("SOC_MODEL", "gemini-flash-latest")
ENV_FILE = Path(__file__).parent / "soc_agents" / ".env"


def load_env():
    """Reads soc_agents/.env if it exists. ADK reads the same file when it runs."""
    from dotenv import load_dotenv

    load_dotenv(ENV_FILE)


def check(label, ok, hint=""):
    print(f"[{'ok' if ok else 'FAIL'}] {label}")
    if not ok and hint:
        print(f"       {hint}")
    return ok


def main():
    results = []

    results.append(check(
        f"Python {sys.version_info.major}.{sys.version_info.minor}",
        sys.version_info[:2] == (3, 12),
        "Use Python 3.12: uv venv --python 3.12 .venv",
    ))

    try:
        results.append(check(f"google-adk {version('google-adk')}", True))
    except PackageNotFoundError:
        results.append(check("google-adk installed", False, "pip install -r requirements.txt"))
        sys.exit(1)

    load_env()
    key = os.environ.get("GOOGLE_API_KEY", "")
    has_key = bool(key) and key != "your-key-here"
    results.append(check(
        "GOOGLE_API_KEY is set",
        has_key,
        "Copy .env.example to soc_agents/.env and add your key.",
    ))

    if "--live" in sys.argv and has_key:
        from google import genai

        try:
            reply = genai.Client().models.generate_content(
                model=MODEL, contents="Reply with the single word: ready"
            )
            results.append(check(f"{MODEL} answered: {reply.text.strip()}", True))
        except Exception as error:  # a demo script: show any failure plainly
            results.append(check(f"{MODEL} request", False, str(error)))

    print()
    print("All good." if all(results) else "Fix the lines marked FAIL, then run this again.")
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
