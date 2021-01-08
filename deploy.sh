#!/bin/bash
source es-env
docker stack deploy -c docker-compose.yml es-stack
