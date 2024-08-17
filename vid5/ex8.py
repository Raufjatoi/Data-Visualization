import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {'Values': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a histogram
sns.histplot(df['Values'], bins=5, kde=False)

# Add title and labels
plt.title('Histogram of Values')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show the plot
plt.show()
