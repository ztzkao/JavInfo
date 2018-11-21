from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from UI import Ui_MainWindow
from downloader import searchSites
import JavInfo


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self,parent=None):
		super(MyWindow, self).__init__(parent)
		self.setupUi(self)
		self.Search.clicked.connect(self.searchButtonClick)
	def searchButtonClick(self):
		self.CoverLable.setText('正在获取')
		keyword = self.inputID.text()
		site = self.selectSite.currentIndex()
		list = []
		data = JavInfo.getInfo(keyword,site)
		self.Title.setText(str(data['title']))
		self.Actor.setText(str(data['actor']))
		self.Tags.setText(str(data['tags']))
		self.releaseDate.setText(str(data['releaseTime']))
		self.Duration.setText(str(data['duration']))
		self.pixmap = QPixmap (data['coverPATH'])
		self.CoverLable.setPixmap(self.pixmap)
		self.CoverLable.setScaledContents(True)

		for i in range(3):
			list.insert(i,searchSites.searchAll(i,keyword))
			if list[i]['result'] == 'PASS':
				self.downloadPATH.setText(str(list[i]['filename']))
				self.downloadURL.setText(str(list[i]['url']))



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	mainWindow = MyWindow()
	mainWindow.show()
	sys.exit(app.exec_())
