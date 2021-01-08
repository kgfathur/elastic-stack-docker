#!/bin/bash

source es-env
docker stack deploy -c es-stack.yml es
