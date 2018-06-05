from bs4 import BeautifulSoup
import requests
import GetHtml
def baidu():
    url2="http://www.baidu.com/s?wd="+"凡人修仙传仙界"+"&pn=2"
    html_doc=requests.get(url2).content.decode("utf-8")
    soup=BeautifulSoup(html_doc,'html.parser')
    h3s=soup.find_all("h3",attrs={"class":"t"})
    print(h3s)
    for link in h3s:
        print(link.find('a').get('href'))

def detail(url):
    proxy = { "http": "http://122.114.31.177:808","https": "http://59.42.42.75:808" }
    s=requests.get(url,proxies=proxy)
    if s.status_code ==200:
        linkurl=s.url
        print(linkurl)
        html_doc=requests.get(linkurl,proxies=proxy).content.decode("GBK",'ignore').replace(u'\xa9', u'')
        soup=BeautifulSoup(html_doc,'html.parser')
        print(soup)
        last_time=soup.find('meta',attrs={"property":"og:novel:update_time"}).get('content')
        last_name=soup.find('meta',attrs={"property":"og:novel:latest_chapter_name"}).get('content')
        last_url=soup.find('meta',attrs={"property":"og:novel:latest_chapter_url"}).get('content')
        # print(soup)
        print(last_time,last_name,last_url)
        showText(last_url)
        urlList(soup)


def urlList(soup):
    urls=soup.find_all('dd')
    for url in urls:
        print(url.find('a').get('href'))

def showText(url):
    proxy = { "http": "http://119.28.152.208:80","https": "http://59.42.42.75:808" }
    html_doc=requests.get(url, proxies=proxy).content.decode("GBK",'ignore').replace(u'\xa9', u'')
    soup=BeautifulSoup(html_doc,'html.parser')
    print(soup.find('div','showtxt').get_text())
# baidu()
detail("http://www.baidu.com/link?url=N4qZfLnnFMa4X7hBuPzxpYjD_rBaynmJU5Z9v8obr0tUqqUfODrbesxL4gZaY_FV")
# detail("http://www.baidu.com/link?url=ikKN1T_QTBp40_rccu0f6FEnrk0VNdo4LqlE2XItIKKeUuDJuY5x-6qr4T0ZI2_9")
