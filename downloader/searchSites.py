import youtube_dl
from bs4 import BeautifulSoup
import requests
import os
import re 
import downloader
from threading import Thread
import time

class MyThread(Thread):
    def __init__(self,site,id):
        Thread.__init__(self)
        self.id = id
        self.site = site
    def run(self):
        self.data = searchAll(self.site,self.id)
        
    def get_resule(self):
        return self.data

def searchSddpoav(keyword):
    Result = {
        "site": "SDDPOAV",
        "result": "FAIL",
        "url": "",
        "filename": "",
    }
    res = requests.get('http://sddpoav.com/?s=' + keyword)
    if res.status_code == requests.codes.ok:
        html = res.content
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find('div', attrs={'class': 'video'})
        if data is not None:
            if data.find('a') is not None:
                href = data.find('a').get('href')
                res = requests.get(href)
                if res.status_code == requests.codes.ok:
                    html = res.content
                    soup = BeautifulSoup(html, 'html.parser')
                    video_path = soup.find('div', attrs={'class': 'video_code'}).find('iframe').get('src')
                    ydl = youtube_dl.YoutubeDL({'quiet': True})
                    with ydl:
                        youtube_dlresult = ydl.extract_info(
                            video_path,
                            download=False  # !!We just want to extract the info
                        )
                    if 'entries' in youtube_dlresult:
                        # Can be a playlist or a list of videos
                        video = youtube_dlresult['entries'][0]
                    else:
                        # Just a video
                        video = youtube_dlresult
                    #print(video)
                    Result['result'] = "PASS"
                    Result['url'] = video['url']
                    Result['filename'] = video['title']
                    #print urllib2.build_opener().open(video['url']).info()
                    return Result
    return Result
def searchDl8X(keyword):
    Result = {
        "site": "Dl8X",
        "result": "FAIL",
        "url": "",
        "filename": "",
    }
    res = requests.get('https://www.dl8x.com/search?query=' + keyword)
    if res.status_code == requests.codes.ok:
        html = res.content
        soup = BeautifulSoup(html, 'html.parser')
        for data in soup.find_all('div', attrs={'class': 'float-left dx-vertical-item dx-video-entry-frame'}):
            if data.find('div', attrs={'class': 'dx-video-entry-title'}) is not None and data.find('div', attrs={'class': 'dx-video-entry-site dx-video-entry-label '}) is not None:
                if data.find('div', attrs={'class': 'dx-video-entry-site dx-video-entry-label '}).find('span').text == "Openload":
                    res = requests.get('https://www.dl8x.com'+data.find('a').get('href'))
                    if res.status_code == requests.codes.ok:
                        html = res.content
                        soup = BeautifulSoup(html, 'html.parser')
                        video_path = soup.find('iframe', attrs={'allowfullscreen': ''}).get('src')
                        ydl = youtube_dl.YoutubeDL({'quiet': True})
                        with ydl:
                            youtube_dlresult = ydl.extract_info(
                                video_path,
                                download=False  # !!We just want to extract the info
                            )
                        if 'entries' in youtube_dlresult:
                            # Can be a playlist or a list of videos
                            video = youtube_dlresult['entries'][0]
                        else:
                            # Just a video
                            video = youtube_dlresult
                        Result['result'] = "PASS"
                        Result['url'] = video['url']
                        Result['filename'] = video['title']
                        return Result
    return Result

def searchPorn68(keyword):
    
    Result = {
        "site": "Porn68",
        "result": "FAIL",
        "url": "",
        "filename": "",
    }
    try:
        res = requests.get('http://porn68jav.com/?s=' + keyword)
        if res.status_code == requests.codes.ok:
            html = res.content
            soup = BeautifulSoup(html, 'html.parser')
            if soup.find('a', attrs={'class': 'clip-link'}) is not None:
                data = soup.find('a', attrs={'class': 'clip-link'}).get("href")
                res = requests.get(data)
                if res.status_code == requests.codes.ok:
                    html = res.content
                    soup = BeautifulSoup(html, 'html.parser')
                    video_path = soup.find('iframe', attrs={'id': 'mIframe'}).get("src")
                    ydl = youtube_dl.YoutubeDL({'quiet': True})
                    with ydl:
                        youtube_dlresult = ydl.extract_info(
                            video_path,
                            download=False  # !!We just want to extract the info
                        )
                    if 'entries' in youtube_dlresult:
                        # Can be a playlist or a list of videos
                        video = youtube_dlresult['entries'][0]
                    else:
                        # Just a video
                        video = youtube_dlresult
                    Result['result'] = "PASS"
                    Result['url'] = video['url']
                    Result['filename'] = video['title']
                    return Result
        return Result
    except youtube_dl.utils.DownloadError:
        return Result

def searchAll(siteID, keyword):
    if siteID == 0:
        return searchSddpoav(keyword)
    elif siteID == 1:
        return searchPorn68(keyword)
    elif siteID == 2:
        return searchDl8X(keyword)
    else:
        return -1
    
def startSearch(keyword):
    Result = {
        "site": "",
        "result": "FAIL",
        "url": "",
        "filename": "",
    }
    t_objs =[]
    for i in range(3):
        t = MyThread(i, keyword)
        t.start()
        t_objs.append(t)
    for t in t_objs:
        t.join()
    for t in t_objs:
        Result = t.get_resule()
        print(Result['result'])   
        if Result['result'] == 'PASS':
            return Result
    return Result
if __name__ == "__main__":
    print(startSearch('ddt-551'))