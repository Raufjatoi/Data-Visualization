import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Values': [1, 2, 3, 4, 5, 6]}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a swarm plot
sns.swarmplot(x='Category', y='Values', data=df)

# Add title and labels
plt.title('Swarm Plot of Values by Category')
plt.xlabel('Category')
plt.ylabel('Values')

# Show the plot
plt.show()
