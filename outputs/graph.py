import numpy as np
import matplotlib.pyplot as plt

### DATA ###

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

def plot(num_threads: int, scale_factor: int, color: str, xmax: int, ymax: int) -> None:
    plt.plot(res[num_threads][scale_factor]["x"], res[num_threads][scale_factor]["y"], 'o', color=color)
    plt.plot(res[num_threads][scale_factor]["x"], fns[num_threads][scale_factor](res[num_threads][scale_factor]["x"]), color=color, label=f"t{num_threads}s{scale_factor}")
    plt.xlim(0, xmax)
    plt.ylim(0, ymax)

### GRAPHS ###

# Graph 1: Effect of runtime
# plot(1, 1, "orange", 4000, 100)
# plot(1, 2, "green", 4000, 100)

# Graph 2: Effect of scale factor
# plot(1, 1, "orange", 1500, 40)
# plot(1, 2, "green", 1500, 40)
# plot(1, 4, "black", 1500, 40)
# plot(1, 8, "purple", 1500, 40)
# plot(1, 16, "blue", 1500, 40)
# plot(1, 24, "pink", 1500, 40)

# Graph 3: Effect of scale factor
# plot(2, 2, "green", 900, 30)
# plot(2, 4, "black", 900, 30)
# plot(2, 16, "blue", 900, 30)
# plot(2, 24, "pink", 900, 30)

# Graph 4: Effect of huge scale factor
# plot(1, 1, "orange", 1500, 40)
# plot(1, 2, "green", 1500, 40)
# plot(1, 128, "red", 1500, 40)
# plot(2, 128, "black", 1500, 40)

# Graph 5: Effect of runtime is logarithmic?
# plot(2, 1, "orange", 900, 30)

# Graph 6: Effect of number of threads
# plot(1, 16, "blue", 900, 90)
# plot(2, 16, "orange", 900, 90)
# plot(4, 16, "green", 900, 90)
# plot(8, 16, "black", 900, 90)
# plot(16, 16, "red", 900, 90)

### PLT BOILERPLATE ###

plt.legend()
plt.show()
