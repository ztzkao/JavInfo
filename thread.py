from PyQt5 import QtCore
from downloader import searchSites
import JavInfo

class searchLinkThread(QtCore.QObject):
    def __init__(self, site, id):
        super(searchLinkThread, self).__init__()
        self.site = site
        self.id = id
        self.doWork()
    def doWork(self):
        self.data = searchSites.searchAll(self.site, self.id)
    def getResult(self):
        return self.data

class searchDataThread(QtCore.QObject):
    def __init__(self, site, id):
        super(searchDataThread, self).__init__()
        self.site = site
        self.id = id
    def doWork(self):
        self.data = JavInfo.getInfo(self.site, self.id)
    def getResult(self):
        return self.data

