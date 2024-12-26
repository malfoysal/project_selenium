from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
chrome_driver_path = r"chromedriver.exe"
chrome_options=Options()
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service = service, options = chrome_options)
driver.get("https://www.rcvacademy.com")
driver.maximize_window()
print(driver.title)
driver.close()