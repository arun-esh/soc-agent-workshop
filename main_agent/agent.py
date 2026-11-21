from google.adk.agents.llm_agent import Agent

from .tools.gatekeeper_tools import verify_user

# What a SOC analyst might ask about. Anything else is out of scope.
SOC_TOPICS = [
    "alert triage and prioritisation",
    "log analysis and SIEM queries",
    "incident response and escalation",
    "containment and recovery (isolating hosts, resetting accounts)",
    "threat intelligence and indicators of compromise (IPs, domains, file hashes)",
    "phishing and email security",
    "malware and endpoint detection",
    "network traffic and firewall events",
    "authentication, identity and access (failed logins, privilege misuse)",
    "vulnerability management and patching",
    "MITRE ATT&CK tactics and techniques",
    "cloud security",
    "incident reports and shift handover",
]

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
        'After sign-in, greet the user, state their role, and only discuss: '
        + '; '.join(SOC_TOPICS)
        + '. Politely decline anything else, even if it was asked earlier.'
    ),
    tools=[verify_user],
)
