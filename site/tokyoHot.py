import re
import requests
from bs4 import BeautifulSoup

def tokyoHot_init(id):
    r = requests.get('https://my.tokyo-hot.com/product/?q=' + id + '&x=0&y=0')
    search = BeautifulSoup(r.text, 'lxml')
    getLink = 'https://my.tokyo-hot.com' + search.find(name='a', class_='rm')['href']
    real = requests.get(getLink)
    soup = BeautifulSoup(real.text, 'lxml')
    return soup

def getTite(soup):
    title = soup.find(name='div', class_="contents").h2.string
    return title

def getDiscription(soup):
    description = soup.find(name='div', class_="sentence").string
    return description

def getInfo(soup):
    tag = ''
    p = re.compile('<[^>]+>')
    soup = tokyoHot_init(id)
    rawData = soup.find(name='dl', class_='info').find_all('dd')
    desc = soup.find('div', class_='sentence')
    description = p.sub('', str(desc)).strip()
    act = rawData[0].a.string
    cover = soup.find('div', class_=re.compile("^flowplayer")).video.attrs['poster']
    releaseTime = rawData[5].string
    duration = rawData[6].string

    for a in rawData[2].find_all('a'):
        tag += a.string + ' '

    info = {
        'id': id,
        'coverLink': cover,
        'title': getTite(soup),
        'description': description,
        'actor': act,
        'releaseTime': releaseTime,
        'duration': duration,
        'tags': tag[:-1]
    }
    return info

if __name__ == '__main__':
    id = input('输入id:\n')
    print(getInfo(id))
