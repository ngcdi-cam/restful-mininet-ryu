#!/bin/sh
run_containers.py -c ryu-config.yaml && run_containers.py -c mininet-config.yaml
