from google.adk.agents.llm_agent import Agent
from google.adk.tools import FunctionTool

from ..guards import require_role
from ..tools.analyst_tools import get_alert, list_alerts
from ..tools.response_tools import isolate_host
from ..topics import SOC_TOPICS
from .log_investigator import log_investigator
from .report_scribe import report_scribe
from .threat_intel_agent import threat_intel

commander = Agent(
    model='gemini-flash-latest',
    name='commander',
    description='Incident commander. Ranks alerts and decides next steps. Handles users with the lead role.',
    instruction=(
        'You are the SOC incident commander. Rank alerts and recommend next steps using only list_alerts and get_alert. '
        'For an alert, hand over to log_investigator for the host timeline, then threat_intel to check any IP found, '
        'then report_scribe to write the report. '
        'To contain a compromised host, propose isolate_host and wait for the human to approve. If something is not in the tool results, say "not in the data". '
        'Never invent data. Keep replies short. Only discuss: ' + '; '.join(SOC_TOPICS) + '.'
    ),
    before_agent_callback=require_role('lead'),
    tools=[list_alerts, get_alert, FunctionTool(isolate_host, require_confirmation=True)],
    sub_agents=[log_investigator, threat_intel, report_scribe],
)
