import matplotlib.pyplot as plt
import pandas as pd

def make_graph(stock_data, revenue_data, stock):
    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    axes[0].plot(pd.to_datetime(stock_data['Date']), stock_data['Close'], color='blue', label='Stock Price')
    axes[0].set_title(f"{stock} Stock Price")
    axes[0].set_ylabel("Price ($)")
    axes[0].grid(True)
    
    axes[1].plot(pd.to_datetime(revenue_data['Date']), revenue_data['Revenue'].astype(float), color='orange', marker='o', label='Revenue')
    axes[1].set_title(f"{stock} Revenue")
    axes[1].set_ylabel("Revenue (Millions USD)")
    axes[1].set_xlabel("Date")
    axes[1].grid(True)
    plt.tight_layout()
    plt.show()

# Call the function for Tesla with a title/graph
make_graph(tesla_data, tesla_revenue, 'Tesla')
