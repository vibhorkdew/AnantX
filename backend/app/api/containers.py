from fastapi import APIRouter
import docker

router = APIRouter(prefix="/api", tags=["containers"])

@router.get("/containers")
def get_containers():
    try:
        client = docker.from_env()

        containers = []

        for c in client.containers.list():
            containers.append({
                "id": c.short_id,
                "name": c.name,
                "image": c.image.tags[0] if c.image.tags else "unknown",
                "status": c.status
            })

        return containers

    except Exception as e:
        return {"error": str(e)}
