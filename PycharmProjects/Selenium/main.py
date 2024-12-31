from selenium import webdriver

# Keep Chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")

# driver.close() # just closes the current tab
# driver.quit() # shutdown the entire browser
