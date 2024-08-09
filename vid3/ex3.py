import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generate random data
np.random.seed(0)
x = np.random.rand(50) * 10
y = 2 * x + np.random.randn(50) * 2  # Linear relationship with some noise

# Create a DataFrame
data = pd.DataFrame({'X': x, 'Y': y})

# Create scatter plot with best fit line
plt.figure(figsize=(8, 6))
sns.regplot(x='X', y='Y', data=data, scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})

# Add titles and labels
plt.title('Scatter Plot with Best Fit Line')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show plot
plt.grid(True)
plt.show()
