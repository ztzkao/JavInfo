import requests
from bs4 import BeautifulSoup

def caribbeancomm_init(id):
    r = requests.get('https://www.caribbeancom.com/moviepages/' + id + '/index.html')
    soup = BeautifulSoup(r.text, 'lxml')
    diction = {
        'id': id,
        'coverLink': 'https://www.caribbeancom.com/moviepages/' + id + '/images/l_l.jpg',
        'title': getTite(soup),
        'description': getDiscription(soup),
        'actor': getActor(soup),
        'releaseTime': getUploadDate(soup),
        'duration': getDuration(soup),
        'tags': getTags(soup)
    }
    return diction

def getTite(soup):
    title = soup.find(name='h1', itemprop="name").string
    return title

def getDiscription(soup):
    description = soup.find(name='p', itemprop="description").string
    return description

def getActor(soup):
    allName = ''
    for name in soup.find_all(name='a', class_= 'spec__tag', itemprop="actor"):
        allName += name.string + ' '
    return allName[:-1]

def getUploadDate(soup):
    date = soup.find(name='span', itemprop="uploadDate").string
    return date

def getDuration(soup):
    get = soup.find(name='span', itemprop="duration").string
    duration = get.strip()
    return duration

def getTags(soup):
    tags = ''
    for name in soup.find_all(name='span', class_='spec-content'):
        for a in name.find_all(name='a', itemprop='url'):
            tags += a.string + ' '
        for a in name.find_all(name='a', itemprop='genre'):
            tags += a.string + ' '
    return tags[:-1]

if __name__ == '__main__':
    id = input('输入id:\n')
    print(caribbeancomm_init(id))
