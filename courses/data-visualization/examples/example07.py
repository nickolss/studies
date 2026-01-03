import numpy as np
import matplotlib.pyplot as plt

print(np.random.randint(0, 10, 50)) # Print 50 random numbers between 0 and 10

plt.plot(np.random.normal(10, 0.5, 10_000))
plt.show()