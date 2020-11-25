# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# Указываем полный путь к geckodriver.exe на вашем ПК.
#driver = webdriver.Firefox(executable_path='C:\\temp\\geckodriver.exe')
driver = webdriver.Chrome(executable_path='C:\\temp\\chromedriver.exe')

driver.get("https://poloniex.com/login")
log = driver.find_element_by_name('username')
log.send_keys('pupkin@mail.ru')
time.sleep(2)
pas = driver.find_element_by_name('password')
pas.send_keys('pupkin@mail.ru')
time.sleep(2)
but = driver.find_elements_by_class_name('geetest_radar_tip')
but.click()

print(log, pas, but)
time.sleep(3)

driver.close()