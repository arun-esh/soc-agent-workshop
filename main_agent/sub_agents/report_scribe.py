from google.adk.agents.llm_agent import Agent

from ..guards import require_role

report_scribe = Agent(
    model='gemini-flash-latest',
    name='report_scribe',
    description='Writes the final incident report from what the team has found.',
    instruction=(
        'You write the incident report. Use only facts already found in this conversation. '
        'Format: Summary (one sentence), Timeline, Indicators, Recommended next step. '
        'If a section has no facts yet, write "not in the data". Never invent anything.'
    ),
    before_agent_callback=require_role('lead'),
)
