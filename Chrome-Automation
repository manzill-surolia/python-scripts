import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Set up Chrome WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver.exe is in PATH
driver.maximize_window()

# Open Google and search for "keyword"
driver.get("https://www.google.com")
time.sleep(2)  # Allow page to load

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("keyword")
search_box.send_keys(Keys.RETURN)
time.sleep(3)  # Wait for search results to load

# Extract the first search result title and URL
first_result = driver.find_element(By.CSS_SELECTOR, "h3").text
first_link = driver.find_element(By.CSS_SELECTOR, "h3").find_element(By.XPATH, "./ancestor::a").get_attribute("href")

# Copy result to clipboard
result_text = f"Title: {first_result}\nURL: {first_link}"
pyautogui.hotkey('ctrl', 'c')  # Copying is optional, directly use text

# Open Notepad
pyautogui.press('win')  # Open start menu
time.sleep(1)
pyautogui.write('Notepad')
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)  # Allow Notepad to open

# Paste the result in Notepad
pyautogui.write(result_text)
time.sleep(1)
pyautogui.hotkey('ctrl', 's')  # Save the file

# Save as 'keyword_result.txt'
time.sleep(1)
pyautogui.write("keyword_result.txt")
time.sleep(1)
pyautogui.press('enter')

# Close everything
time.sleep(2)
driver.quit()
