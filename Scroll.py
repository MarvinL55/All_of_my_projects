from selenium import webdriver
import time

# Set up Chrome driver
options = webdriver.ChromeOptions()
options.page_load_timeout = 120
options.script_timeout = 120

driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
driver = webdriver.Chrome(options=options)

# Define scroll function
def scroll_down():
    # Get current page height
    current_height = driver.execute_script("return document.body.scrollHeight")

    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for new content to load
    time.sleep(2)

    # Check if page height has changed
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height != current_height:
        scroll_down()

# Scroll down the page
scroll_down()


