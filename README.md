# DJIA-Data-Scraping-and-Visualization

This project is aimed at scraping data from Wikipedia for tickers of all companies listed in the Dow Jones Industrial Average (US30) and retrieving their logos. The obtained tickers are utilized to download stock data and company information from Yahoo Finance. The collected data is then used to prepare interactive dashboards in Power BI.

## Features
- Scrapes tickers and logos of companies listed in the Dow Jones Industrial Average from Wikipedia.
- Utilizes obtained tickers to fetch stock data and company information from Yahoo Finance.
- Prepares interactive dashboards in Power BI using the collected data.

## Installation

### Prerequisites
- Python 3.x
- Power BI Desktop

## Instructions
1. Run the main script (data_downloader.py) to download historical data prices and company information. CSV files will be saved in the same folder where the Python script is located.
2. Updating Path in Power Query in Power BI
- Open the Power BI file (dashboard.pbix) using Power BI Desktop.
- Go to "Home" > "Transform Data" > "Data Source Settings".
- Update the file path in the data sources to match the location of the downloaded data on your local machine.
3. Refreshing Power BI
- Once the path is updated, refresh the data sources to reflect the latest changes.
- Click on "Home" > "Refresh" to update the data in your dashboard.

## Ideas for Upgrading the Project
1. **Implementing a Database/Data Warehouse:** Set up a database or data warehouse to efficiently store financial data scraped from various sources.
2. **Scheduling Downloads:** Use a scheduling tool to automate the execution of data scraping scripts at specific intervals. This ensures that the data is regularly updated without manual intervention.
3. **Including Fundamental Analysis Data:** Expand the scope of the project to include fundamental analysis data such as balance sheets, income statements, and cash flows. This will provide users with comprehensive insights into the financial health of the listed companies.
4. **Integrating Market News and Events:** Incorporate market news and events into the dashboard to provide users with context and insights into market trends and developments impacting the listed companies.

## License
This project is licensed under the MIT License.
