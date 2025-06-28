


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


# Set up Selenium driver
driver = webdriver.Chrome()
driver.get("https://www.baseball-almanac.com/yearmenu.shtml")
time.sleep(2) 

# Scrape all year links from the main menu
results = []

#Get all link elements inside the table rows
links = driver.find_elements(By.XPATH, '//table//a')

for link in links:
    try:
        year_text = link.text.strip()
        year_url = link.get_attribute('href')
        if year_text.isdigit():  # Only include numeric year entries
            results.append({"Year": year_text, "URL": year_url})
    except Exception as e:
        print("Error extracting a link:", e)



# Close the browser
driver.quit()

# Convert to DataFrame and save
df = pd.DataFrame(results)
df.to_csv("year_links.csv", index=False)
print(df)

