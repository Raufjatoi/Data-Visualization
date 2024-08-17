import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {'X': [1, 2, 3, 4, 5],
        'Y': [5, 4, 3, 2, 1],
        'Category': ['A', 'A', 'B', 'B', 'A']}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a scatter plot
sns.scatterplot(x='X', y='Y', hue='Category', data=df)

# Add title and labels
plt.title('Scatter Plot with Categories')
plt.xlabel('X')
plt.ylabel('Y')

# Show the plot
plt.show()
