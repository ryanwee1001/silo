#!/bin/bash
# This script sets up the repository for testing.

cd ..
sudo apt update
sudo apt install autoconf
sudo apt install libnuma-dev
sudo apt install libjemalloc-dev
sudo apt install libgoogle-perftools-dev
sudo apt install libdb5.3++-dev libmysqld-dev libaio-dev
make
make dbtest
