from google.genai import types


def require_role(*allowed_roles: str):
    """Builds a guard that only lets users with one of these roles into an agent."""

    def guard(callback_context):
        role = callback_context.state.get("role")
        if role in allowed_roles:
            return None  # allowed: let the agent run
        return types.Content(
            role="model",
            parts=[types.Part(text="Access denied: your role cannot use this agent.")],
        )

    return guard
