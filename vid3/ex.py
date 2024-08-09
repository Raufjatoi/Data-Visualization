import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(0)
x = np.random.rand(50) * 10
y = np.random.rand(50) * 10

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', marker='o')

# Add titles and labels
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show plot
plt.grid(True)
plt.show()
