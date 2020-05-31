import sys

from PyQt4 import QtGui
from utils.SplashScreen import SplashScreen
from views.mainTabs import MainTabWidget


class ARM(QtGui.QMainWindow):

    def __init__(self):
        super(ARM, self).__init__()
        self.initMenu()
        self.initMainTab()
        self.resize(950, 600)
        self.setMinimumSize(950, 600)
        self.setWindowTitle('AndroidTools')
        self.setWindowIcon(QtGui.QIcon(':/icons/monitor.png'))

        # 初始化菜单栏

    def initMenu(self):
        menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&文件')
        helpMenu = menubar.addMenu('&帮助')
        helpMenu.addMenu('&关于')
        helpMenu.addMenu('&帮助')


    def center(self):  # 主窗口居中显示函数
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def initMainTab(self):
        self.mainTabWidget = MainTabWidget()
        self.setCentralWidget(self.mainTabWidget)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    splash = SplashScreen()
    splash.effect()
    app.processEvents()
    arm = ARM()
    arm.show()
    arm.center()
    splash.finish(arm)
    sys.exit(app.exec_())
