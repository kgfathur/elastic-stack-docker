#!/bin/bash

rm -vrf /data/es-master{1..3}/*
rm -vrf /data/es-master{1..3}/.[^\.][a-zA-Z]*

rm -vrf /data/es-data{1..4}/*
rm -vrf /data/es-data{1..4}/.[^\.][a-zA-Z]*

rm -vrf /data/es-coor{1..3}/*
rm -vrf /data/es-coor{1..3}/.[^\.][a-zA-Z]*

# rm -vrf /data/prometh{1..3}/*
# rm -vrf /data/prometh{1..3}/.[^\.][a-zA-Z]*

# rm -vrf /data/sidecar{1..3}/*
# rm -vrf /data/sidecar{1..3}/.[^\.][a-zA-Z]*

# rm -vrf /data/kibana/*
# rm -vrf /data/kibana/.[^\.][a-zA-Z]*

# rm -vrf /data/grafana/*
# rm -vrf /data/grafana/.[^\.][a-zA-Z]*

tree -fal /data/