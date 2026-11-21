from google.adk.agents.llm_agent import Agent
from google.adk.tools import FunctionTool

from ..guards import require_role
from ..tools.response_tools import isolate_host

report_scribe = Agent(
    model='gemini-flash-latest',
    name='report_scribe',
    description='Writes the final incident report from what the team has found.',
    instruction=(
        'You write the incident report. Use only facts already found in this conversation. '
        'Format: Summary (one sentence), Timeline, Indicators, Recommended next step. '
        'If a section has no facts yet, write "not in the data". Never invent anything. '
        'After the report, if the host was found to be compromised, call isolate_host for that host. '
        'The system asks a human to approve, so do not ask in text.'
    ),
    before_agent_callback=require_role('lead'),
    tools=[FunctionTool(isolate_host, require_confirmation=True)],
)
