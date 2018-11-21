import requests
import os
from sites import caribbeancom
from sites import caribbeancompr
from sites import heyzo
from sites import ken8tengoku
from sites import _1pondo
from sites import R18
from sites import tokyoHot
from threading import Thread

siteNameList = ['caribbeancom', 'caribbeancompr', 'heyzo', 'ken8tengoku', '1pondo', 'R18', 'tokyoHot']
siteDict = {
    'caribbeancom': 'caribbeancom.caribbeancomm_init(id)', 
    'caribbeancompr': 'caribbeancompr.caribbeancommpr_init(id)',
    'heyzo': 'heyzo.heyzo_init(id)', 
    'ken8tengoku': 'ken8tengoku.kin8tengoku_init(id)', 
    '1pondo': '_1pondo._1pondo_init(id)', 
    'R18': 'R18.R18_init(id)', 
    'tokyoHot': 'tokyoHot.tokyoHot_init(id)'
}

def getInfo(id, siteNum):
    data = eval(str(siteDict[siteNameList[int(siteNum)]]))
    saveImage(data)
    return data

def saveImage(item):
    if not os.path.exists('cover'):
        os.mkdir('cover')
    try:
        response = requests.get(item['coverLink'])
        if response.status_code == 200:
            file_path = "{0}/{1}.{2}".format('cover',item['id'], 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                    item['coverPATH'] = file_path
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')
if __name__ == "__main__":
    siteNum = int(input('请输入网站名：\n1:caribbeancom, 2:caribbeancompr, 3:heyzo, 4:ken8tengoku, 5:1pondo, 6:R18, 7:tokyoHot\n'))-1
    id = input('请输入id：\n')
    print(getInfo(id,siteNum))