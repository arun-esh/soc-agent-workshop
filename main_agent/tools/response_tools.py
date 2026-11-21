def isolate_host(host: str) -> dict:
    """Cuts one host off from the network (mock: nothing is really isolated).

    Args:
        host: The host name, for example "FIN-LT-07".
    """
    return {"status": "isolated", "host": host.strip()}
