import json
from pathlib import Path

DATA = Path(__file__).parent.parent / "data"


def list_alerts() -> dict:
    """Lists every open alert with its id, severity and title."""
    alerts = json.loads((DATA / "alerts.json").read_text())
    return {"alerts": [{"id": a["id"], "severity": a["severity"], "title": a["title"]} for a in alerts]}


def get_alert(alert_id: str) -> dict:
    """Returns the full details of one alert.

    Args:
        alert_id: The alert id, for example "A-201".
    """
    for alert in json.loads((DATA / "alerts.json").read_text()):
        if alert["id"].lower() == alert_id.strip().lower():
            return alert
    return {"status": "not_found", "reason": f"No alert with id {alert_id}."}


def search_logs(host: str) -> dict:
    """Returns the log lines recorded for one host.

    Args:
        host: The host name, for example "FIN-LT-07".
    """
    logs = [l for l in json.loads((DATA / "logs.json").read_text()) if l["host"].lower() == host.strip().lower()]
    if not logs:
        return {"status": "not_found", "reason": f"No logs for host {host}."}
    return {"host": host, "logs": logs}
