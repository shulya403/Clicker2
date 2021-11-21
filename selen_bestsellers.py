from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import DriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.proxy import *
import requests
import random
import time
from datetime import datetime
import pandas as pd
from datetime import datetime as dt
import sys

class Clicker(object):

    def __init__(self):

        #proxy_ = "93.171.164.251:8080"
        proxy_ = [
            "109.248.249.33:8081",
            "178.49.188.53:8080",
            "91.217.42.2:8080",
            "79.120.3.122:80",
            "176.32.185.22:8080"
            # "139.180.165.197:3128",
            # "169.57.1.84:8123",
            # "163.172.168.124:3128",
            # "35.169.156.54:3128",
            # "169.57.1.84:25",
            # "169.57.1.85:25",
            # "173.192.128.238:25"
        ]
        
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.5; rv:90.0) Gecko/20100101 Firefox/90.0",
            "Mozilla/5.0 (X11; Linux i686; rv:90.0) Gecko/20100101 Firefox/90.0",
            "Mozilla/5.0 (Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
            "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:90.0) Gecko/20100101 Firefox/90.0",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
            "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.5; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Mozilla/5.0 (Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; Trident/4.0;)",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)",
            "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.0)",
            "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2)",
            "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 6.2; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.112",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.112",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.112",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.112",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Vivaldi/4.1",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Vivaldi/4.1",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Vivaldi/4.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Vivaldi/4.1",
            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Vivaldi/4.1",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 YaBrowser/21.6.0 Yowser/2.5 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 YaBrowser/21.6.0 Yowser/2.5 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 YaBrowser/21.6.0 Yowser/2.5 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/92.0.4515.90 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (iPad; CPU OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/92.0.4515.90 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (iPod; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/92.0.4515.90 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 11_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/35.0 Mobile/15E148 Safari/605.1.15",
            "Mozilla/5.0 (iPad; CPU OS 11_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/35.0 Mobile/15E148 Safari/605.1.15",
            "Mozilla/5.0 (iPod touch; CPU iPhone OS 11_5_1 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) FxiOS/35.0 Mobile/15E148 Safari/605.1.15",
            "Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
            "Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/90.0",
            "Mozilla/5.0 (Android 11; Mobile; LG-M255; rv:90.0) Gecko/90.0 Firefox/90.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (iPad; CPU OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (iPod touch; CPU iPhone 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 EdgA/46.6.4.5160",
            "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 EdgA/46.6.4.5160",
            "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 EdgA/46.6.4.5160",
            "Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 EdgA/46.6.4.5160",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 EdgiOS/46.3.13 Mobile/15E148 Safari/605.1.15",
            "Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 Edge/40.15254.603",
            "Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 OPR/63.3.3216.58675",
            "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 OPR/63.3.3216.58675",
            "Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 OPR/63.3.3216.58675",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 YaBrowser/21.6.3.883 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (iPad; CPU OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 YaBrowser/21.6.3.883 Mobile/15E148 Safari/605.1",
            "Mozilla/5.0 (iPod touch; CPU iPhone 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 YaBrowser/21.6.3.883 Mobile/15E148 Safari/605.1",
            "Mozilla/5.0 (Linux; arm_64; Android 11; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 YaBrowser/21.3.4.59 Mobile Safari/537.36"
            ]

        for i in range(len(user_agents)):
            options = webdriver.ChromeOptions()
            # options.add_argument('--headless')
            #options.add_argument('--user-agent=%s' % use,1080")
            #options.add_argument('--proxy-server=%s' % proxy_[i])

            try:
                self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
                self.driver.get("https://www.itbestsellers.ru/")
                # site = self.driver.find_element_by_tag_name("title").text
                # print("site:", site)
                # print(EC.presence_of_element_located((By.TAG_NAME, "title")))
                self.element = WebDriverWait(self.driver, 1).\
                    until(EC.presence_of_element_located((By.NAME, "itbs_top_adv")))
                #self.element.click()
                #self.driver.get("https://yandex.ru/internet/")
                # self.element = WebDriverWait(self.driver, 1).\
                #     until(EC.presence_of_element_located((By.CLASS_NAME, "parameter-header__title")))
                if self.element:
                    print("Сработал: ", proxy_[i])

            except Exception:
                try:
                    response = requests.get("https://yandex.ru/internet/",
                                            proxies={"https": proxy_[i]})
                    print(response.status_code, proxy_[i])
                except requests.exceptions.ProxyError:
                    print("Requests none", proxy_[i])

