headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;'
                  'q=0.9,image/webp,image/apng,*/*;'
                  'q=0.8,application/signed-exchange;v=b3;q=0.9',
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9",
"Origin": "https://www.weiq.com",
"Connection": "keep-alive",
"Referer":"https://www.weiq.com/owner/redbook/media.html",
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.97 Safari/537.36',
"Cookie" : "Hm_lvt_93deba7872e0b27eee3d1e5a437ceafe=1625658000; UM_distinctid=17a80c546be979-01f4acec058964-6373264-144000-17a80c546bfe10; PHPSESSID=97bj6tpve805g0dtvm3qk23023; wadmincode=97bj6tpve805g0dtvm3qk23023; _getmc=AAVeVwczUWJSY10xVWJUZwozAmEMOVNgV2I%3D; CNZZDATA1260733938=1831691067-1625654215-%7C1634558528"
}

import requests
from requests.sessions import RequestsCookieJar
import bs4
import json

redbook_url = "https://www.weiq.com/owner/redbook/mediaList.html"

setCookies = RequestsCookieJar()
setCookies.set('CNZZDATA1260733938','1831691067-1625654215-%7C1634558528',domain='www.weiq.com',path='/')
def get_work():
    data = {
        "plattype":"image_text",
        'page': 1,
    }
    url = 'https://www.weiq.com/owner/newweibo/mediauserNew.html'
    resp = requests.post(url=redbook_url,headers=headers,data=data)
    resp.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    target_json = soup.find('p').text
    target = json.loads(target_json)
    # print(target['data'])
    for item in range(0,10):
        print(target['data'][item]['account_name'],"平均阅读数为：",target['data'][item]['note_art_avg_read'])
get_work()