from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8000")

cards = driver.find_elements(By.CLASS_NAME, "card")

assert len(cards) == 2

print("Teste dos cards aprovado!")

driver.quit()