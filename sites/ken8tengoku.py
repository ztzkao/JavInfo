import requests
from bs4 import BeautifulSoup

def getTite(soup):
    title = soup.find(name='p', class_='sub_title').string.strip()
    return title

def getDiscription(soup):
    description = soup.find(name='div', id="comment").string
    return description
def kin8tengoku_init(id):
    try:
        r = requests.get('http://www.kin8tengoku.com/moviepages/' + id + '/index.html')
        soup = BeautifulSoup(r.text, 'lxml')
        tag = ''
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
            'tags': tag[:-1],
            'coverPATH': ''
        }
        return info
    except IndexError:
        return -1
        
if __name__ == '__main__':
    id = input('输入id:\n')
    print(kin8tengoku_init(id))
