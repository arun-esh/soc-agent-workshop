from google.adk.agents.llm_agent import Agent

from ..guards import require_role
from ..tools.analyst_tools import search_logs

log_investigator = Agent(
    model='gemini-flash-latest',
    name='log_investigator',
    description='Reads the logs of one host and says what happened, in time order.',
    instruction=(
        'You investigate one host. Call search_logs, then list what happened in time order, one line each. '
        'Quote only what the logs say. If something is not in the logs, say "not in the data". '
        'Always include any IP address you see, so the next specialist can check it.'
    ),
    before_agent_callback=require_role('lead'),
    tools=[search_logs],
)
