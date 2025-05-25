# Car Sales Report Automation

This project processes car sales data from a JSON file, generates summary insights, outputs a PDF report using ReportLab, and emails the report via Python’s SMTP libraries.

## Features

- Analyzes sales data (most revenue, highest sales, most popular year)
- Generates professional PDF report using ReportLab
- Sends report via email using Python’s `smtplib` and `email` modules

## Technologies

- Python 3
- ReportLab
- SMTP / Email

## How to Use

1. Place `car_sales.json` in the working directory.
2. Run:

```bash
python3 cars.py
```

The PDF is saved to `/tmp/cars.pdf` and emailed to `student@example.com`.

## Author

Bekzod Ochilov
