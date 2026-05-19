import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(50, 10, 1000)

plt.hist(
    data,
    bins=20,
    color="orange",
    edgecolor="black",
    alpha=0.7
)

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Normal Distribution")

plt.show()