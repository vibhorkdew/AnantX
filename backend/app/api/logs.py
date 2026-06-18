from fastapi import APIRouter

router = APIRouter(
    prefix="/api/logs",
    tags=["Logs"]
)

@router.get("")
def get_logs():
    return {
        "logs": [
            {
                "timestamp": "2026-06-19 10:15:22",
                "service": "anantbuy-api",
                "severity": "INFO",
                "message": "User login successful"
            },
            {
                "timestamp": "2026-06-19 10:16:45",
                "service": "anantbuy-api",
                "severity": "WARNING",
                "message": "Invalid login attempt"
            },
            {
                "timestamp": "2026-06-19 10:18:10",
                "service": "prometheus",
                "severity": "INFO",
                "message": "Metrics scraped successfully"
            }
        ]
    }