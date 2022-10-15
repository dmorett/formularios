import time
from turtle import bye
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\Users\\Dulce\\Documents\\WEBDRIVER\\chromedriver.exe")

driver.get("https://demoqa.com/text-box") 
driver.maximize_window()
time.sleep(1)
#driver.find_element(By.XPATH, '//button[text()="Some text"]')
nom=driver.find_element(By.XPATH, "//input[contains(@id,'userName')]")
nom.send_keys("jose")
time.sleep(1)
driver.find_element(By.XPATH, "//input[contains(@id,'userEmail')]" ).send_keys("osa1827@outlook.com")
time.sleep(1)
driver.find_element(By.XPATH, "//textarea[contains(@id,'currentAddress')]" ).send_keys("municippio libertador calle caasa")
time.sleep(1)
driver.find_element(By.XPATH, "//textarea[contains(@id,'permanentAddress')]").send_keys("apartamento libertado 40")
time.sleep(2)
driver.find_element(By.ID,"submit").click()
time.sleep(10)
driver.close()