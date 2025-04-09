import requests
url = "https://example.com"
response = requests.get(url)
print(response.status_code)

import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
print(response.status_code)  # Should print 200 if the request is successful

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())  # View the formatted HTML structure

headlines = soup.find_all("h2")  # Extracts all h2 elements
for headline in headlines:
    print(headline.text)

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver
browser = webdriver.Chrome()
browser.get("https://example.com")

# Extract dynamic content
elements = browser.find_elements(By.TAG_NAME, "h2")
for el in elements:
    print(el.text)

browser.quit()