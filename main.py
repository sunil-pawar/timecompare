import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime as dat
from selenium.webdriver.common.keys import Keys
import time


URL = 'http://ec2-54-184-81-169.us-west-2.compute.amazonaws.com/now/'
driver = webdriver.Chrome('./chromedriver')
driver.get(URL)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
results = soup.p.string
localtime = dat.datetime.now()
current_time = localtime.strftime("%H:%M:%S")
py_time = dat.datetime.strptime(current_time,"%H:%M:%S")
server_time = dat.datetime.strptime(results,"%H:%M:%S")
if py_time == server_time:
    print("both the server time and browser time macthes")
else:
    print("the server time and local time doesnt macth")

print("the browser time is " + current_time)
print("the server time is " + results)
driver.close()



