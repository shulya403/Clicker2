from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import DriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.proxy import *
import requests
import random
import time
from datetime import datetime
import pandas as pd
from datetime import datetime as dt
import sys


class Clicker_simple(object):

    def __init__(self,
                 site,
                 counter=0,
                 #logfile="log.xlsx",
                 ip="мой домашний",
                 headless="y"):

        self.options = webdriver.ChromeOptions()

        if headless == "y":
            self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('disable-infobars')
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
                "title_is": "Бестселлеры ИТ-рынка. Аналитика российского рынка ИТ",
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
                "banner_list": ['byte_left_adv',
                                'itbs_right_adv',
                                'byte_center_adv',
                                'byte_top_adv'],
                "home_page": "HOME bytemag.ru",
                "title_is": "BYTE/Россия",
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

    def Proxie_try(self, site,
                   user_agent,
                   proxie_base="https://hidemy.name/ru/proxy-list/?country=BYKZLVRUUAUZ#list"
                   ):

        options = webdriver.ChromeOptions()
        #options.add_argument(user_agent)
        options.add_argument('--disable-gpu')
        # options.add_argument("--headless")

        if self.proxie_list_actual:
            pass
        else:
            try:
                driver_proxie_base = webdriver.Chrome(ChromeDriverManager().install(), options=options)
                driver_proxie_base.set_window_size(1920, 1080)
                driver_proxie_base.get(proxie_base)
                tbl_on_proxie_page = pd.read_html(driver_proxie_base.page_source)
                proxy_table = tbl_on_proxie_page[0]
                proxy_table = proxy_table[proxy_table['Тип'] != 'HTTP']
                print(proxy_table)
                for i, row in proxy_table.iterrows():
                    self.proxie_list_actual.append(row['Тип'].lower() + "://" + str(row['IP адрес']) + ":" + str(row['Порт']))


            except Exception as Err:
                print(Err)
                self.proxie_list_actual = []
                return ""

        while self.proxie_list_actual:
                this = random.randint(0, len(self.proxie_list_actual)-1)
                print("Проверка прокси: {}".format(self.proxie_list_actual[this]))
                self.options.add_argument("--proxy-server=%s" % self.proxie_list_actual[this])
                self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.options)
                if ("ios" in user_agent.lower()) or ("android" in user_agent.lower()):
                    self.driver.set_window_size(360, 720)
                else:
                    self.driver.set_window_size(1920, 1080)

                try:
                    self.driver.get(site)
                    wait = WebDriverWait(self.driver, 10).until(EC.title_contains(self.Sites[site]["title_is"]))
                    print("OK прокси ->", self.proxie_list_actual[this])
                    return self.proxie_list_actual[this]
                except Exception:
                    print("битый прокси", self.proxie_list_actual.pop(this))
                    print(len(self.proxie_list_actual))
                    self.driver.quit()

        return ""


    def banner_click(self, adv):
        
            try:        
                link_ = self.driver.find_element_by_name(adv)
                link_.location_once_scrolled_into_view
                time.sleep(2)
                webdriver.ActionChains(self.driver).move_to_element(link_).perform()
                link_.click()
            except Exception:
                pass
                
            if len(self.driver.window_handles) > 1:
                first_win = self.driver.window_handles[0]
                new_win = self.driver.window_handles[1]
                self.driver.switch_to.window(new_win)
                try:
                    wait = WebDriverWait(self.driver, 5). \
                        until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
    
                    adv_page_clicks = (int(random.expovariate(0.4)) + 1)

                    for i in range(adv_page_clicks):
                        try:
                            time.sleep(3)
                            list_link_adv = self.driver.find_elements_by_tag_name('a')
                            if list_link_adv:
                                try:
                                    link_adv = random.choice(list_link_adv[1:-1])
                                except IndexError:
                                    link_adv = list_link_adv[0]
                            else:
                                link_adv = ""
                            if link_adv:
                                link_adv.location_once_scrolled_into_view
                                time.sleep(1)
                                webdriver.ActionChains(self.driver).move_to_element(link_adv).perform()
                                link_adv.click()
                        except Exception:
                            pass
                except Exception:
                    pass
                self.driver.switch_to.window(first_win)
         

        #    self.random_link_click(random.randint(1, 7))

    def random_link_click(self, delay):

        time.sleep(random.randint(5, delay))
        
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
                    for j in list_links[0:list_links.index(link_):5]:
                        j.location_once_scrolled_into_view
                        ActionChains(self.driver).move_to_element(j).perform()
                        time.sleep(random.randint(0, 2))
                    link_.location_once_scrolled_into_view
                    ActionChains(self.driver).move_to_element(link_).perform()
                    link_.click()
                    print(self.counter, page_)
                    #self.Log(page_)
            except Exception as Err:
                print("Плохой линк -> ", Err)
    

    def click_random_3(self,
                       delay,
                       page="https://www.itbestsellers.ru/",
                       q=6, #макс число просмотров пользователе---
                       ban=100):

        if page == self.site:
            self.counter += 1
            #self.Log(self.site_home)
            print(self.counter, self.site_home)

        for i in range(int(random.expovariate(0.2))):

            banner = random.randint(0, ban)
            if banner <= len(self.banner_list) - 1:
                self.banner_click(self.banner_list[banner])
                #self.Log("BANNER click {}".format(self.banner_list[banner]))
                print(self.counter, "BANNER click {}".format(self.banner_list[banner]))

            self.counter += 1
            self.random_link_click(delay)
        time.sleep(random.randint(5, delay))

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
    site, debug, ip, Q, delay, deep, ban = "https://www.itbestsellers.ru/", "", "", 0, 0, 0, 0
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
        delay = 10
    if deep == 0:
        deep = 12
    if ban == 0:
        ban = 20
    

    go = Clicker_simple(site=site,
                        counter=counter_,
                        #logfile=log,
                        ip=ip,
                        headless=headless)


    if debug:
        lag = 1
    else:
        lag = 60

    for i in range(Q):

        delay_ = int(lag / delay_time_rel())
        time.sleep(delay_)

        #try:
        if delay_:
            # str_agent = '--user-agent="' + random.choice(go.user_agents) + '"'
            # print(str_agent)
            # user_agent = go.user_agents_base.iloc[random.randint(0, len(go.user_agents_base))]
            # str_agent = '--user-agent="' + user_agent + '"'
            # go.options.add_argument(str_agent)

            proxy = "" #go.Proxie_try(user_agent=user_agent, site=go.site)
            if proxy:
                #go.options.add_argument("--proxy-server=%s" % proxy)
                print("работаем под прокси:", proxy)
                #print(user_agent)

            else:
                print("работаем БЕЗ прокси:", dt.now())
                #print(str_agent)
                go.options = webdriver.ChromeOptions()
                #go.options.add_argument(str_agent)
                go.options.add_argument('--disable-gpu')
                go.driver = webdriver.Chrome(ChromeDriverManager().install(), options=go.options)
                # if ("ios" in user_agent.lower()) or ("android" in user_agent.lower()):
                #     go.driver.set_window_size(360, 720)
                #     print("MOBILE")
                # else:
                #     go.driver.set_window_size(1920, 1080)
                #     print("DESKTOP")
                go.driver.get(go.site)

        #except Exception as Err:
            #print("не вышло ->", Err)
            #self.driver.close()
        print(i, delay_)

        counter_ = go.click_random_3(page=site, delay=delay, ban=ban, q=deep)
        try:
            go.driver.quit()
        except Exception:
            pass


