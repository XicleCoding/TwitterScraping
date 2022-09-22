import csv
from getpass import getpass
from lib2to3.pgen2 import driver
from pickletools import optimize
from ssl import Options
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from msedge.selenium_tools import Edge, EdgeOptions

options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options)

#navigate in session to login screen
driver.get('https://twitter.com/login')
driver.maximize_window()
sleep(5)
username = driver.find_element_by_xpath('//input[@name="text"]')
username.send_keys('sirmorningwooderinos@gmail.com')
username.send_keys(Keys.RETURN)
sleep(3)

password = driver.find_element_by_xpath('//input[@name="password"]')
password.send_keys('masterthesis')
password.send_keys(Keys.RETURN)
sleep(3)

