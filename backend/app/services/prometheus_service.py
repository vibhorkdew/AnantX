import requests

PROMETHEUS_URL = "http://prometheus:9090"


def query_prometheus(query: str):

    response = requests.get(
        f"{PROMETHEUS_URL}/api/v1/query",
        params={"query": query}
    )

    return response.json()
