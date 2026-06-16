from fastapi import APIRouter
import json

router = APIRouter(prefix="/api", tags=["vulnerabilities"])

TRIVY_REPORT = "reports/trivy-report.json"

@router.get("/vulnerabilities")
def get_vulnerabilities():

    try:

        with open(TRIVY_REPORT, "r") as f:
            data = json.load(f)

        vulnerabilities = []

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

                vulnerabilities.append({
                    "id": vuln.get("VulnerabilityID"),
                    "package": vuln.get("PkgName"),
                    "severity": severity,
                    "title": vuln.get("Title")
                })

        return {
            "critical": critical,
            "high": high,
            "medium": medium,
            "low": low,
            "count": len(vulnerabilities),
            "vulnerabilities": vulnerabilities
        }

    except Exception as e:
        return {"error": str(e)}
