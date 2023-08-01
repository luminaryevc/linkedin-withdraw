#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:52:51 2023

@author: shahadsami
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# This instance will be used to log into LinkedIn

# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")

# waiting for the page to load
time.sleep(5)

# entering username
username = driver.find_element(By.ID, "username")

# In case of an error, try changing the element
# tag used here.

# Enter Your Email Address
username.send_keys('shahad_samii@hotmail.com')

# entering password
pword = driver.find_element(By.ID,"password")
# In case of an error, try changing the element
# tag used here.

# Enter Your Password
pword.send_keys("shahad563")	

# Clicking on the log in button
# Format (syntax) of writing XPath -->
# //tagname[@attribute='value']
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.

# Click the "Message" button 
driver.find_element(By.XPATH, "/html/body/div[5]/header/div/nav/ul/li[2]/a/span").click()
time.sleep(5)

driver.get('https://www.linkedin.com/mynetwork/invitation-manager/')
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/section/div[1]/div/button[2]").click()
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/section/div[2]/ul/li/div/div[2]/button/span").click()
time.sleep(5)
# Close the browser
driver.quit()