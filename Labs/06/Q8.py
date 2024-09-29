import pandas as pd

# a) Load CSV files
products_df = pd.read_csv('products.csv')
orders_df = pd.read_csv('orders.csv')

# b) Display the first 5 and last 10 rows
print("First 5 rows of Products DataFrame:")
print(products_df.head())
print("\nLast 10 rows of Products DataFrame:")
print(products_df.tail(10))

print("\nFirst 5 rows of Orders DataFrame:")
print(orders_df.head())
print("\nLast 10 rows of Orders DataFrame:")
print(orders_df.tail(10))

# c) Calculate total revenue
# Ensure column names match the file headers
merged_df = pd.merge(orders_df, products_df, on="Product ID")  # Merge on "Product ID"
merged_df["Revenue"] = merged_df["Quantity"] * merged_df["Price"]

total_revenue = merged_df["Revenue"].sum()
print("\nTotal Revenue Generated from All Orders:", total_revenue)

# d) Best-selling products by quantity
best_selling = merged_df.groupby("Product Name")["Quantity"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Best-Selling Products:\n", best_selling)

# d) Low-selling products by quantity
low_selling = merged_df.groupby("Product Name")["Quantity"].sum().sort_values(ascending=True).head(5)
print("\nTop 5 Low-Selling Products:\n", low_selling)

# e) Most common category among the top 5 best-selling products
top_5_products = merged_df[merged_df["Product Name"].isin(best_selling.index)]
most_common_category = top_5_products["Category"].mode()[0]
print("\nMost Common Product Category Among Top 5 Best-Selling Products:", most_common_category)

# f) Calculate and display the average price of products in each category
avg_price_by_category = products_df.groupby("Category")["Price"].mean()
print("\nAverage Price of Products by Category:\n", avg_price_by_category)

# Convert 'Order Date' to datetime and extract day, month, year
merged_df["Order Date"] = pd.to_datetime(merged_df["Order Date"], format="%m-%d-%Y", errors="coerce")
merged_df["Day"] = merged_df["Order Date"].dt.day
merged_df["Month"] = merged_df["Order Date"].dt.month
merged_df["Year"] = merged_df["Order Date"].dt.year

# g) Day with highest total revenue
day_highest_revenue = merged_df.groupby("Day")["Revenue"].sum().idxmax()
print("\nDay with Highest Total Revenue:", day_highest_revenue)

# g) Month with highest total revenue
month_highest_revenue = merged_df.groupby("Month")["Revenue"].sum().idxmax()
print("Month with Highest Total Revenue:", month_highest_revenue)

# g) Year with highest total revenue
year_highest_revenue = merged_df.groupby("Year")["Revenue"].sum().idxmax()
print("Year with Highest Total Revenue:", year_highest_revenue)

# h) New DataFrame to show the total revenue for each month
monthly_revenue_df = merged_df.groupby("Month")["Revenue"].sum().reset_index()
print("\nMonthly Revenue DataFrame:\n", monthly_revenue_df)

# i) Check for null values
print("\nNull Values in Data:")
print(merged_df.isnull().sum())
