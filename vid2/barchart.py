# the boiler plate code always have to write 
import seaborn as sns
import matplotlib.pyplot as plt
# import pandas as pd

# Sample data
data = {'Category': ['A', 'B', 'C', 'D'],
        'Value': [10, 20, 15, 25]}

# Create a Seaborn DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Create a bar plot
sns.barplot(x='Category', y='Value', data=df)

# Show plot
plt.title('Simple Bar Chart')
plt.show()
