import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create a heat map
sns.heatmap(data, annot=True, cmap='coolwarm')

# Show plot
plt.title('Simple Heat Map')
plt.show()
