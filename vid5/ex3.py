import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a heatmap
sns.heatmap(df, annot=True, cmap="YlGnBu")

# Add title
plt.title('Heatmap of Data')

# Show the plot
plt.show()
