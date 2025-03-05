import requests
from bs4 import BeautifulSoup
import pandas as pd

# Example URL (modify as needed)
url = "https://www.bizbuysell.com"

# Send request and parse the page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Example: Extract business names
businesses = soup.find_all("h2", class_="business-title")  # Modify selector based on actual HTML structure

data = []
for biz in businesses:
    name = biz.text.strip()
    data.append({"Business Name": name})

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("smb_listings.csv", index=False)
print("Scraping complete. Data saved to smb_listings.csv")
