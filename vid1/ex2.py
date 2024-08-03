import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create some example data
data = pd.DataFrame({
    'x': range(10),
    'y': [2*i + 1 for i in range(10)]
})

# Create a line plot
plt.figure(figsize=(8, 4))  # Set the figure size
sns.lineplot(data=data, x='x', y='y')
plt.title('Simple Line Plot')
plt.show()

print(range(10))