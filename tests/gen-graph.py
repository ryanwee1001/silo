# This script generates a graphical representation of the test results.

import numpy as np
import matplotlib.pyplot as plt

### DATA (SEP 27) ###

# res[num_threads][scale_factor][axis]
res = dict()    
res[1] = dict()
res[1][1] = dict()
res[1][1]["x"] = [30, 60, 600, 1200, 3600]
res[1][1]["y"] = [1.022, 1.846, 16.556, 29.775, 95.116]
res[1][2] = dict()
res[1][2]["x"] = [30, 60, 600, 3600]
res[1][2]["y"] = [1.210, 2.169, 18.234, 93.288]
res[1][4] = dict()
res[1][4]["x"] = [30, 60, 600]
res[1][4]["y"] = [1.401, 2.400, 19.434]
res[1][8] = dict()
res[1][8]["x"] = [30, 60, 600]
res[1][8]["y"] = [1.802, 2.730, 19.320]
res[1][16] = dict()
res[1][16]["x"] = [30, 60, 600]
res[1][16]["y"] = [2.483, 3.280, 19.046]
res[1][24] = dict()
res[1][24]["x"] = [30, 60, 600]
res[1][24]["y"] = [2.898, 3.598, 15.885]
res[1][128] = dict()
res[1][128]["x"] = [30, 60, 600]
res[1][128]["y"] = [13.027, 13.586, 20.525]

res[2] = dict()
res[2][1] = dict()
res[2][1]["x"] = [30, 60, 600, 1200]
res[2][1]["y"] = [1.404, 2.593, 12.818, 17.030]
res[2][2] = dict()
res[2][2]["x"] = [30, 60, 600]
res[2][2]["y"] = [1.966, 3.568, 30.675]
res[2][4] = dict()
res[2][4]["x"] = [30, 60, 600]
res[2][4]["y"] = [2.253, 4.137, 34.784]
res[2][16] = dict()
res[2][16]["x"] = [30, 60, 600]
res[2][16]["y"] = [2.697, 4.457, 35.825]
res[2][24] = dict()
res[2][24]["x"] = [30, 60]
res[2][24]["y"] = [3.632, 4.903]
res[2][128] = dict()
res[2][128]["x"] = [30, 60]
res[2][128]["y"] = [13.668, 14.942]

res[4] = dict()
res[4][8] = dict()
res[4][8]["x"] = [60, 600]
res[4][8]["y"] = [7.090, 53.823]
res[4][16] = dict()
res[4][16]["x"] = [30, 60, 600]
res[4][16]["y"] = [4.933, 7.545, 54.082]

res[8] = dict()
res[8][8] = dict()
res[8][8]["x"] = [60, 600]
res[8][8]["y"] = [11.757, 64.068]
res[8][16] = dict()
res[8][16]["x"] = [30, 60, 600]
res[8][16]["y"] = [7.630, 12.998, 66.882]

res[16] = dict()
res[16][8] = dict()
res[16][8]["x"] = [60, 600]
res[16][8]["y"] = [14.035, 66.458]
res[16][16] = dict()
res[16][16]["x"] = [30, 60, 600]
res[16][16]["y"] = [12.203, 22.461, 81.831]

### DATA (OCT 1) ###

