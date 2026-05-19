import numpy as np
import matplotlib.pyplot as plt

categories = np.array(["Carbohydrates", "Proteins", "Vitamins"])
values = np.array([1200, 120, 100])

plt.bar(categories, values, color="skyblue")
plt.title("Nutrition")
plt.xlabel("Category")
plt.ylabel("Value")

plt.show()