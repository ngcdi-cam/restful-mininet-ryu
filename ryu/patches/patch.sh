#!/bin/sh
set -e

cd "$(dirname $0)"

for patch in *.patch; do
    (cd /usr/lib/python3/dist-packages/ryu && patch -N -p0) < "$patch"
done
