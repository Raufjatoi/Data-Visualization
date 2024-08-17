import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Create a simple dataset
np.random.seed(0)
data = pd.DataFrame({
    'value': np.random.normal(loc=0, scale=1, size=1000)  # Normally distributed data
})

# Histogram
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.histplot(data['value'], kde=False, bins=30)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Box Plot
plt.subplot(1, 3, 2)
sns.boxplot(x=data['value'])
plt.title('Box Plot')
plt.xlabel('Value')

# Density Plot
plt.subplot(1, 3, 3)
sns.kdeplot(data['value'], fill=True)
plt.title('Density Plot')
plt.xlabel('Value')
plt.ylabel('Density')

plt.tight_layout()
plt.show()
