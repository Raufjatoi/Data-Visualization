import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {'X': [1, 2, 3, 4, 5],
        'Y': [2, 3, 5, 7, 11]}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a regression plot
sns.regplot(x='X', y='Y', data=df)

# Add title and labels
plt.title('Regression Plot')
plt.xlabel('X')
plt.ylabel('Y')

# Show the plot
plt.show()
