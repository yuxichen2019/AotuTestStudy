from PyQt4.QtGui import *
from views.resources import ResourcesWidget
from views.monkey import MonkeyWidget


class MainTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(MainTabWidget, self).__init__(parent)
        # self.resize(400, 300)
        self.resourcesWidget = ResourcesWidget()
        self.monkeyWidget = MonkeyWidget()
        self.addTab(self.resourcesWidget, u"资源监控")
        self.addTab(self.monkeyWidget, u"Monkey")
