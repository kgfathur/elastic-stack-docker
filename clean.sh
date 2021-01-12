#!/bin/bash

sudo rm -vrf /data/es0{1..3}/*
sudo rm -vrf /data/es0{1..3}/.[^\.][a-zA-Z]*

sudo rm -vrf /data/log_es0{1..3}/*
sudo rm -vrf /data/log_es0{1..3}/.[^\.][a-zA-Z]*

sudo rm -vrf /data/prometheus{0..2}/*
sudo rm -vrf /data/prometheus{0..2}/.[^\.][a-zA-Z]*

sudo rm -vrf /data/sidecar{0..2}/*
sudo rm -vrf /data/sidecar{0..2}/.[^\.][a-zA-Z]*

sudo rm -vrf /data/kibana/*
sudo rm -vrf /data/kibana/.[^\.][a-zA-Z]*

sudo rm -vrf /data/grafana/*
sudo rm -vrf /data/grafana/.[^\.][a-zA-Z]*

sudo ls -lRa /data