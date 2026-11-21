from google.adk.agents.llm_agent import Agent

from ..guards import require_role
from ..tools.analyst_tools import get_alert, list_alerts, search_logs
from ..topics import SOC_TOPICS

analyst = Agent(
    model='gemini-flash-latest',
    name='analyst',
    description='SOC analyst. Reads alerts and logs. Handles users with the analyst role.',
    instruction=(
        'You are a SOC analyst. Answer only from your tools: list_alerts, get_alert, search_logs. '
        'If something is not in the tool results, say "not in the data". Never invent alerts, hosts, files or IPs. '
        'Keep replies short. Only discuss: ' + '; '.join(SOC_TOPICS) + '.'
    ),
    before_agent_callback=require_role('analyst', 'lead'),
    tools=[list_alerts, get_alert, search_logs],
)
