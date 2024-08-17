import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Create a simple dataset
np.random.seed(0)
data = pd.DataFrame({
    'value': np.random.normal(loc=0, scale=1, size=1000)  # Normally distributed data
})

# Density Plot
plt.subplot(1, 3, 3)
sns.kdeplot(data['value'], fill=True)
plt.title('Density Plot')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()