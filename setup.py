import pandas as pd
from pathlib import Path
import glob

def process_csv(path):
    ticker = Path(path).stem
    df = pd.read_csv(path, parse_dates=['Date'])
    df.insert(0, 'stock symbol', ticker)
    return df

# process all csv files and combine into one dataframe
csv_files = glob.glob("data/*.csv")
stock_price_list = [process_csv(file) for file in csv_files]
stock_prices = pd.concat(stock_price_list, ignore_index=True)
stock_prices.to_csv('big_tech_stock_prices.csv', index=False)

# create df for stock symbols and company name
company_symbols = pd.DataFrame({'stock_symbol': ["AAPL", "ADBE", "AMZN", "CRM", "CSCO", "GOOGL", "IBM", "INTC", "META", "MSFT", "NFLX", "NVDA", "ORCL", "TSLA"], 
                                'company': ["Apple Inc.", "Adobe Inc.", "Amazon.com, Inc.", "Salesforce, Inc.", "Cisco Systems, Inc.", "Alphabet Inc.", "International Business Machines Corporation", "Intel Corporation", "Meta Platforms, Inc.", "Microsoft Corporation", "Netflix, Inc.", "NVIDIA Corporation", "Oracle Corporation", "Tesla, Inc."]
                                })
company_symbols.to_csv('big_tech_companies.csv', index=False)
