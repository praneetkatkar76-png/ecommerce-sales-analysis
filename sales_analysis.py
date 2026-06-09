import pandas as pd

# Load CSV file
data = pd.read_csv("sales_data.csv")

# Convert Date column to datetime
data["Date"] = pd.to_datetime(data["Date"])

# Create Month column
data["Month"] = data["Date"].dt.month_name()

# Create Revenue column
data["Revenue"] = data["Quantity"] * data["Price"]

# Display data
print(data)

#Calculate total revenue
total_revenue = data["Revenue"].sum()

print("\nTotal Revenue:", total_revenue)

# Product-wise quantity sold
product_sales = data.groupby("Product")["Quantity"].sum()

print("\nProduct Sales:")
print(product_sales)

# Top-selling product
top_product = product_sales.idxmax()
top_quantity = product_sales.max()

print("\nTop Selling Product:", top_product)
print("Units Sold:", top_quantity)

import matplotlib.pyplot as plt

# Create bar chart
product_sales.plot(kind="bar")

plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")

import matplotlib.pyplot as plt

# Create bar chart
product_sales.plot(kind="bar")

plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")

import matplotlib.pyplot as plt

# Create bar chart
product_sales.plot(kind="bar")

plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")

plt.savefig("product_sales_chart.png")
print("Chart saved successfully!")

# Category-wise revenue
category_revenue = data.groupby("Category")["Revenue"].sum()

print("\nCategory Revenue:")
print(category_revenue)

best_category = category_revenue.idxmax()
best_revenue = category_revenue.max()

print("\nBest Category:", best_category)
print("Revenue:", best_revenue)

print("\n----- BUSINESS INSIGHTS -----")

print(f"Total Revenue Generated: ₹{total_revenue}")

print(f"Top Selling Product: {top_product} ({top_quantity} units sold)")

print(f"Best Performing Category: {best_category} (₹{best_revenue} revenue)")

# Category Revenue Chart
category_revenue.plot(kind="bar")

plt.title("Category Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue")

plt.savefig("category_revenue_chart.png")
print("Category Revenue Chart saved successfully!")

monthly_revenue = data.groupby(data["Date"].dt.month_name())["Revenue"].sum()

month_order = ["January", "February", "March", "April",
               "May", "June", "July", "August",
               "September", "October", "November", "December"]

monthly_revenue = monthly_revenue.reindex(month_order).dropna()

print(monthly_revenue)

