from fastapi import APIRouter
import docker

router = APIRouter(
    prefix="/api",
    tags=["containers"]
)

@router.get("/containers")
def get_containers():

    client = docker.from_env()

    containers = client.containers.list(all=True)

    result = []

    for c in containers:

        result.append({
            "name": c.name,
            "status": c.status
        })

    return result