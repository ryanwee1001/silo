#!/bin/bash

for threads in 1 2 4 8 16;
do
    for scale in 1 2 4 8 16;
    do
        for time in 30 60 600 1200 3600;
        do
            /usr/bin/time -vo threads${threads}/scale${scale}runtime${time}.out ../out-perf.masstree/benchmarks/dbtest --verbose --bench tpcc --num-threads ${threads} --scale-factor ${scale} --runtime ${time}
        done
    done
done
