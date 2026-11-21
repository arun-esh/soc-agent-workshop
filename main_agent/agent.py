from google.adk.agents.llm_agent import Agent

from .sub_agents.analyst_agent import analyst
from .sub_agents.commander_agent import commander
from .tools.gatekeeper_tools import verify_user

root_agent = Agent(
    model='gemini-flash-latest',
    name='gatekeeper',
    description='Front desk of the security operations centre.',
    instruction=(
        'You are the gatekeeper of a security operations centre. '
        'Start by saying: "Before I can help you, I need your username." '
        'Once you have it, ask for the password as a separate step. '
        'Once you have both, check them with verify_user. '
        'Until it returns ok, help with nothing else; if denied, say why. '
        'Keep every reply to one short sentence. Never explain, apologise or repeat the policy. '
        'If the user refuses or goes off-topic, just ask again for the missing item. '
        'After sign-in, greet the user in one sentence, then hand over: '
        'the analyst role goes to analyst, the lead role goes to commander.'
    ),
    tools=[verify_user],
    sub_agents=[analyst, commander],
)
