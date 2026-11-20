# SOC agent workshop

Build a small security operations team with Google ADK, one branch at a time.
Every branch adds one idea to the same agent. All data is fake.

## Setup (this branch: `00-setup`)

You need Python 3.12 and a free Gemini API key from https://aistudio.google.com/apikey

```bash
# 1. Make a virtual environment and install ADK
uv venv --python 3.12 .venv          # or: python3.12 -m venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt   # or: pip install -r requirements.txt

# 2. Add your key (the real .env file is never committed)
mkdir soc_agents
cp .env.example soc_agents/.env
# open soc_agents/.env and replace your-key-here

# 3. Check ADK is installed
adk --version
```

## The branches

| Branch | What it adds |
|---|---|
| `00-setup` | Python, ADK, your key (you are here) |
| `01-root-agent` | A root agent, the receptionist |
| `02-tools` | A tool to check who you are |
| `03-sub-agents` | Two colleagues: Analyst and Commander |
| `04-guard` | A guard so roles can't be faked |
| `05-team` | The Commander gets specialists |
| `06-approval` | A dangerous action needs a human |

Move between them with `git switch <branch>`. To see only what a step added:

```bash
git diff 02-tools 03-sub-agents
```

## Run the agent (from branch 01 on)

```bash
adk web
```

Then open the address it prints and pick `soc_agents`.
