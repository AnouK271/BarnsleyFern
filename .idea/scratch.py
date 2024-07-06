import matplotlib.pyplot as plt
import random

# Initialize lists to hold the x and y coordinates of the points
x_points = [0]
y_points = [0]

# Number of points to generate
num_points = 50000

# Function to generate the Barnsley Fern
def barnsley_fern(x, y):
    rand = random.random()
    if rand < 0.01:
        return 0, 0.16 * y
    elif rand < 0.86:
        return 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
    elif rand < 0.93:
        return 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
    else:
        return -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

# Generate the points for the fern
for _ in range(num_points):
    x, y = barnsley_fern(x_points[-1], y_points[-1])
    x_points.append(x)
    y_points.append(y)

# Plot the points
plt.figure(figsize=(6, 10))
plt.scatter(x_points, y_points, s=0.1, color='green')
plt.title("Barnsley Fern")
plt.show()

