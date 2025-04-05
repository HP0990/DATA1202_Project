
import pandas as pd

# Load dataset
df = pd.read_csv('vgsales.csv')

# Remove rows where 'Year' is missing
df_clean = df.dropna(subset=['Year'])

# Convert 'Year' from float to int
df_clean['Year'] = df_clean['Year'].astype(int)

# Create a new column for 'SalesPeriod' based on year
df_clean['SalesPeriod'] = df_clean['Year'].apply(lambda x: 'pre-2005' if x < 2005 else 'post-2005')

# Calculate average global sales for each period
avg_sales = df_clean.groupby('SalesPeriod')['Global_Sales'].mean().reset_index()
print("Average Global Sales by Period:")
print(avg_sales)

# Save cleaned dataset and results
df_clean.to_csv('vgsales_cleaned.csv', index=False)
avg_sales.to_csv('average_sales_by_period.csv', index=False)

print("Data cleaning and transformation complete. Files saved: 'vgsales_cleaned.csv', 'average_sales_by_period.csv'.")
