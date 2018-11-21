from PyQt5 import QtCore, QtGui, QtWidgets
from UI import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self,parent=None):
		super(MyWindow, self).__init__(parent)
		self.setupUi(self)
		self.Search.clicked.connect(self.downloadButtonClick)
	def downloadButtonClick(self):
		self.statu.setText('正在获取')
		t_link = []
		Th = QtCore.QThread()
		keyword = self.inputID.text()
		from thread import searchLinkThread
		for i in range(3):
			t=searchLinkThread(i,keyword)
			t_link.append(t)
		for t in t_link:
			t.moveToThread(Th)
		Th.start()
		for t in t_link:
			data = t.getResult()
			if data['result']=='PASS':
				self.downloadURL.setText(str(data['url']))
				self.downloadPATH.setText(str(data['filename']))



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	mainWindow = MyWindow()
	mainWindow.show()
	sys.exit(app.exec_())
