import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Y': [1, 2, 1.5, 3, 2.5, 4, 3.5, 4.5, 4, 5]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a joint plot with KDE
sns.jointplot(x='X', y='Y', data=df, kind='kde', fill=True)

# Add title
plt.suptitle('Joint Plot with KDE', y=1.02)

# Show the plot
plt.show()
