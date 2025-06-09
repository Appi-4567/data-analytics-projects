import pandas as pd
import matplotlib.pyplot as plt

# Load COVID-19 data
df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv')

# Top 10 countries by total cases
top_countries = df.sort_values('total_cases', ascending=False).head(10)

# Plot
plt.figure(figsize=(10, 6))
plt.bar(top_countries['location'], top_countries['total_cases'])
plt.xticks(rotation=45)
plt.title('Top 10 Countries by Total COVID-19 Cases')
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.tight_layout()
plt.show()
