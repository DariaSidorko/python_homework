
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://owasp.org/www-project-top-ten/")

items = driver.find_elements(By.XPATH, "//section//li/a")

results = []
for item in items:
    title = item.text
    link = item.get_attribute("href")
    results.append({"Title": title, "Link": link})

print(results)

df = pd.DataFrame(results)
df.to_csv("owasp_top_10.csv", index=False)

driver.quit()
