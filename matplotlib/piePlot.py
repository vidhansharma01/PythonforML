import numpy as np
import matplotlib.pyplot as plt

categories = np.array(["Fisherman", "Farmer", "Porter"])
values = np.array([200, 120, 100])

plt.pie(values, labels=categories, autopct="%1.1f%%", explode=(0, 0, 0.1))

plt.title("Pie Chart")
plt.show()