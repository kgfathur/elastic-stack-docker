#!/bin/bash

docker-compose -f elastic-docker-tls.yml up -d
docker-compose -f elastic-docker-tls.yml ps