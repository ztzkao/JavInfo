import requests
from bs4 import BeautifulSoup

def kin8tengoku_init(id):
    r = requests.get('http://www.kin8tengoku.com/moviepages/' + id + '/index.html')
    soup = BeautifulSoup(r.text, 'lxml')
    return soup

def getTite(soup):
    title = soup.find(name='p', class_='sub_title').string.strip()
    return title

def getDiscription(soup):
    description = soup.find(name='div', id="comment").string
    return description

def getInfo(id):
    tag = ''
    soup = kin8tengoku_init(id)
    rawData = soup.find_all(name='td', class_='movie_table_td2')
    act = rawData[0].a.string.replace(' ','')
    releaseTime = rawData[-1].string
    duration = rawData[-2].string.strip()
    for a in rawData[-3].find_all('a'):
        tag += a.string + ' '
    info = {
        'id': id,
        'coverLink': 'http://www.kin8tengoku.com/' + id + '/pht/1.jpg',
        'title': getTite(soup),
        'description': getDiscription(soup),
        'actor': act,
       'releaseTime': releaseTime,
       'duration': duration,
        'tags': tag[:-1]
    }
    return info

if __name__ == '__main__':
    id = input('输入id:\n')
    print(getInfo(id))