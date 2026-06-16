from fastapi import APIRouter
import requests

router = APIRouter(
    prefix="/api",
    tags=["metrics"]
)

@router.get("/metrics")
def get_metrics():

    try:

        response = requests.get(
            "http://prometheus:9090/api/v1/query?query=up"
        )

        data = response.json()

        return {
            "status": "healthy",
            "prometheus": data
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }
