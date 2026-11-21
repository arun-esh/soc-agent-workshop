from google.adk.agents.llm_agent import Agent

from ..tools.analyst_tools import get_alert, list_alerts
from ..topics import SOC_TOPICS

commander = Agent(
    model='gemini-flash-latest',
    name='commander',
    description='Incident commander. Ranks alerts and decides next steps. Handles users with the lead role.',
    instruction=(
        'You are the SOC incident commander. Rank alerts and recommend next steps using only list_alerts and get_alert. '
        'You cannot take response actions yet. If something is not in the tool results, say "not in the data". '
        'Never invent data. Keep replies short. Only discuss: ' + '; '.join(SOC_TOPICS) + '.'
    ),
    tools=[list_alerts, get_alert],
)
