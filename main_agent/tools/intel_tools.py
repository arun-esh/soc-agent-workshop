import json
from pathlib import Path

DATA = Path(__file__).parent.parent / "data"


def lookup_ip(ip: str) -> dict:
    """Looks up the reputation of one IP address.

    Args:
        ip: The IP address, for example "198.51.100.23".
    """
    reputation = json.loads((DATA / "ip_reputation.json").read_text())
    entry = reputation.get(ip.strip())
    if entry is None:
        return {"status": "not_found", "reason": f"No reputation data for {ip}."}
    return {"ip": ip.strip(), **entry}
