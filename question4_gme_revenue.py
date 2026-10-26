import requests
from bs4 import BeautifulSoup
import pandas as pd

# Download the webpage containing the data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data = requests.get(url).text

# Parse html data using BeautifulSoup
soup = BeautifulSoup(html_data, "html.parser")

# Extract GameStop Quarterly Revenue data into a pandas DataFrame
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for table in soup.find_all("table"):
    if "GameStop Quarterly Revenue" in table.text:
        for row in table.find("tbody").find_all("tr"):
            col = row.find_all("td")
            if len(col) >= 2:
                date = col[0].text.strip()
                revenue = col[1].text.strip()
                gme_revenue = pd.concat([gme_revenue, pd.DataFrame({"Date": [date], "Revenue": [revenue]})], ignore_index=True)

# Clean the Revenue column by removing dollar signs and commas, and drop empty rows
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace("$", "").str.replace(",", "")
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]

# Display the last five rows
print(gme_revenue.tail())
