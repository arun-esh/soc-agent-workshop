# SOC Agent Workshop

Build a small security operations team with [Google ADK](https://google.github.io/adk-docs/), one branch at a time. Each branch adds one idea to the same agent. All data is fake.

## Run the agent

```bash
source .venv/bin/activate   # after completing Setup below
adk web
```

Open the address it prints and select `main_agent`.

> The `main_agent` agent is introduced on branch `01-root-agent`.

## Prerequisites

- Python 3.12
- A free Gemini API key: https://aistudio.google.com/apikey

## Setup

```bash
# 1. Create a virtual environment and install ADK
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Add your API key (.env is git-ignored and never committed)
cp .env.example .env
# edit .env and replace your-key-here

# 3. Verify the installation
adk --version
```

## Branches

The branches form a single linear history. Each one is created from the previous branch and only adds to it.

| Branch              | Adds                                  |
| ------------------- | ------------------------------------- |
| `00-setup`        | Python, ADK, API key                  |
| `01-root-agent`   | A plain root agent                    |
| `02-tools`        | A tool to verify who the user is      |
| `03-instructions` | Strict, on-topic gatekeeper rules     |
| `04-sub-agents`   | Two colleagues: Analyst and Commander |
| `05-guard`        | A guard so roles cannot be faked      |
| `06-team`         | Specialists for the Commander         |
| `07-approval`     | Human approval for dangerous actions  |

## Troubleshooting

| Problem                              | Fix                                                             |
| ------------------------------------ | --------------------------------------------------------------- |
| `adk: command not found`           | Activate the virtual environment: `source .venv/bin/activate` |
| API key or authentication error      | Check `.env` is in the repo root and contains your real key   |
| Stale state after switching branches | `rm -rf main_agent/.adk`, then restart `adk web`            |
