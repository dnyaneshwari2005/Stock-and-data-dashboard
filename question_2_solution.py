import requests
from bs4 import BeautifulSoup
import pandas as pd

# Question 2: Use Webscraping to Extract Tesla Revenue Data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for table in soup.find_all("table"):
    if "Tesla Quarterly Revenue" in table.text:
        for row in table.find("tbody").find_all("tr"):
            col = row.find_all("td")
            if len(col) >= 2:
                date = col[0].text.strip()
                revenue = col[1].text.strip()
                tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame({"Date": [date], "Revenue": [revenue]})], ignore_index=True)

tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace("$", "").str.replace(",", "")
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

# Display the last five rows using tail()
print(tesla_revenue.tail())