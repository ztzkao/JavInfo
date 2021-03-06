import sys
import requests
from bs4 import BeautifulSoup

def caribbeancommpr_init(id):
    try:
        r = requests.get('https://www.caribbeancompr.com/moviepages/' + id + '/index.html')
        r.encoding = 'euc-jp'
        soup = BeautifulSoup(r.text, 'lxml')
        diction = {
            'id': id,
            'coverLink': 'https://www.caribbeancompr.com/moviepages/' + id + '/images/l_l.jpg',
            'title': getTite(soup),
            'description': getDiscription(soup),
            'actor': getActor(soup),
            'releaseTime': getUploadDate(soup),
            'duration': getDuration(soup),
            'tags': getTags(soup),
            'coverPATH': ''
        }
        return diction
    except AttributeError:
        return -1

def getTite(soup):
    title = soup.find(name='div', class_='video-detail').find(name='h1').string.strip()
    return title
def getDiscription(soup):
    description = soup.find(name='div', class_='movie-comment').find(name='p').string
    return description

def getActor(soup):
    allName = ''
    for name in soup.find(name='div', class_='movie-info').find_all(name='strong'):
        allName += name.string + ' '
    return allName[:-1]

def getUploadDate(soup):
    date = soup.find(name='div', class_='movie-info').find_all(name='dd')[-4].string
    return date

def getDuration(soup):
    get = soup.find(name='div', class_='movie-info').find_all(name='dd')[-5].string
    duration = get.strip()
    return duration

def getTags(soup):
    tags = ''
    for name in soup.find(name='dl', class_='movie-info-cat').find_all(name='a'):
        for a in name:
            tags += a.string + ' '
    return tags[:-1]

if __name__ == '__main__':
    id = input('输入id:\n')
    print(caribbeancommpr_init(id))
