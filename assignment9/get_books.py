
# Task 2: Understanding HTML and the DOM for the Durham Library Site

# cp-search-result-item

# cp-title-link

# cp-author-link

# cp-format-info + cp-format



# Task 3: Write a Program to Extract this Data

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
import time
import os



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

results = []
books = driver.find_elements(By.CLASS_NAME, "cp-search-result-item")

for book in books:
    try:
        title = book.find_element(By.CLASS_NAME, "cp-title-link").text
    except:
        title = "N/A"

    try:
        authors = book.find_elements(By.CLASS_NAME, "cp-author-link")
        author_texts = [a.text for a in authors]
        author = "; ".join(author_texts)
    except:
        author = "N/A"

    try:
        format_div = book.find_element(By.CLASS_NAME, "cp-format-info")
        format_year = format_div.find_element(By.CLASS_NAME, "cp-format").text
    except:
        format_year = "N/A"

    results.append({
        "Title": title,
        "Author": author,
        "Format-Year": format_year
    })

df = pd.DataFrame(results)
print(df)


df.to_csv("get_books.csv", index=False)
with open("get_books.json", "w") as f:
    json.dump(results, f, indent=2)

driver.quit()