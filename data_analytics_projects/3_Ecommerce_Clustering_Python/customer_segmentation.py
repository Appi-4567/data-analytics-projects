import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')  # Simulated example

# Example RFM-like feature (Total bill)
X = df[['total_bill', 'tip']]

# Apply KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

# Plot
plt.scatter(df['total_bill'], df['tip'], c=df['cluster'], cmap='viridis')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Customer Segmentation based on Tips Data')
plt.show()
