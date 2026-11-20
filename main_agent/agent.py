from google.adk.agents.llm_agent import Agent

from .tools.gatekeeper_tools import verify_user

root_agent = Agent(
    model='gemini-flash-latest',
    name='gatekeeper',
    description='Front desk of the security operations centre.',
    instruction=(
        'You are the gatekeeper of a security operations centre. '
        'Ask for a username and password and check them with verify_user. '
        'If denied, say why. If ok, greet the user and state their role.'
    ),
    tools=[verify_user],
)
