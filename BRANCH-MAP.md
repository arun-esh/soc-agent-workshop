# Branch map: building the SOC team step by step

Status: `00-setup` is built. Branches 01 to 06 are still plans.
Talk: 30 minutes, for cyber security students who have not built an agent team.
Approach: new repo, new code from scratch in `soc_agents/`. One branch per step. Each branch adds one thing to the same agent.

## Branches

| # | Branch | What we add | ADK code (the only new idea) | Files added | What students see |
|---|---|---|---|---|---|
| 0 | `00-setup` | Python 3.12, ADK, requirements, `.env.example` | – | `requirements.txt`, `.python-version`, `.env.example`, `README.md` | `adk --version` prints 2.15.0 |
| 1 | `01-root-agent` | A root agent, the receptionist | `Agent(name, model, instruction)` | `agent.py` | It chats and welcomes you, but can't check anything. |
| 2 | `02-tools` | A tool to check who you are | `tools=[verify_user]` | `tools/gatekeeper_tools.py`, `data/users.json` | Sign in works. Wrong password and switched-off account are refused. |
| 3 | `03-sub-agents` | Two colleagues: Analyst and Commander | `sub_agents=[analyst, commander]` | `analyst_agent.py`, `commander_agent.py`, `tools/analyst_tools.py`, `data/alerts.json`, `data/logs.json` | Sam goes to the Analyst and reads alerts. Riya goes to the Commander. |
| 4 | `04-guard` | A guard so roles can't be faked | `before_agent_callback=require_role(...)` | `guards.py` | Sam says "I'm a lead" and the code refuses. |
| 5 | `05-team` | The Commander gets specialists | `sub_agents=[log_investigator, threat_intel, report_scribe]` | `log_investigator.py`, `threat_intel_agent.py`, `report_scribe.py`, `data/ip_reputation.json` | An alert goes in and a report comes out. |
| 6 | `06-approval` | A dangerous action needs a human | Confirmation on `isolate_host` | `tools/response_tools.py` | The agent proposes isolating a host, stops, and you approve or reject. |

Each branch builds on the one before it. `git diff 03-sub-agents 04-guard` shows only that step's new lines.

## The story, one line per branch

1. Meet the receptionist.
2. Now it can check who you are.
3. Different people get different colleagues.
4. Someone lies, and the code says no.
5. The Commander builds a team.
6. Some actions need a person.

## Limits

- Branches 1, 2, 5 and 6 are about 1 to 3 lines of new ADK each. Branches 3 and 4 are about 10.
- Instructions stay 1 to 3 lines on screen. Tools can be as long as they need to be.
- Mock data only. No live APIs. No A2A.
- The trace plugin is left out of the 6 branches. Optional bonus at the end if there is time.

## How we build it

One branch at a time. After each branch, show the diff and stop. The presenter reviews it ("good" or "change this") before the next branch starts. Next branch: `01-root-agent`.

## Live switching routine

```bash
git diff <previous> <next> -- soc_agents   # show only the new lines
rm -rf soc_agents/.adk                     # clear old session state
git switch <next>
adk web                                    # restart at each branch
```
