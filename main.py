import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime as dat
from selenium.webdriver.common.keys import Keys
import time


URL = 'http://ec2-54-203-118-10.us-west-2.compute.amazonaws.com/now/'
#URL = 'https://google.com'
try:

    response_code = requests.get(URL).status_code
    if response_code==200:
            print("the " +URL+ " is  OK and working with status code " + str(response_code))
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
                print("The clock of the server and the python machine is in sync")
                print("the python time is " + current_time)
                print("the server time is " + results)
            else:
                print("The clock of the server and the python machine is NOT in sync")
                print("the python machine time is " + current_time)
                print("the server time is " + results)
            driver.close()
    else:
         print("the " +URL+ " is NOT OK as it is responding with status " +str(response_code) )
except requests.ConnectionError as c:
    print("The URL is not responding it is NOT OKAY  ....   " + str(c))
except AttributeError as a:
    print("the URL " +URL+ "  is not intended to be used for the script ")