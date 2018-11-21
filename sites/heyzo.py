import  re
import requests
from bs4 import BeautifulSoup

def heyzo_init(id):
    try:
        r = requests.get('http://www.heyzo.com/moviepages/' + id + '/index.html')
        soup = BeautifulSoup(r.text, 'lxml')
        diction = {
            'id': id,
            'coverLink': 'http://www.heyzo.com/contents/3000/'+ id +'/images/player_thumbnail.jpg',
            'title': getTite(soup),
            'description': getDiscription(soup),
            'actor': getActor(soup),
            'releaseTime': getUploadDate(soup),
            'duration': getDuration(soup),
            'tags': getTags(soup)
        }
        return diction
    except AttributeError:
        return -1

def getTite(soup):
    title = soup.find(name='h1').string.strip().replace("\t", "").replace("\n", "")
    return title

def getDiscription(soup):
    description = soup.find(name='p', class_="memo").string
    return description

def getActor(soup):
    allName = ''
    for name in soup.find(name='tr', class_='table-actor').find_all('span'):
        allName += name.string + ' '
    return allName[:-1]

def getUploadDate(soup):
    date = soup.find(name='tr', class_="table-release-day").find_all('td')[1].string.strip()
    return date

def getDuration(soup):
    get = str(soup)
    duration = re.search('\{\"full\"\:\"(.?.?.?.?.?.?.?.?).*?\"\}\;', get).group(1)
    return duration

def getTags(soup):
    tags = ''
    for a in soup.find(name='ul', class_='tag-keyword-list').find_all('a'):
        tags += a.string + ' '
    return tags[:-1]

if __name__ == '__main__':
    id = input('输入id:\n')
    print(heyzo_init(id))
