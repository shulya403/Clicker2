import matplotlib.pyplot as plt
import random

nums = [int(random.expovariate(0.2)) for i in range(1000)]

plt.plot(nums)
plt.show()

plt.hist(nums, bins=35)
plt.show()