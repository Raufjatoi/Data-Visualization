import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {'Values': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a KDE plot
sns.kdeplot(df['Values'], fill=True)

# Add title and labels
plt.title('KDE Plot of Values')
plt.xlabel('Value')
plt.ylabel('Density')

# Show the plot
plt.show()
