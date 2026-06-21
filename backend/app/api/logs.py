from fastapi import APIRouter
import requests
import os
import json

router = APIRouter(
    prefix="/api/logs",
    tags=["Logs"]
)

SPLUNK_URL = os.getenv("SPLUNK_URL")
SPLUNK_USER = os.getenv("SPLUNK_USER")
SPLUNK_PASSWORD = os.getenv("SPLUNK_PASSWORD")


@router.get("/debug")
def debug():
    return {
        "SPLUNK_URL": SPLUNK_URL,
        "SPLUNK_USER": SPLUNK_USER,
        "SPLUNK_PASSWORD": SPLUNK_PASSWORD
    }


@router.get("/test")
def test():

    requests.packages.urllib3.disable_warnings()

    try:

        response = requests.post(
            f"{SPLUNK_URL}/services/search/jobs/export",
            auth=(SPLUNK_USER, SPLUNK_PASSWORD),
            verify=False,
            data={
                "search": "search index=main | head 5",
                "output_mode": "json"
            },
            timeout=30
        )

        return {
            "status_code": response.status_code,
            "response_text": response.text
        }

    except Exception as e:

        return {
            "error": str(e)
        }


@router.get("")
def get_logs():

    requests.packages.urllib3.disable_warnings()

    try:

        response = requests.post(
            f"{SPLUNK_URL}/services/search/jobs/export",
            auth=(SPLUNK_USER, SPLUNK_PASSWORD),
            verify=False,
            data={
                "search": "search index=main | head 50",
                "output_mode": "json"
            },
            timeout=30
        )

        logs = []

        for line in response.text.splitlines():

            if not line.strip():
                continue

            try:

                data = json.loads(line)

                if "result" not in data:
                    continue

                result = data["result"]

                raw_message = result.get("_raw", "")

                severity = "INFO"

                raw_lower = raw_message.lower()

                if "warn" in raw_lower:
                    severity = "WARNING"

                if (
                    "error" in raw_lower
                    or "critical" in raw_lower
                    or "falco" in raw_lower
                ):
                    severity = "CRITICAL"

                logs.append({
                    "timestamp": result.get("_time", "-"),
                    "service": result.get("source", "-"),
                    "severity": severity,
                    "message": raw_message[:1000]
                })

            except Exception as parse_error:

                logs.append({
                    "timestamp": "-",
                    "service": "parser",
                    "severity": "WARNING",
                    "message": str(parse_error)
                })

        return {
            "count": len(logs),
            "logs": logs
        }

    except Exception as e:

        return {
            "count": 0,
            "logs": [
                {
                    "timestamp": "-",
                    "service": "splunk",
                    "severity": "CRITICAL",
                    "message": str(e)
                }
            ]
        }