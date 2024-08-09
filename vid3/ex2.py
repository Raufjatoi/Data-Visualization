import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(0)
x = np.random.rand(50) * 10
y = 2 * x + np.random.randn(50) * 2  # Linear relationship with some noise

# Calculate the best fit line
m, b = np.polyfit(x, y, 1)
best_fit_line = m * x + b

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', marker='o', label='Data points')

# Plot the best fit line
plt.plot(x, best_fit_line, color='red', linestyle='-', label='Best fit line')

# Add titles and labels
plt.title('Scatter Plot with Best Fit Line')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add legend
plt.legend()

# Show plot
plt.grid(True)
plt.show()
