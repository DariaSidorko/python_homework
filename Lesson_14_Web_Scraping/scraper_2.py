
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Set up Chrome options
options = Options()
options.add_argument("--headless")  
options.add_argument("--disable-gpu")
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0")

# Create driver
driver = webdriver.Chrome()

# Target URL
url = "https://www.baseball-almanac.com/players/Oldest_Living_Baseball_Players.php"
driver.get(url)
time.sleep(3)

# Locate the table
table = driver.find_element(By.XPATH, "//table[contains(@class, 'boxed')]")
rows = table.find_elements(By.TAG_NAME, "tr")

# Skip header
data = []
for row in rows[1:]:
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) < 7:
        continue

    try:
        rank = cols[0].text.strip()
        name_elem = cols[1].find_element(By.TAG_NAME, "a")
        name = name_elem.text.strip()
        profile_link = name_elem.get_attribute("href")
    except:
        name = cols[1].text.strip()
        profile_link = "N/A"

    birth_date = cols[2].text.strip()
    age = cols[3].text.strip()
    debut = cols[4].text.strip()
    final_game = cols[5].text.strip()
    team = cols[6].text.strip()

    data.append({
        "Rank": rank,
        "Name": name,
        "Birth Date": birth_date,
        "Age": age,
        "Debut": debut,
        "Final Game": final_game,
        "Team": team,
        "Profile Link": profile_link
    })

driver.quit()

# Save to CSV or view
df = pd.DataFrame(data)
df.to_csv("oldest_living_players.csv", index=False)
print(df.head(10))



