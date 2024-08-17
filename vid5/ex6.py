import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {'X': [1, 2, 3, 4, 5, 6],
        'Y': [2, 4, 5, 7, 8, 10],
        'Category': ['A', 'A', 'B', 'B', 'A', 'B']}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a linear model plot
sns.lmplot(x='X', y='Y', hue='Category', data=df)

# Add title and labels
plt.title('Linear Model Plot by Category')
plt.xlabel('X')
plt.ylabel('Y')

# Show the plot
plt.show()
