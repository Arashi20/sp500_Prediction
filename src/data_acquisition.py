
import yfinance as yf
import pandas as pd
import os

#Using yfinance to download long-term S&P 500 data from Yahoo Finance and save it to a CSV file. I will download 
#the dat from the past 50 years as it contains multiple bull and bear markets.
#This will help us to train the model on different market conditions.


def download_sp500_data(start_date="1970-01-01", end_date="2025-01-01", save_path="data/sp500.csv"):
    """
    Downloads long-term S&P 500 historical data from Yahoo Finance and saves it to a CSV file.
    """
    print("[INFO] Downloading long-term S&P 500 data from Yahoo Finance...")

    ticker = "^GSPC"
    sp500_data = yf.download(ticker, start=start_date, end=end_date)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    sp500_data.to_csv(save_path)

    print(f"[SUCCESS] Long-term data saved to {save_path}")
