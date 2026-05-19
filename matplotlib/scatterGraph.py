import numpy as np
import matplotlib.pyplot as plt

hours = np.array([1,2,2,4,6, 6, 8])
grades = np.stack([55, 65, 75, 85, 85, 90, 92])

grades2 = np.stack([50, 60, 70, 80, 85, 91, 87])

plt.scatter(hours, grades, color="skyblue", label="Grades 1")
plt.scatter(hours, grades2, color="red", label="Grades 2")
plt.xlabel("Hours")
plt.ylabel("Grades")
plt.title("Grades vs Hours")
plt.legend()

plt.show()