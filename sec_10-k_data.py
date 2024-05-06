from sec_edgar_downloader import Downloader
import os


output_directory = "sec-edgar-filings"

email = "archishmanvb27@gmail.com.com"


os.makedirs(output_directory, exist_ok=True)


dl = Downloader(output_directory, email)

# List of company tickers
companies = ["AAPL", "NVDA", "AMZN"]

# Download 10-K filings for each company from 1995 to 2023
for company in companies:
    # The range is from 1995-2023
    for year in range(1995, 2024):
        print(f"Downloading 10-K for {company} for the year {year}")
        dl.get("10-K", company, after=f"{year}-01-01", before=f"{year}-12-31")

print("Download complete.")
