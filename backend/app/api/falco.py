from fastapi import APIRouter
import requests
import os
import urllib3

urllib3.disable_warnings()

router = APIRouter(
    prefix="/api/falco",
    tags=["Falco"]
)

SPLUNK_HOST = os.getenv("SPLUNK_HOST", "splunk")
SPLUNK_PORT = os.getenv("SPLUNK_PORT", "8089")
SPLUNK_USERNAME = os.getenv("SPLUNK_USERNAME", "admin")
SPLUNK_PASSWORD = os.getenv("SPLUNK_PASSWORD")


@router.get("")
def get_falco_alerts():

    search_query = '''
    search index=* "container_name="
    | head 20
    '''

    try:

        response = requests.post(
            f"https://{SPLUNK_HOST}:{SPLUNK_PORT}/services/search/jobs/export",
            auth=(SPLUNK_USERNAME, SPLUNK_PASSWORD),
            verify=False,
            data={
                "search": search_query,
                "output_mode": "json"
            }
        )

        return {
            "raw": response.text
        }

    except Exception as e:

        return {
            "error": str(e)
        }