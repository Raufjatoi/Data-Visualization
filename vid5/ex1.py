import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020],
    'Sales': [250, 300, 350, 400, 450, 500]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the style for the plot
sns.set(style="whitegrid")

# Create a line plot
sns.lineplot(x='Year', y='Sales', data=df)

# Add titles and labels
plt.title('Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Sales')

# Show the plot
plt.show()
