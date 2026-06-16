from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    tags=["falco"]
)

@router.get("/falco-alerts")
def get_falco_alerts():

    return {
        "alerts": [
            {
                "severity": "HIGH",
                "source": "Falco",
                "description": "Terminal shell detected inside container"
            },
            {
                "severity": "MEDIUM",
                "source": "Falco",
                "description": "Unexpected process execution"
            }
        ]
    }