# Importing libraries
from bs4 import BeautifulSoup
from lxml import etree
import requests
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

try:
    # Configuration
    root = 'https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average'
    result = requests.get(root)
    result.raise_for_status()  # Raise an error if request fails
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    dom = etree.HTML(str(soup))

    # Scrap all US30 ticker symbols
    tickers = dom.xpath('//table[@id="constituents"]//tr//td[2]//*/text()')

    # All US30 wiki sites
    websites = dom.xpath('//table[@id="constituents"]//tr//th//a[1]//@href')

    # Scrap each US30 logo
    company_logos = []
    for website in websites:
        url = f'https://en.wikipedia.org{website}'
        result = requests.get(url)
        result.raise_for_status()  # Raise an error if request fails
        content = result.text
        soup = BeautifulSoup(content, 'lxml')
        dom = etree.HTML(str(soup))
        try:
            # Handle IndexError when logo path is not found
            logo_path = dom.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[1]/td/span/a/img/@src')[0]
            company_logos.append('https:' + logo_path)
        except IndexError:
            logo_path = dom.xpath('//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[1]/td/span/a/img/@src')[0]
            company_logos.append('https:' + logo_path)

    # Lists to store company information
    address = []
    website = []
    industry = []
    sector = []
    longBusinessSummary = []
    marketCap = []
    fiftyTwoWeekLow = []
    fiftyTwoWeekHigh = []
    longName = []
    trailingPE = []
    forwardPE = []

    # Fetch company information for each ticker
    for ticker in tickers:
        ticker_info = yf.Ticker(ticker)
        address.append(", ".join([ticker_info.info.get('address1', ''),
                                   ticker_info.info.get('city', ''),
                                   ticker_info.info.get('state', ''),
                                   ticker_info.info.get('country', '')]))

        website.append(ticker_info.info.get('website', ''))
        industry.append(ticker_info.info.get('industry', ''))
        sector.append(ticker_info.info.get('sector', ''))
        longBusinessSummary.append(ticker_info.info.get('longBusinessSummary', ''))
        marketCap.append(ticker_info.info.get('marketCap', ''))
        fiftyTwoWeekLow.append(ticker_info.info.get('fiftyTwoWeekLow', ''))
        fiftyTwoWeekHigh.append(ticker_info.info.get('fiftyTwoWeekHigh', ''))
        longName.append(ticker_info.info.get('longName', ''))
        trailingPE.append(ticker_info.info.get('trailingPE', ''))
        forwardPE.append(ticker_info.info.get('forwardPE', ''))
        
    # Create DataFrame
    company_information = pd.DataFrame({
                                        'symbol': tickers,
                                        'address': address,
                                        'website': website,
                                        'industry': industry,
                                        'sector': sector,
                                        'longBusinessSummary': longBusinessSummary,
                                        'marketCap': marketCap,
                                        'fiftyTwoWeekLow': fiftyTwoWeekLow,
                                        'fiftyTwoWeekHigh': fiftyTwoWeekHigh,
                                        'longName': longName,
                                        'logo_url': company_logos,
                                        'trailingPE': trailingPE,
                                        'forwardPE': forwardPE})
    
    # Yesterday date
    yesterday = datetime.today() - timedelta(days=1)
    yesterday = yesterday.strftime('%Y-%m-%d')
    
    # Fetching price history
    price_history = pd.DataFrame()
    for ticker in tickers:
        df = yf.download(ticker, start="2010-01-01", end=yesterday)
        df['symbol'] = ticker
        price_history = pd.concat([price_history, df])
    
except requests.exceptions.RequestException as req_err:
    print(f'Request exception occurred: {req_err}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
    
# Saving to csv
company_information.to_csv('company_information.csv', index=False)
price_history.to_csv('price_history.csv', index=True)