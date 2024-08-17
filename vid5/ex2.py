import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {'Category': ['A', 'B', 'C', 'D'],
        'Values': [4, 7, 1, 8]}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar plot
sns.barplot(x='Category', y='Values', data=df)

# Add title and labels
plt.title('Bar Plot of Values by Category')
plt.xlabel('Category')
plt.ylabel('Values')

# Show the plot
plt.show()
