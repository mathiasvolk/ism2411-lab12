""" --- Self-Reflection Questions ---

1) Python is particularly useful for automating repetitive tasks and processing large 
amounts of data, while Excel makes it easier to visually inspect data, create charts, 
and make quick manual adjustments.


2) A business could use an append-mode log file to track each customer's purchases or 
transactions over time. Append mode is useful because it adds each new transaction 
without deleting previous records, allowing the business to maintain a continuous
history of its activity.

"""


import csv
from datetime import datetime

# --- Exercise 2 ---

with open("data/sales.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# --- Exercise 3 ---

with open("data/sales.csv","r") as file:
    reader = csv.reader(file)

    header = next(reader)  
    print("Header:", header)

    for row in reader:
        print(row)

# --- Exercise 4 ---

with open("data/sales.csv","r") as file:
    reader = csv.reader(file)
    header = next (reader)  

    total_revenue = 0

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

    print(f"Total Revenue: ${total_revenue:.2f}")

# --- Exercise 5 ---

with open("data/sales.csv","r") as file:
    reader = csv.reader(file)
    header = next(reader)

    cleaned_rows = []
    original_count = 0 

    for row in reader:
        original_count += 1
        
        product = row[0]
        price = row[1]
        quantity = row[2]

        total = float(price) * int(quantity)

        if total > 100:
            cleaned_rows.append([product, price, quantity, total])

with open("data/cleaned.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Product", "Price", "Qty", "Total"])
    writer.writerows(cleaned_rows)

print(f"Rows Written: {len(cleaned_rows)}")
print(f"Original Rows: {original_count}")

# --- Exercise 6 ---

import csv

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    dict_total = 0

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total Revenue using DictReader: ${dict_total:.2f}")

# DictReader uses column names to access columns, while csv.reader uses numerican indexes.
# DictReader is easier to read when working with csv files that have clear column headers.

# --- Exercise 7 ---

sales_summary = {}

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

print("\nSales Summary by Product:")

for product in sorted(sales_summary):
   print(f"{product}: ${sales_summary[product]:.2f}")

# --- Exercise 8 --- 

from datetime import datetime

with open("data/run_log.txt", "a") as file:
          timestamp = datetime.now()
          file.write(f"{timestamp} - Total Revenue: ${dict_total:.2f}\n")

print("Run log updated with total revenue.")

