import csv
from datetime import datetime
import random

# Here I'm entering the pivot file
with open("product_orders_copy.csv", "r", encoding="utf8") as file:
    # I read the pivot file and place the results in a list
    data = list(csv.reader(file))
    # I find the index of the word "product_id" in the first row of the CSV
    product_id_index = data[0].index("product_id")
    # I do the same for "order_date"
    order_date_index = data[0].index("order_date")
    # I iterate over the rows in the CSV file, starting from the second row
    for row in data[1:]:
        # I convert the order date to a datetime object and retrieve the year
        order_date = datetime.strptime(row[order_date_index], "%Y-%m-%d").year
        # I check the year and assign a product index accordingly
        match order_date:
            case 2019:
                row[product_id_index] = "102"
            case 2020:
                row[product_id_index] = random.choice(["101", "102"])
            case 2021:
                row[product_id_index] = random.choice(
                    ["100", "101", "102", "104", "105"]
                )

# This time I open the file you'll use in your project
with open("product_orders.csv", "w", newline="", encoding="utf8") as file:
    # I create a csv write object and specify the file it should write to
    writer = csv.writer(file)
    # I write the data list to the file
    writer.writerows(data)