res_oct_x = [10, 20, 30, 60, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
res_oct_y = [
    0.4418832, 
    0.6872052,
    0.9238940,
    1.6760308,
    2.6624640,
    5.1311284,
    7.6060028,
    9.9832356,
    12.2947784,
    15.0971908,
    17.7542932,
    20.6066664,
    22.5965756,
    24.9462280,
]

res_throughput_x = [10, 20, 30, 60, 100, 600, 900, 1000]
res_throughput_y = [
    65299.70, 
    62892.34,
    61881.52,
    60528.42,
    61193.30,
    59875.10, 
    59208.68, 
    58854.55,
]

res_latency_x = [10, 20, 30, 60, 100, 600, 900, 1000]
res_latency_y = [
    15.28042,
    15.87654,
    16.14138,
    16.50482,
    16.33013,
    16.68464, 
    16.86774, 
    16.96458,
]

### LINEAR FITTING ###

# fns[num_threads][scale_factor]
fns = dict()
for num_threads in [1, 2, 4, 8, 16]:
    fns[num_threads] = dict()
for scale_factor in [1, 2, 4, 8, 16, 24, 128]:
    coef = np.polyfit(res[1][scale_factor]["x"], res[1][scale_factor]["y"], 1)
    fns[1][scale_factor] = np.poly1d(coef)
for scale_factor in [1, 2, 4, 16, 24, 128]:
    coef = np.polyfit(res[2][scale_factor]["x"], res[2][scale_factor]["y"], 1)
    fns[2][scale_factor] = np.poly1d(coef) 
for num_threads in [4, 8, 16]:
    for scale_factor in [8, 16]:
        coef = np.polyfit(res[num_threads][scale_factor]["x"], res[num_threads][scale_factor]["y"], 1)
        fns[num_threads][scale_factor] = np.poly1d(coef) 

### PLT BOILERPLATE ###

plt.xlabel("Runtime (sec)")
plt.ylabel("Peak RSS (GB)")

def plot(
    num_threads: int, 
    scale_factor: int, 
    color: str, 
    xmax: int, 
    ymax: int, 
) -> None:
    plt.plot(res[num_threads][scale_factor]["x"], res[num_threads][scale_factor]["y"], 'o', color=color)
    plt.plot(res[num_threads][scale_factor]["x"], fns[num_threads][scale_factor](res[num_threads][scale_factor]["x"]), color=color, label=f"threads{num_threads}scale{scale_factor}")
    plt.xlim(0, xmax)
    plt.ylim(0, ymax)

### GRAPHS ###

# Graph 1: Effect of runtime
# plot(1, 1, "orange", 4000, 100)
# plot(1, 2, "green", 4000, 100)
# plt.title(label="RSS scales with runtime")

# Graph 2: Effect of scale factor
# plot(1, 1, "orange", 400, 15)
# plot(1, 2, "green", 400, 15)
# plot(1, 4, "black", 400, 15)
# plot(1, 8, "purple", 400, 15)
# plot(1, 16, "blue", 400, 15)
# plot(1, 24, "pink", 400, 15)
# plot(1, 128, "red", 400, 15)
# plt.title(label="Starting value scales with scale factor (1 thread)")

# Graph 3: Effect of scale factor
# plot(2, 1, "orange", 400, 15)
# plot(2, 2, "green", 400, 15)
# plot(2, 4, "black", 400, 15)
# plot(2, 16, "blue", 400, 15)
# plot(2, 24, "pink", 400, 15)
# plot(2, 128, "red", 400, 15)
# plt.title(label="Starting value scales with scale factor (2 threads)")

# Graph 4: Effect of number of threads
# plot(1, 16, "blue", 900, 90)
# plot(2, 16, "orange", 900, 90)
# plot(4, 16, "green", 900, 90)
# plot(8, 16, "black", 900, 90)
# plot(16, 16, "red", 900, 90)
# plt.title(label="Gradient scales with number of threads")

# Graph 5: RSS
# plt.plot(res_oct_x, res_oct_y, 'o', color="black")
# coef = np.polyfit(res_oct_x, res_oct_y, 1)
# fn = np.poly1d(coef)
# plt.plot(res_oct_x, fn(res_oct_x), color="black", label=f"threads1scale1")
# plt.xlim(0, 1000)
# plt.ylim(0, 25)
# plt.title(label="RSS (number threads 1, scale factor 1)")

# Graph 6: Throughput
# plt.plot(res_throughput_x, res_throughput_y, 'o', color="black")
# coef = np.polyfit(res_throughput_x, res_throughput_y, 1)
# fn = np.poly1d(coef)
# plt.plot(res_throughput_x, fn(res_throughput_x), color="black", label=f"threads1scale1")
# plt.xlim(0, 1000)
# plt.ylim(57000, 66000)
# plt.xlabel("Runtime (sec)")
# plt.ylabel("Throughput (ops/sec)")
# plt.title(label="Throughput (number threads 1, scale factor 1)")

# Graph 7: Latency
# plt.plot(res_latency_x, res_latency_y, 'o', color="black")
# coef = np.polyfit(res_latency_x, res_latency_y, 1)
# fn = np.poly1d(coef)
# plt.plot(res_latency_x, fn(res_latency_x), color="black", label=f"threads1scale1")
# plt.xlim(0, 1000)
# plt.ylim(15, 17)
# plt.xlabel("Runtime (sec)")
# plt.ylabel("Latency (microsec)")
# plt.title(label="Latency (number threads 1, scale factor 1)")

### PLT BOILERPLATE ###

plt.legend()
plt.show()
