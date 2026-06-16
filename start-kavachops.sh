#!/bin/bash

cd ~/KavachOps

echo "Starting KavachOps..."

docker compose up -d

docker start jenkins 2>/dev/null
docker start sonarqube 2>/dev/null

echo ""
echo "Running Containers:"
docker ps
