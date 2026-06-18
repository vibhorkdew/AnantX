from fastapi import APIRouter
import subprocess
import re

router = APIRouter(
    prefix="/api/falco",
    tags=["Falco"]
)

FALCO_CONTAINER = "anantx-falco-1"


@router.get("")
def get_falco_alerts():

    try:
        result = subprocess.check_output(
            [
                "docker",
                "logs",
                FALCO_CONTAINER,
                "--tail",
                "50"
            ],
            stderr=subprocess.STDOUT,
            text=True
        )

        alerts = []

        for line in result.splitlines():

            if "container_name=" in line:

                container = "unknown"

                match = re.search(
                    r"container_name=([^\s]+)",
                    line
                )

                if match:
                    container = match.group(1)

                severity = "NOTICE"

                if "Critical" in line:
                    severity = "CRITICAL"

                alerts.append({
                    "severity": severity,
                    "container": container,
                    "rule": line[:120],
                    "time": "Live"
                })

        return {
            "alerts": alerts
        }

    except Exception as e:
        return {
            "alerts": [],
            "error": str(e)
        }