# McDonalds-Breakfast

📌 Project Overview

This project analyzes McDonald's Indonesia breakfast menu using data collected through web scraping from the official McDonald's Indonesia website. The analysis focuses on understanding the composition and structure of breakfast menu offerings, rather than the full McDonald's menu.
This project demonstrates an end-to-end Data Analyst workflow, from data collection to insight generation.

🌐 Data Source

Website: https://www.mcdonalds.co.id/menu#Sarapan%20Pagi

Data scope: Breakfast menu only (Sarapan Pagi)

The website does not provide downloadable datasets; therefore, data was collected programmatically using web scraping techniques.

🛠️ Data Collection (Web Scraping)

Data was collected automatically, not manually.
Web scraping was performed using Python, leveraging:
requests
BeautifulSoup

Collected attributes:

- product_name
- product_link
- image_url
- category

The scraped data was stored as a CSV file for further analysis.

🧹 Data Cleaning

The following cleaning steps were applied:

- Removed duplicate records
- Checked for missing values (no missing values found)
- Standardized column structure

Final dataset contains 134 breakfast menu items.

and more used;

Exploratory Data Analysis (EDA)
