import requests
from bs4 import BeautifulSoup

def caribbeancomm_init(id):
    r = requests.get('https://www.caribbeancompr.com/moviepages/' + id + '/index.html')
    f = open('file.txt', mode='w')
    f.write(r.text)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup

def getTite(soup):
    title = soup.find(name='title').string.strip()
    return title
def getDiscription(soup):
    description = soup.find(name='div', class_='movie-comment').find(name='p').string
    return description

def getActor(soup):
    allName = ''
    for name in soup.find_all(name='a', class_= 'spec__tag', itemprop='actor'):
        allName += name.string + ' '
    return allName[:-1]

def getUploadDate(soup):
    date = soup.find(name='span', itemprop='uploadDate').string
    return date

def getDuration(soup):
    get = soup.find(name='span', itemprop='duration').string
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
    soup = caribbeancomm_init(id)
    # diction = {
    #     'id': id,
    #     'coverLink': 'https://www.caribbeancom.com/moviepages/' + id + '/images/l_l.jpg',
    #     'title': getTite(soup),
    #     'description': getDiscription(soup),
    #     'actor': getActor(soup),
    #     'releaseTime': getUploadDate(soup),
    #     'duration': getDuration(soup),
    #     'tags': getTags(soup)
    # }
    # print(getDiscription(soup))
