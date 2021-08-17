import schedule
import requests
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from slacker import Slacker
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:/Users/황길연/Desktop/html/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
driver.get('https://www.binance.com/en/futures/SOLUSDT')
token = "xoxb-2409343342448-2385969245523-lAIzZ4ycBWXXZfHZtr2nPZ6E"
slack = Slacker(token)

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
myToken = "xoxb-2409343342448-2385969245523-lAIzZ4ycBWXXZfHZtr2nPZ6E"

def job():
    count = 0
    count2 = 0
    macd = driver.find_element_by_xpath('//*[@id="__APP"]/div/div[3]/div/div/div[3]/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[4]/div/div[2]/span[4]').text
    ma20 = driver.find_element_by_xpath('//*[@id="__APP"]/div/div[3]/div/div/div[3]/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/span[2]').text
    ma60 = driver.find_element_by_xpath('//*[@id="__APP"]/div/div[3]/div/div/div[3]/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/span[4]').text
    ma120 = driver.find_element_by_xpath('//*[@id="__APP"]/div/div[3]/div/div/div[3]/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/span[6]').text
    k = driver.find_element_by_xpath('//*[@id="__APP"]/div/div[3]/div/div/div[3]/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[3]/div/div[2]/span[3]').text
    d = driver.find_element_by_xpath('//*[@id="__APP"]/div/div[3]/div/div/div[3]/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[3]/div/div[2]/span[5]').text
    j = driver.find_element_by_xpath('//*[@id="__APP"]/div/div[3]/div/div/div[3]/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[3]/div/div[2]/span[7]').text
    if float(ma20) < float(ma60) < float(ma120):
      if float(macd) < 0:
        if float(j) < float(k) < float(d):
          count += 1
          post_message(myToken,"#5","숏")
      else:
        count2 += 1
        
    elif float(ma120) < float(ma60) < float(ma20):
      if float(macd) > 0:
        if float(d) < float(k) < float(j):
          count += 1
          post_message(myToken,"#5","롱")
      else:
        count2 += 1

schedule.every(1).minutes.do(job)
while True:
  schedule.run_pending()
  time.sleep(1)