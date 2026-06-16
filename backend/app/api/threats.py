from fastapi import APIRouter

router = APIRouter()

@router.get("/threats")
def get_threats():

    return [

        {
            "id": "THR-001",
            "severity": "CRITICAL",
            "source": "Trivy",
            "status": "ACTIVE",
            "description": "Multiple critical vulnerabilities detected"
        },

        {
            "id": "THR-002",
            "severity": "HIGH",
            "source": "Falco",
            "status": "ACTIVE",
            "description": "Suspicious shell execution"
        },

        {
            "id": "THR-003",
            "severity": "HIGH",
            "source": "Docker",
            "status": "MONITORING",
            "description": "Container exposed on public network"
        },

        {
            "id": "THR-004",
            "severity": "MEDIUM",
            "source": "Jenkins",
            "status": "INVESTIGATING",
            "description": "Multiple failed login attempts"
        },

        {
            "id": "THR-005",
            "severity": "LOW",
            "source": "Monitoring",
            "status": "RESOLVED",
            "description": "Temporary CPU spike detected"
        }

    ]