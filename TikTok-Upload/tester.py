from selenium import webdriver
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\webdrivers\geckodriver.exe")

driver.get("http://www.youtube.com")