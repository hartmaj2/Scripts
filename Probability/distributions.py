import random
import matplotlib.pyplot as plt
import numpy as np
import math

num_samples = 1_000_000
data_y = [0] * num_samples
sum = 0
for i in range(len(data_y)):
    data_y[i] = random.uniform(0,1)
    sum += data_y[i]
mean_y = sum / len(data_y)

sum = 0
for i in range(len(data_y)):
    sum += (data_y[i] - mean_y) ** 2
stdev_y = math.sqrt(sum / len(data_y))

sum = 0
for i in range(len(data_y)):
    sum += data_y[i] <= 0.4
p_leq = sum / len(data_y)

data_x = [1/y for y in data_y]
mean_x = np.mean(data_x)
stdev_x = np.std(data_x)

sum = 0
for i in range(len(data_x)):
    sum += 2 <= data_x[i] <= 3
p_intvl = sum / len(data_x)

print()
print("--- Y ---")
print(f"E[Y] = {mean_y}")
print(f"σ(Y) = {stdev_y}")
print(f"P(Y<=0.4) = {p_leq}")
print()
print("--- X ---")
print(f"E[X] =  {mean_x}")
print(f"σ(X) = {stdev_x}")
print(f"P(2<=X<=3) = {p_intvl}")

plt.figure(figsize=(10, 6))
plt.title(f"Histogram of {num_samples} samples of random variable X")
plt.xlabel("Value of X")
plt.ylabel("Count")
plt.hist(data_x,bins=np.arange(0,30,1),edgecolor='black')
plt.show()
