import re
import requests
from bs4 import BeautifulSoup
p = re.compile('<[^>]+>')

def getCode(link):
    final = re.search('id\=(.*?)\/', link).group(1)
    return final

def R18_init(id):


    r = requests.get('http://www.r18.com/common/search/searchword=' + id + '/')
    search = BeautifulSoup(r.text, 'lxml')
    link = search.find(name='li', class_='item-list').a['href']
    code = getCode(link)
    real = requests.get('http://www.r18.com/videos/vod/movies/detail/-/id=' + code + '/?lg=zh')
    real.encoding = 'UTF-8'
    soup = BeautifulSoup(real.text, 'lxml')
    diction = {
        'id': id,
        'coverLink': 'https://pics.r18.com/digital/video/' + code + '/' + code + 'pl.jpg',
        'title': getTite(soup),
        'description': getDiscription(soup),
        'actor': getActor(soup),
        'releaseTime': getUploadDate(soup),
        'duration': getDuration(soup),
        'tags': getTags(soup)
    }
    return diction

def getTite(soup):
    title = soup.find(name='cite', itemprop='name').string.strip()
    return title

def getDiscription(soup):
    pass

def getActor(soup):
    allName = ''
    for name in soup.find(name='div', itemprop="actors").find_all(name='a'):
        allName += str(name.span.string) + ' '
    return allName[:-1]

def getUploadDate(soup):
    date = soup.find(name='dd', itemprop="dateCreated")
    date = p.sub("", str(date)).strip()
    return date

def getDuration(soup):
    get = soup.find(name='dd', itemprop="duration")
    duration = re.search('(.*?)分鐘', str(get)).group(1).strip() + 'min'
    return duration

def getTags(soup):
    tags = ''
    for name in soup.find(name='div', class_="product-categories-list product-box-list").find_all(name='a', itemprop="genre"):
        for a in name:
            tags += a.string.strip() + ' '
    return tags[:-1]

if __name__ == '__main__':
    id = input('输入id:\n')
    print(R18_init(id))

