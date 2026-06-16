from fastapi import APIRouter
from pydantic import BaseModel
import json

router = APIRouter(prefix="/api", tags=["ai"])

TRIVY_REPORT = "reports/trivy-report.json"

class AIQuery(BaseModel):
    question: str

@router.post("/ai/query")
def ask_ai(query: AIQuery):

    question = query.question.lower()

    try:

        with open(TRIVY_REPORT, "r") as f:
            data = json.load(f)

        critical = 0
        high = 0
        medium = 0
        low = 0

        for result in data.get("Results", []):

            for vuln in result.get("Vulnerabilities", []):

                severity = vuln.get("Severity")

                if severity == "CRITICAL":
                    critical += 1

                elif severity == "HIGH":
                    high += 1

                elif severity == "MEDIUM":
                    medium += 1

                elif severity == "LOW":
                    low += 1

        if "critical" in question:
            return {
                "answer":
                f"There are {critical} critical vulnerabilities detected."
            }

        if "high" in question:
            return {
                "answer":
                f"There are {high} high vulnerabilities detected."
            }

        if "medium" in question:
            return {
                "answer":
                f"There are {medium} medium vulnerabilities detected."
            }

        if "low" in question:
            return {
                "answer":
                f"There are {low} low vulnerabilities detected."
            }

        return {
            "answer":
            "Ask about critical, high, medium or low vulnerabilities."
        }

    except Exception as e:

        return {
            "answer": str(e)
        }
