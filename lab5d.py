import csv
import matplotlib.pyplot as plt

products = []
sales = []
quantities = []

total_sales = 0
total_quantity = 0

# Read CSV file

with open("sales.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        product = row["Product"]
        quantity = int(row["Quantity"])
        price = float(row["Price"])

        revenue = quantity * price

        products.append(product)
        sales.append(revenue)
        quantities.append(quantity)

        total_sales += revenue
        total_quantity += quantity


# Display Sales Report

print("\n----- RETAIL SALES REPORT -----")

for i in range(len(products)):

    print("\nProduct:", products[i])
    print("Quantity Sold:", quantities[i])
    print("Total Sales:", sales[i])


# Find highest-selling product by revenue

highest_index = sales.index(max(sales))

print("\n----- SALES SUMMARY -----")

print("Total Revenue: Rs.", total_sales)

print("Total Quantity Sold:", total_quantity)

print("Highest Revenue Product:", products[highest_index])

print("Highest Revenue: Rs.", sales[highest_index])


# Bar Chart

plt.figure(figsize=(8, 5))

plt.bar(products, sales)

plt.title("Product-wise Retail Sales")

plt.xlabel("Products")

plt.ylabel("Sales Revenue")

plt.show()


# Pie Chart

plt.figure(figsize=(7, 7))

plt.pie(
    sales,
    labels=products,
    autopct="%1.1f%%"
)

plt.title("Retail Sales Distribution")

plt.show()