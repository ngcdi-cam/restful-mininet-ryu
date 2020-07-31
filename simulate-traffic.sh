#!/bin/bash

SRC_HOST=${1:-h1}
DST_HOST=${2:-h2}
BANDWIDTH=${3:-50000000}
DURATION=${4:-20}

MN_API_URL=${MN_API_URL:-"http://localhost:8081"}

exec curl -d "iperf -u -t $DURATION -c $DST_HOST -b $BANDWIDTH" "$MN_API_URL/nodes/$SRC_HOST/cmd"
