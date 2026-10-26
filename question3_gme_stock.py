import yfinance as yf
import pandas as pd

# Extract GameStop Stock Data
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")

# Reset the index and display the first five rows
gme_data.reset_index(inplace=True)
print(gme_data.head())
