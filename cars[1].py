#!/usr/bin/env python3

import json
import locale
import sys
import reports
import emails

def load_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data

def format_car(car):
    return "{} {} ({})".format(car["car_make"], car["car_model"], car["car_year"])

def process_data(data):
    max_revenue = {"revenue": 0}
    max_sales = {"total_sales": 0}
    year_sales = {}

    for item in data:
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price

        if item_revenue > max_revenue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item

        if item["total_sales"] > max_sales["total_sales"]:
            max_sales = item

        year = item["car"]["car_year"]
        year_sales[year] = year_sales.get(year, 0) + item["total_sales"]

    most_popular_year = max(year_sales, key=year_sales.get)

    summary = [
        "The {} generated the most revenue: ${:.2f}".format(format_car(max_revenue["car"]), max_revenue["revenue"]),
        "The {} had the most sales: {}".format(format_car(max_sales["car"]), max_sales["total_sales"]),
        "The most popular year was {} with {} sales.".format(most_popular_year, year_sales[most_popular_year])
    ]
    return summary

def cars_dict_to_table(car_data):
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table_data.append([
            item["id"],
            format_car(item["car"]),
            item["price"],
            item["total_sales"]
        ])
    return table_data

def main(argv):
    print("Starting script...")
    locale.setlocale(locale.LC_ALL, '')

    data = load_data("car_sales.json")
    print("Data loaded.")

    summary = process_data(data)
    print("Summary generated.")

    print("Generating PDF...")
    summary_text = "<br/>".join(summary)
    reports.generate("/tmp/cars.pdf", "Sales summary for last month", summary_text, cars_dict_to_table(data))
    print("PDF generated.")

    print("Sending email...")
    message = emails.generate(
        "automation@example.com",
        "student@example.com",
        "Sales summary for last month",
        "\n".join(summary),
        "/tmp/cars.pdf"
    )
    emails.send(message)
    print("Email sent.")

if __name__ == "__main__":
    main(sys.argv)
