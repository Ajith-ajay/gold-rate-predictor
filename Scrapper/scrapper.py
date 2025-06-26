import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL of the page
url = "https://www.exchange-rates.org/precious-metals/gold-price/india/2024"

# Send a request to fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 1: Find all <h3> month headings (each month has a table below it)
headings = soup.find_all("h3")

# Step 2: Filter only headings related to month tables
monthly_tables = []
for heading in headings:
    if "2024" in heading.text:  # Should match "January 2024", ..., "December 2024"
        month_name = heading.text.strip()
        table = heading.find_next("table")
        df = pd.read_html(str(table))[0]

        # Optional: add the month as a new column
        df["Month"] = month_name
        monthly_tables.append(df)

# Step 3: Combine all monthly tables into a single DataFrame
# combined_df = pd.concat(monthly_tables, ignore_index=True)

# Step 4: Save to CSV
# combined_df.to_csv("India_Gold_Price_2024.csv", index=False)
print(monthly_tables)

# (Optional) Save to Excel instead
# combined_df.to_excel("India_Gold_Price_2024.xlsx", index=False)

print("Scraping complete. Data saved to 'India_Gold_Price_2024.csv'")
