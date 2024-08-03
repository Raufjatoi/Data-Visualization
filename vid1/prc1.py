#setup code (always have code)
import pandas as pd 
import matplotlib.pyplot as plt # the pd and plt are just alias u can create your own 
import seaborn as sns 

# lezz use some real data now 
data = pd.read_csv("fifa.csv", index_col='Date',parse_dates=True)

# now lezz create a simple graph 
#plot size
plt.figure(figsize=(16,6))

# simple line chart showing how FIFA rankings evolved over time
sns.lineplot(data=data)
plt.show()

