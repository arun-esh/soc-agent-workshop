import json
from pathlib import Path

from google.adk.tools import ToolContext

USERS_FILE = Path(__file__).parent.parent / "data" / "users.json"


def verify_user(username: str, password: str, tool_context: ToolContext) -> dict:
    """Checks a username and password against the staff list.

    Args:
        username: The user's login name, for example "sam".
        password: The user's password.

    Returns:
        A dict with "status" ("ok" or "denied") and, when ok, the user's "role".
    """
    users = json.loads(USERS_FILE.read_text())
    user = users.get(username.strip().lower())
    if user is None or user["password"] != password:
        return {"status": "denied", "reason": "Wrong username or password."}
    if not user["active"]:
        return {"status": "denied", "reason": "This account is switched off."}
    tool_context.state["role"] = user["role"]  # remembered by the code, not by the chat
    return {"status": "ok", "role": user["role"]}