class Clicker_simple(object):
    
    

    def __init__(self,
                 site,
                 counter=0,
                 logfile="log.xlsx",
                 ip="мой домашний",
                 headless="y"):
        # self.user_agents = [
        #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        #     "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        #     "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        #     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.5; rv:90.0) Gecko/20100101 Firefox/90.0",
        #     "Mozilla/5.0 (X11; Linux i686; rv:90.0) Gecko/20100101 Firefox/90.0",
        #     "Mozilla/5.0 (Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
        #     "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:90.0) Gecko/20100101 Firefox/90.0",
        #     "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
        #     "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
        #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
        #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.5; rv:78.0) Gecko/20100101 Firefox/78.0",
        #     "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
        #     "Mozilla/5.0 (Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
        #     "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
        #     "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
        #     "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
        #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
        #     "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)",
        #     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; Trident/4.0;)",
        #     "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)",
        #     "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.0)",
        #     "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
        #     "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
        #     "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2)",
        #     "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
        #     "Mozilla/5.0 (Windows NT 6.2; Trident/7.0; rv:11.0) like Gecko",
        #     "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
        #     "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko",
        #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67",
        #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67",
        #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.112",
        #     "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.112",
        #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.112",
        #     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.112",
        #     "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Vivaldi/4.1",
        #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Vivaldi/4.1",
        #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Vivaldi/4.1",
        #     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Vivaldi/4.1",
        #     "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Vivaldi/4.1",
        #     "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 YaBrowser/21.6.0 Yowser/2.5 Safari/537.36",
        #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 YaBrowser/21.6.0 Yowser/2.5 Safari/537.36",
        #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 YaBrowser/21.6.0 Yowser/2.5 Safari/537.36",
        #     "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/92.0.4515.90 Mobile/15E148 Safari/604.1",
        #     "Mozilla/5.0 (iPad; CPU OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/92.0.4515.90 Mobile/15E148 Safari/604.1",
        #     "Mozilla/5.0 (iPod; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/92.0.4515.90 Mobile/15E148 Safari/604.1",
        #     "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        #     "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        #     "Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        #     "Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        #     "Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        #     "Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        #     "Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        #     "Mozilla/5.0 (iPhone; CPU iPhone OS 11_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/35.0 Mobile/15E148 Safari/605.1.15",
        #     "Mozilla/5.0 (iPad; CPU OS 11_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/35.0 Mobile/15E148 Safari/605.1.15",
        #     "Mozilla/5.0 (iPod touch; CPU iPhone OS 11_5_1 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) FxiOS/35.0 Mobile/15E148 Safari/605.1.15",
        #     "Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        #     "Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/90.0",
        #     "Mozilla/5.0 (Android 11; Mobile; LG-M255; rv:90.0) Gecko/90.0 Firefox/90.0",
        #     "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
        #     "Mozilla/5.0 (iPad; CPU OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
        #     "Mozilla/5.0 (iPod touch; CPU iPhone 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
        #     "Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 EdgA/46.6.4.5160",
        #     "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 EdgA/46.6.4.5160",
        #     "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 EdgA/46.6.4.5160",
        #     "Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 EdgA/46.6.4.5160",
        #     "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 EdgiOS/46.3.13 Mobile/15E148 Safari/605.1.15",
        #     "Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 Edge/40.15254.603",
        #     "Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 OPR/63.3.3216.58675",
        #     "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 OPR/63.3.3216.58675",
        #     "Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 OPR/63.3.3216.58675",
        #     "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 YaBrowser/21.6.3.883 Mobile/15E148 Safari/604.1",
        #     "Mozilla/5.0 (iPad; CPU OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 YaBrowser/21.6.3.883 Mobile/15E148 Safari/605.1",
        #     "Mozilla/5.0 (iPod touch; CPU iPhone 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 YaBrowser/21.6.3.883 Mobile/15E148 Safari/605.1",
        #     "Mozilla/5.0 (Linux; arm_64; Android 11; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 YaBrowser/21.3.4.59 Mobile Safari/537.36"
        #     ]

        self.options = webdriver.ChromeOptions()

        if headless == "y":
            self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        #self.options.add_argument("--window-size=1920,1080")
        # self.options.add_argument('--proxy-server=%s' % proxy_[i])
        self.user_agents_base = pd.read_excel("headers_data/user_agents.xlsx")
        self.user_agents_base = self.user_agents_base[self.user_agents_base['Ok'] == 1]['User-Agents']
        self.proxie_list_actual = []

        # try:
        #     self.logfile = logfile
        #     self.df = pd.read_excel(self.logfile, index_col=0)
        #     if not self.df.empty:
        #         self.df_counter = len(self.df)
        #     else:
        #         self.df_counter = 0
        # except Exception as Err:
        #     print(Err)
        #     self.df = pd.DataFrame(columns=['Time', 'Page', 'ip'])
        #     self.df_counter = 0

        self.counter = counter
        self.ip = ip

        self.Sites = {
            "https://www.itbestsellers.ru/": {
                "banner_list": [
                    "itbs_top_adv",
                    "itbs_right_adv",
                    "itbs_center_adv",
                    "itbs_left_adv"
                ],
                "home_page": "HOME itbestsellers.ru",
                "exclude": [
                    "Номера",
                    "Форумы",
                    "Об издании",
                    "студия iMake",
                    "RSS",
                    "Подписка на рассылки",
                    "Авторизация",
                    "bestsellers@itbestsellers.ru",
                    "",
                    "Создание сайта",
                    "Подписка на издание"
                    ]
        },
            "https://www.bytemag.ru/": {
                'banner_list': ['byte_left_adv',
                                'itbs_right_adv',
                                'byte_center_adv',
                                'byte_top_adv'],
                'home_page': "HOME bytemag.ru",
                "exclude": [
                    "byte@bytemag.ru",
                    "Корпоративная подписка",
                    "Поместить в блог",
                    "",
                    "RSS",
                    "ITRN",
                    "CRN/RE"
                ]
            },
            "https://allgid.ru/" : {
                'banner_list': [],
                'home_page': "HOME allgid.ru",
                "exclude": [
                    "expert@itresearch.ru"
                    ]
                    
                }
        }

        self.site = site
        if "exclude" in self.Sites[self.site]:
            self.site_exclude = self.Sites[self.site]["exclude"]
        else:
            self.site_exclude = []
        self.banner_list = self.Sites[self.site]["banner_list"]
        self.site_home = self.Sites[self.site]["home_page"]

    def Proxie_try(self,
                   user_agent='--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"',
                   proxie_base="https://hidemy.name/ru/proxy-list/?country=BYKZLVRUUAUZ#list"):

        options = webdriver.ChromeOptions()
        #options.add_argument(user_agent)
        options.add_argument('--disable-gpu')
        # options.add_argument("--headless")

        if self.proxie_list_actual:
            pass
        else:
            try:
                driver_proxie_base = webdriver.Chrome(ChromeDriverManager().install(), options=options)
                driver_proxie_base.get(proxie_base)
                tbl_on_proxie_page = pd.read_html(driver_proxie_base.page_source)
                proxy_table = tbl_on_proxie_page[0]
                # proxy_table = proxy_table[proxy_table['Тип'] == 'HTTPS']

                for i, row in proxy_table.iterrows():
                    self.proxie_list_actual.append(row['Тип'].lower() + "://" + str(row['IP адрес']) + ":" + str(row['Порт']))

            except Exception as Err:
                print(Err)
                self.proxie_list_actual = []
                return ""

        while self.proxie_list_actual:
                this = random.randint(0, len(self.proxie_list_actual))
                print("Проверка прокси: {}".format(self.proxie_list_actual[this]))
                options.add_argument("--proxy-server=%s" % self.proxie_list_actual[this])
                driver_proxie_base = webdriver.Chrome(ChromeDriverManager().install(), options=options)
                try:
                    driver_proxie_base.get("https://allgid.ru/rate/")
                    wait = WebDriverWait(driver_proxie_base, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                    return self.proxie_list_actual[this]
                except Exception:
                    print("битый прокси", self.proxie_list_actual.pop(this))

        return ""


    def banner_click(self, adv):
        
            try:        
                link_ = self.driver.find_element_by_name(adv)
                link_.click()
            except Exception:
                pass
                
            if len(self.driver.window_handles) > 1:
                first_win = self.driver.window_handles[0]
                new_win = self.driver.window_handles[1]
                self.driver.switch_to.window(new_win)
                wait = WebDriverWait(self.driver, 5). \
                    until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
    
                adv_page_clicks = (int(random.expovariate(1.1)))
    
                for i in range(adv_page_clicks):
                    try:
                        link_adv = self.driver.find_element_by_tag_name('a')
                        link_adv.click()
                    except Exception:
                        pass
                self.driver.switch_to.window(first_win)
         

        #    self.random_link_click(random.randint(1, 7))

    def random_link_click(self, delay):

        time.sleep(delay)
        
        try:

            list_links = self.driver.find_elements_by_tag_name('a')


        except Exception:
            list_links = list()
        
        if list_links:

            link_ = random.choice(list_links)
            #print(link_.text)
            try:
                page_ = link_.text
                if page_ and (page_ not in self.site_exclude):
                    link_.click()
                    print(self.counter, page_)
                    #self.Log(page_)
            except:
                print("Плохой линк")
    

    def click_random_3(self,
                       delay,
                       page="https://www.itbestsellers.ru/",
                       q=6, #макс число просмотров пользователе-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------м
                       ban=100):

        if page == self.site:
            self.counter += 1
            #self.Log(self.site_home)
            print(self.counter, self.site_home)

        for i in range(int(random.expovariate(0.4))):

            banner = random.randint(0, ban)
            if banner <= len(self.banner_list) - 1:
                self.banner_click(self.banner_list[banner])
                #self.Log("BANNER click {}".format(self.banner_list[banner]))
                print(self.counter, "BANNER click {}".format(self.banner_list[banner]))

            self.counter += 1
            self.random_link_click(delay)

        return self.counter

    def Log(self, text_):

        counter_ = self.df_counter + self.counter
        self.df.loc[counter_, 'Page'] = text_
        self.df.loc[counter_, 'Time'] = datetime.now()
        self.df.loc[counter_, 'ip'] = self.ip
        # try:
        #     myip = requests.get("https://ramziv.com/ip").text
        #     if myip:
        #         self.df.loc[counter_, 'ip'] = myip
        # except Exception:
        #     print("Глюк ramiz")
        #     pass
        if ((counter_ % 10) == 0):
            try:
                self.df.to_excel(self.logfile)
            except Exception:
                print("что-то с файлом")
                pass


def delay_time_rel():
    hur = int(dt.now().hour)
    if dt.now().weekday() >= 5:
        day = 0.5
        
    else:
        day = 1
    if 0 <= hur < 3:
        return 1
    elif 3 <= hur < 6:
        return 0.5
    elif 6 <= hur < 7:
        return 2*day
    elif 7 <= hur < 9:
        return 4*day
    elif 9 <= hur < 11:
        return 12*day
    elif 11 <= hur < 13:
        return 16*day
    elif 13 <= hur < 17:
        return 20*day
    elif 17 <= hur < 19:
        return 18*day
    elif 19 <= hur < 21:
        return 12*day
    elif 21 <= hur <= 22:
        return 6*day
    else:
        return 3*day


if __name__ == '__main__':

    counter_ = 0
    random.seed()

    #print(sys.argv)
    site, debug, ip, Q, delay, deep, ban, log = "https://www.itbestsellers.ru/", "", "", 0, 0, 0, 0, "log.xlsx"
    headless = "n"
    for sysarg in sys.argv[1:]:
        if "-site" in sysarg:
            st = str(sysarg.replace("-site=", ""))
            if "by" in st:
                site = "https://www.bytemag.ru/"
            elif "al" in st:
                site = "https://allgid.ru/"
        if "-debug" in sysarg:
            debug = "n"
        if "-ip" in sysarg:
            ip = str(sysarg.replace("-ip=", ""))
        elif "-q" in sysarg:
            Q = int(sysarg.replace("-q=", ""))
        elif "-del" in sysarg:
            delay = int(sysarg.replace("-del=", ""))
        elif "-deep" in sysarg:
            deep = int(sysarg.replace("-deep=", ""))
        elif "-ban" in sysarg:
            ban = int(sysarg.replace("-ban=", ""))
        elif "-headless" in sysarg:
            headless="y"
        elif "-log" in sysarg:
            log = str(sysarg.replace("-log=", ""))
            if not ".xlsx" in log:
                log += ".xlsx"

    if ip == "":
        ip = "дом_dsh"
    if Q == 0:
        Q = 500
    if delay == 0:
        delay = 3
    if deep == 0:
        deep = 6
    if ban == 0:
        ban = 100
    

    go = Clicker_simple(site=site,
                        counter=counter_,
                        logfile=log,
                        ip=ip,
                        headless=headless)


    if debug:
        lag = 1
    else:
        lag = 60

    for i in range(Q):

        delay_ = int(lag / delay_time_rel())
        time.sleep(delay_)

        try:
            # str_agent = '--user-agent="' + random.choice(go.user_agents) + '"'
            # print(str_agent)
            user_agent = go.user_agents_base.iloc[random.randint(0, len(go.user_agents_base))]
            str_agent = '--user-agent="' + user_agent + '"'
            print(str_agent)
            go.options.add_argument(str_agent)

            proxy = go.Proxie_try()
            if proxy:
                go.options.add_argument("--proxy-server=%s" % proxy)
                print(proxy)


            go.driver = webdriver.Chrome(ChromeDriverManager().install(), options=go.options)
            if ("Windows" in str_agent) or ("Macintosh" in str_agent) or ("Linux" in str_agent):
                print("DESKTOP")
                go.driver.set_window_size(1920,1080)
            else:
                print("MOBILE")
                go.driver.set_window_size(360,720)
            go.driver.get(go.site)
        except Exception:
            print("не вышло")
            #self.driver.close()
        print(i, delay_)

        counter_ = go.click_random_3(page=site, delay=delay, ban=ban)
        try:
            go.driver.quit()
        except Exception:
            pass


