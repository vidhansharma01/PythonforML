import matplotlib.pyplot as plt

x = [2023, 2024, 2025, 2026]
y1 = [15, 25, 80, 40]
y2 = [35, 25, 40, 30]
y3 = [35, 5, 30, 50]

plotvar = dict(marker=".", markersize=10, markerfacecolor="red", markeredgecolor="black",
               linestyle="solid", linewidth=3)

plt.title("Class size")
plt.xlabel("Year")
plt.ylabel("Students")
plt.tick_params(axis="both")
plt.xticks(x)
plt.grid(axis="both")

plt.plot(x, y1, **plotvar)
plt.plot(x, y2, **plotvar)
plt.plot(x, y3, **plotvar)

plt.show()

