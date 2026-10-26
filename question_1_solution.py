import yfinance as yf
import pandas as pd

# Question 1: Use yfinance to Extract Tesla Stock Data
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")

# Reset the index, save, and display the first five rows using head()
tesla_data.reset_index(inplace=True)
print(tesla_data.head())
```ef

I have generated the Python file for Question 1. You can run this code in your Jupyter Notebook or Python environment to execute the extraction and display the first five rows of the `tesla_data` DataFrame for your screenshot.