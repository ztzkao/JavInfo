import requests
from bs4 import BeautifulSoup

def caribbeancomm_init(id):
    r = requests.get('https://cn.caribbeancom.com/moviepages/' + id + '/index.html')
    soup = BeautifulSoup(r.text, 'lxml')
    return soup
def getactor_cn(soup):
    fullname = ''
    for name in soup.find_all(name='span', itemprop="name"):
        fullname += name.string + ' '
    return fullname

def getcat_cn(soup):
    cates = ''
    for name in soup.find_all(name='dl', class_='movie-info-cat'):
        for span in name.find_all(name='span'):
            cates += span.string + ' '
        for a in name.find_all(name='a', itemprop = 'genre'):
            cates += a.string + ' '
    return cates

def getuploadDate_cn(soup):
    date = soup.find(name='dd', itemprop="uploadDate").string
    return date

def getduration_cn(soup):
    get = soup.find(name='span', itemprop="duration").string
    duration = get.replace(' ', '')
    return duration
if __name__ == '__main__':
    id = input('输入id:\n')
    r = requests.get('https://cn.caribbeancom.com/moviepages/' + id + '/index.html')
    soup = BeautifulSoup(r.text, 'lxml')
    print(getcat_cn(soup)+ '\n')
    print(getactor_cn(soup) + '\n')
    print(getuploadDate_cn(soup) + '\n')
    print(str(getduration_cn(soup)) + '\n')
