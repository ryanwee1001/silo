#!/bin/bash

sudo apt update
sudo apt install autoconf
sudo apt install libnuma-dev
sudo apt install libjemalloc-dev
sudo apt install libgoogle-perftools-dev
sudo apt install libdb5.3++-dev libmysqld-dev libaio-dev
make
make dbtest
./out-perf.masstree/benchmarks/dbtest \
    --verbose \
    --bench tpcc \
    --num-threads 2 \
    --scale-factor 28 \
    --runtime 30 \
