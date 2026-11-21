from google.adk.agents.llm_agent import Agent

from ..guards import require_role
from ..tools.intel_tools import lookup_ip

threat_intel = Agent(
    model='gemini-flash-latest',
    name='threat_intel',
    description='Checks whether an IP address is known to be bad.',
    instruction=(
        'You check IP addresses. Call lookup_ip for each one and give the verdict, score and notes. '
        'If lookup_ip finds nothing, say "not in the data". Never guess a reputation.'
    ),
    before_agent_callback=require_role('lead'),
    tools=[lookup_ip],
)
