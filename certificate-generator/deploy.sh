#!/bin/bash

source ../.env
docker-compose -f docker-compose.yml run --rm create_certs
