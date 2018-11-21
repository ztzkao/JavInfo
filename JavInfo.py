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
    return data
    
if __name__ == "__main__":
    siteNum = int(input('请输入网站名：\n1:caribbeancom, 2:caribbeancompr, 3:heyzo, 4:ken8tengoku, 5:1pondo, 6:R18, 7:tokyoHot\n'))-1
    id = input('请输入id：\n')
    print(getInfo(id,siteNum))