from fastapi import APIRouter
import requests
from datetime import datetime

router = APIRouter()

@router.get("/api/metrics")
def get_metrics():

    try:

        query = "process_resident_memory_bytes"

        response = requests.get(
            "http://prometheus:9090/api/v1/query",
            params={"query": query}
        )

        result = response.json()

        chart_data = []

        for item in result["data"]["result"]:

            value = float(item["value"][1])

            chart_data.append({
                "time": datetime.now().strftime("%H:%M"),
                "memory": round(value / 1024 / 1024, 2)
            })

        return chart_data

    except Exception as e:

        return {
            "error": str(e)
        }
