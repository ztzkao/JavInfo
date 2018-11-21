import requests
from bs4 import BeautifulSoup

search_key = 'ddt-551'
res=requests.get('http://www.dmm.co.jp/search/=/searchstr=' + search_key + '/analyze=V1EBAVcHUQA_/limit=30/n1=FgRCTw9VBA4GAVhfWkIHWw__/sort=ranking/')
Result = {
    "result": "FAIL",
    "title": "",
    "number": "",
    "date": "",
    "avers": "",
    "video_long": "",
    "maker": "",
    "seller": "",
    "company": "",
    "img": "",
    "have": "",
}
if res.status_code == requests.codes.ok:
            html = res.content
            soup = BeautifulSoup(html, 'html.parser')
            href = soup.find('p', attrs={'class': 'tmb'}).find('a').get("href")
            print(href)
            res = requests.get(href)
            if res.status_code == requests.codes.ok:
                html = res.content
                f=open('dmm.html','w')
                f.write(str(html))
                soup = BeautifulSoup(html, 'html.parser')
                img = soup.find('div', attrs={'id': 'sample-video'}).find('a').get("href")
                print(img)
                tr = soup.find('table', attrs={'class': 'mg-b20'}).find_all('tr')
                for tds in tr:
                    for td in tds.find_all('td'):
                        if td.get("class") is None:
                            print(td.text)
else:
    print(Result)