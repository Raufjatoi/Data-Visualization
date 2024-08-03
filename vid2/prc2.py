#setup the thing importin libs with alias 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

#reading data
data = pd.read_csv("ign_scores.csv" , index_col='Platform')
#print(data.head())

#bar chart

plt.figure(figsize=(8,6)) # size width and height
sns.barplot(x=data['Racing'], y=data.index)
plt.xlabel("")
plt.title("Average Score for Racing Games , by Plotform")
#plt.show()

# Heat map now 

plt.figure(figsize=(10,10))
sns.heatmap(data , annot = False ) # try annot to make it true and see the change 
plt.xlabel('Genre')
plt.title("Average Game Score, by Plotform and Genre")
plt.show()