import requests
import time
import random
import datetime as dt
import pandas as pd
import requests_html


# response = requests.get('http://datalytics.ru/')
# print(response.status_code)
# time.sleep(10)
#
# response.close()

def User_Agent(file_ua="headers_data/user_agents.xlsx"):

    random.seed()

    df = pd.read_excel(file_ua)
    df = df[df.Ok == 1]
    len_ = len(df)

    return df.iloc[random.randint(0, len_)]['User-Agents']

def Headers(host_, new_ua=User_Agent(), referrer_=""):

    def referrer(host_, referrer_):
        if not referrer_:
            return host_
        else:
            return referrer_

    def host(host_):
        return host_[host_.find("//")+2:]

    Headers = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8, application/signed-exchange;v=b3;q=0.9",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        'Cache-Control': "no-cache",
        'Connection': "keep-alive",
        'Cookie': "PHPSESSID=26dbd995196e60f814af12b39b5498ab; _ym_uid=1636034587926488240; _ym_d=1636034587; _ym_isad=2; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1",
        'Host': host(host_),
        'Pragma': "no-cache",
        'Referer': referrer(host_, referrer_),
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': new_ua
    }
    return Headers

print(dt.datetime.now())

session = requests_html.HTMLSession()
user_agent = User_Agent()
print(user_agent)
header = Headers('http://datalytics.ru')
response = session.get('http://datalytics.ru/all/golovolomka-pro-randomny-sempl/', headers=header)
response.html.render()
time.sleep(25)
print(response.status_code)
if response.status_code == 200:
    links = response.html.links
    go_page_url = list(links)[random.randint(0, len(links))]
    header = Headers('http://datalytics.ru', new_ua=user_agent, referrer_='http://datalytics.ru/all/golovolomka-pro-randomny-sempl/')
    response = session.get(go_page_url, headers=header)
    print(go_page_url)

time.sleep(18)

session.close()
