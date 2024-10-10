import pandas as pd
import matplotlib.pyplot as plt
# Url 
url = 'https://raw.githubusercontent.com/weekysui/Sales_conversion/master/KAG_conversion_data.csv'
df = pd.read_csv(url, low_memory=False)

mean_value = df['Approved_Conversion'].mean()
median_value = df['Approved_Conversion'].median()
mode_value = df['Approved_Conversion'].mode()[0]
var_value = df['Approved_Conversion'].var()
sd_value = df['Approved_Conversion'].std()
skew_value = df['Approved_Conversion'].skew()
kur_value = df['Approved_Conversion'].kurt()

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Variance: {var_value}")
print(f"Standard Deviation: {sd_value}")
print(f"Skewness: {skew_value}")
print(f"Kurtosis: {kur_value}")

df['Approved_Conversion'].value_counts().plot(kind='bar', title='Impressions Count')
plt.title('Distribution of Approved Conversion]')
plt.xlabel('Approved_Conversion')
plt.ylabel('Total_Conversion')
plt.show()