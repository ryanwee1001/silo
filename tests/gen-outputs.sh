#!/bin/bash
# This script runs the TPC-C benchmark suite for some fixed number of threads 
# and some fixed scale factor. It runs the suite for some runtime values and 
# runs each test 10 times. It also does some work to aggregate the results for 
# easier analysis.

threads=1
scale=1
times=(10 20 30 60 100 200 300 400 500 600 700 800 900 1000) # in seconds

for time in "${times[@]}";
do
    for test in {1..2};
    do
        /usr/bin/time -vo time${time}test${test}.out \
            ../out-perf.masstree/benchmarks/dbtest --verbose \
                                                   --bench tpcc \
                                                   --num-threads ${threads} \
                                                   --scale-factor ${scale} \
                                                   --runtime ${time} \
            2> time${time}test${test}.stderr
    done
done

for time in "${times[@]}";
do
    cat time${time}test*.out | grep "Maximum resident set size" \
        >> time${time}aggregated.out
    cat time${time}test*.stderr | grep "avg_latency" \
        >> time${time}latency.stderr
    cat time${time}test*.stderr | grep "agg_throughput" \
        >> time${time}throughput.stderr  
done
