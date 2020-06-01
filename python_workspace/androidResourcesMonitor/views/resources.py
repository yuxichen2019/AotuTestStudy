import numpy as np
import pyqtgraph as pg
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from utils.cpuUtil import CpuUtil
from utils.memoryUtil import MemoryUtil
from utils.networkUtil import NetworkUtil
from utils.powerUtil import PowerUtil


# 资源监控视图
class ResourcesWidget(QtGui.QMainWindow):
    cpuStep = 0
    memoryStep = 0
    powerStep = 0
    networkStep = 0
    useingTimes = 0

    # 构造函数初始化
    def __init__(self, parent=None):
        super(ResourcesWidget, self).__init__(parent)
        self.initMonitorContent()
        self.initToolbar()
        self.initCpuMonitor()
        self.initMemoryMonitor()
        self.initPowerMonitor()
        self.initNetworkMonitor()

    # 初始化工具栏
    def initToolbar(self):
        startAction = QtGui.QAction(QtGui.QIcon(':/icons/start.png'), '开始', self)
        pauseAction = QtGui.QAction(QtGui.QIcon(':/icons/pause.png'), '暂停', self)
        stopAction = QtGui.QAction(QtGui.QIcon(':/icons/stop.png'), '停止', self)

        startAction.setShortcut('Ctrl+N')
        pauseAction.setShortcut('Ctrl+E')
        stopAction.setShortcut('Delete')
        startAction.triggered.connect(self.startTimer)
        pauseAction.triggered.connect(self.pauseTimer)
        stopAction.triggered.connect(self.stopTimer)
        # startAction.setStatusTip('启动监控任务')
        # pauseAction.setStatusTip('暂停监控任务')
        # stopAction.setStatusTip('停止监控任务')

        self.tb_start = self.addToolBar('Start')
        self.tb_pause = self.addToolBar('Pause')
        self.tb_stop = self.addToolBar('Stop')
        self.tb_start.addAction(startAction)
        self.tb_pause.addAction(pauseAction)
        self.tb_stop.addAction(stopAction)

    def initMonitorContent(self):
        self.workspace = QtGui.QWidget()
        self.setCentralWidget(self.workspace)

        # 第一行显示监控时长与监控类型
        firstHbox = QtGui.QHBoxLayout()
        monitorTypeHbox = QtGui.QHBoxLayout()
        self.cpuFlag = QtGui.QCheckBox("CPU")
        self.cpuFlag.setChecked(True)
        self.memoryFlag = QtGui.QCheckBox("内存")
        self.memoryFlag.setChecked(True)
        self.powerFlag = QtGui.QCheckBox("电量")
        self.powerFlag.setChecked(True)
        self.networkFlag = QtGui.QCheckBox("流量")
        self.networkFlag.setChecked(True)
        QtCore.QObject.connect(self.cpuFlag, QtCore.SIGNAL('clicked()'), self.displayCpuMonitor)
        QtCore.QObject.connect(self.memoryFlag, QtCore.SIGNAL('clicked()'), self.displayMemoryMonitor)
        QtCore.QObject.connect(self.powerFlag, QtCore.SIGNAL('clicked()'), self.displayPowerMonitor)
        QtCore.QObject.connect(self.networkFlag, QtCore.SIGNAL('clicked()'), self.displayNetworkMonitor)

        monitorTypeHbox.addWidget(self.cpuFlag)
        monitorTypeHbox.addWidget(self.memoryFlag)
        monitorTypeHbox.addWidget(self.powerFlag)
        monitorTypeHbox.addWidget(self.networkFlag)

        packageNameHbox = QtGui.QHBoxLayout()
        packageNameHbox.addWidget(QtGui.QLabel("应用包名："))
        self.packageName = QtGui.QLineEdit()
        self.packageName.setText("com.eclite.activity")
        packageNameHbox.addWidget(self.packageName)

        resultPathHbox = QtGui.QHBoxLayout()
        resultPathHbox.addWidget(QtGui.QLabel("结果路径："))
        self.resultPath = QtGui.QLineEdit()
        self.resultPath.setReadOnly(True)
        self.resultPathSelect = QtGui.QPushButton()
        self.resultPathSelect.setObjectName("browse")
        self.resultPathSelect.setText("浏览")
        resultPathHbox.addWidget(self.resultPath)
        resultPathHbox.addWidget(self.resultPathSelect)
        QtCore.QObject.connect(self.resultPathSelect, QtCore.SIGNAL('clicked()'), self.selectFolder)


        # monitorTimesHbox = QtGui.QHBoxLayout()
        # monitorTimesHbox.addWidget(QtGui.QLabel("监控时长："))
        # self.usedTimes = QtGui.QLabel("0秒")
        # monitorTimesHbox.addWidget(self.usedTimes)
        # # monitorTimesHbox.addWidget(QtGui.QSpacerItem)
        # frequencyTitle = QtGui.QLabel("监控频率：")
        # frequencyTimes = QtGui.QLabel("1秒")
        # # frequencyTitle.setAlignment(QtCore.Qt.AlignRight)
        # # frequencyTimes.setAlignment(QtCore.Qt.AlignRight)
        # monitorTimesHbox.addWidget(frequencyTitle)
        # monitorTimesHbox.addWidget(frequencyTimes)
        # monitorTimesHbox.addStretch(1)

        firstHbox.addLayout(packageNameHbox)
        firstHbox.addLayout(resultPathHbox)
        firstHbox.addLayout(monitorTypeHbox)
        # firstHbox.addLayout(monitorTimesHbox)

        monitorTypeGroupBox = QtGui.QGroupBox()
        monitorTypeGroupBox.setLayout(firstHbox)

        # 第二行显示CPU与内存的监控
        self.cpuGroupBox = QtGui.QGroupBox("CPU")
        self.memoryGroupBox = QtGui.QGroupBox("内存")

        # 第三行显示电量与流量的监控
        self.powerGroupBox = QtGui.QGroupBox("电量")
        self.networkGroupBox = QtGui.QGroupBox("流量")

        secondHbox = QtGui.QHBoxLayout()
        secondHbox.addWidget(self.cpuGroupBox)
        secondHbox.addWidget(self.memoryGroupBox)

        thirdHbox = QtGui.QHBoxLayout()
        thirdHbox.addWidget(self.powerGroupBox)
        thirdHbox.addWidget(self.networkGroupBox)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(monitorTypeGroupBox)
        vbox.addLayout(secondHbox)
        vbox.addLayout(thirdHbox)
        vbox.addStretch(1)
        self.workspace.setLayout(vbox)

    def selectFolder(self):
        absolute_path = QtGui.QFileDialog.getExistingDirectory(self, "请选择结果保存路径...", "./")
        if absolute_path:
            self.resultPath.setText(absolute_path)

    def displayCpuMonitor(self):
        if self.cpuFlag.isChecked():
            self.cpuGroupBox.show()
        else:
            self.cpuGroupBox.hide()

    def displayMemoryMonitor(self):
        if self.memoryFlag.isChecked():
            self.memoryGroupBox.show()
        else:
            self.memoryGroupBox.hide()

    def displayPowerMonitor(self):
        if self.powerFlag.isChecked():
            self.powerGroupBox.show()
        else:
            self.powerGroupBox.hide()

    def displayNetworkMonitor(self):
        if self.networkFlag.isChecked():
            self.networkGroupBox.show()
        else:
            self.networkGroupBox.hide()

    def startTimer(self):
        # 定时器采样的频率
        print("package name is:" + self.packageName.text())
        if self.packageName.text() and self.resultPath.text():
            self.timeOut()
        else:
            if not self.packageName.text():
                QtGui.QMessageBox.critical(self, '系统提示', "请输入要监控应用的包名!", "确定")
                return
            if not self.resultPath.text():
                QtGui.QMessageBox.critical(self, '系统提示', "请选择监控结果保存路径!", "确定")
                return

    def stopTimer(self):
        self.updateCpuMonitorThread.cpuTimer.stop()
        self.updateMemoryMonitorThread.memoryTimer.stop()
        self.updatePowerMonitorThread.powerTimer.stop()
        self.updateNetWorkMonitorThread.netWorkTimer.stop()

    def pauseTimer(self):
        self.updateCpuMonitorThread.cpuTimer.stop()
        self.updateMemoryMonitorThread.memoryTimer.stop()
        self.updatePowerMonitorThread.powerTimer.stop()
        self.updateNetWorkMonitorThread.netWorkTimer.stop()

        # 初始化cpu监控视图

    def initCpuMonitor(self):
        cpuVbox = QtGui.QVBoxLayout()
        win = pg.GraphicsWindow()
        plotCpu = win.addPlot()
        self.dataCpu = np.random.normal(size=10)
        # self.curveCpu = plotCpu.plot(self.dataCpu, pen='r')
        self.curveCpu = plotCpu.plot(pen='r')
        plotCpu.setDownsampling(mode='peak')
        plotCpu.setClipToView(True)
        # plotCpu.setRange(xRange=[1, 10])
        cpuVbox.addWidget(win)
        self.cpuGroupBox.setLayout(cpuVbox)

        # 更新cpu监控视图

    def updateCpuMonitor(self):
        self.updateCpuMonitorThread = CpuUtil(self.cpuStep, 10, self.packageName.text(),
                                              self.resultPath.text() + "\cpu.csv")
        self.updateCpuMonitorThread.render()
        self.connect(self.updateCpuMonitorThread, SIGNAL("output(QString,QString)"), self.updateCpuGraph)

    def updateCpuGraph(self, counter, cpuvalue):
        self.statusBar().showMessage('正在采样终端CPU占用率(单位:百分比)')
        # if float(cpuvalue) != 0:
        executeResult = np.array([int(counter), float(cpuvalue)])
        self.dataCpu[:-1] = self.dataCpu[1:]
        self.cpuStep += 1
        self.dataCpu[-1] = executeResult[1]
        self.curveCpu.setData(self.dataCpu)
        self.curveCpu.setPos(self.cpuStep, 0)
        # else:
        #     self.stopTimer()
        #     QtGui.QMessageBox.question(self, '系统提示', "没有监控到手机CPU信息，请确认手机是否连接正常?", "确定")

            # 初始化内存监控视

    def initMemoryMonitor(self):
        memoryVbox = QtGui.QVBoxLayout()
        win = pg.GraphicsWindow()
        plotMemory = win.addPlot()
        self.dataMemory = np.random.normal(size=10)
        self.curveMemory = plotMemory.plot(pen='g')
        plotMemory.setDownsampling(mode='peak')
        plotMemory.setClipToView(True)
        memoryVbox.addWidget(win)
        self.memoryGroupBox.setLayout(memoryVbox)

        # 更新内存监控视图
    def updateMemoryMonitor(self):
        self.updateMemoryMonitorThread = MemoryUtil(self.memoryStep, 10, self.packageName.text(),
                                                    self.resultPath.text() + "\memory.csv")
        self.updateMemoryMonitorThread.render()
        self.connect(self.updateMemoryMonitorThread, SIGNAL("output(QString,QString)"), self.updateMemoryGraph)

    def updateMemoryGraph(self, counter, memoryValue):
        self.statusBar().showMessage('正在采样终端内存占用大小(单位:M)')
        # if float(memoryValue) != 0:
        executeResult = np.array([int(counter), float(memoryValue)])
        self.dataMemory[:-1] = self.dataMemory[1:]
        self.memoryStep += 1
        self.dataMemory[-1] = executeResult[1]
        self.curveMemory.setData(self.dataMemory)
        self.curveMemory.setPos(self.memoryStep, 0)
        # else:
        #     self.stopTimer()
        #     QtGui.QMessageBox.question(self, '系统提示', "没有监控到手机内存信息，请确认手机是否连接正常?", "确定")

            # 初始化电量监控视图

    def initPowerMonitor(self):
        powerVbox = QtGui.QVBoxLayout()
        win = pg.GraphicsWindow()
        plotPower = win.addPlot()
        self.dataPower = np.random.normal(size=10)
        self.curvePower = plotPower.plot(pen='g')
        plotPower.setDownsampling(mode='peak')
        plotPower.setClipToView(True)
        powerVbox.addWidget(win)
        self.powerGroupBox.setLayout(powerVbox)

        # 更新内存监控视图

    def updatePowerMonitor(self):
        self.updatePowerMonitorThread = PowerUtil(self.powerStep, 10, self.resultPath.text() + "\power.csv")
        self.updatePowerMonitorThread.render()
        self.connect(self.updatePowerMonitorThread, SIGNAL("output(QString,QString)"), self.updatePowerGraph)

    def updatePowerGraph(self, counter, powerValue):
        self.statusBar().showMessage('正在采样终端耗电量(单位:百分比)')
        # if float(powerValue) != 0:
        executeResult = np.array([int(counter), float(powerValue)])
        self.dataPower[:-1] = self.dataPower[1:]
        self.powerStep += 1
        self.dataPower[-1] = executeResult[1]
        self.curvePower.setData(self.dataPower)
        self.curvePower.setPos(self.powerStep, 0)
        # else:
        #     self.stopTimer()
        #     QtGui.QMessageBox.question(self, '系统提示', "没有监控到手机内存信息，请确认手机是否连接正常?","确定")

            # 初始化网络监控视图

    def initNetworkMonitor(self):
        networkVbox = QtGui.QVBoxLayout()
        win = pg.GraphicsWindow()
        plotNetwork = win.addPlot()
        self.dataNetwork = np.random.normal(size=10)
        self.curveNetwork = plotNetwork.plot(pen='g')
        plotNetwork.setDownsampling(mode='peak')
        plotNetwork.setClipToView(True)
        networkVbox.addWidget(win)
        self.networkGroupBox.setLayout(networkVbox)

        # 更新内存监控视图

    def updateNetWorkMonitor(self):
        self.updateNetWorkMonitorThread = NetworkUtil(self.networkStep, 10, self.packageName.text(),
                                                      self.resultPath.text() + "\\netWork.csv")
        self.updateNetWorkMonitorThread.render()
        self.connect(self.updateNetWorkMonitorThread, SIGNAL("output(QString,QString)"), self.updateNetWorkGraph)

    def updateNetWorkGraph(self, counter, netWorkValue):
        self.statusBar().showMessage('正在采样终端流量消耗(单位:M)')
        # if float(netWorkValue) != 0:
        executeResult = np.array([int(counter), float(netWorkValue)])
        self.dataNetwork[:-1] = self.dataNetwork[1:]
        self.networkStep += 1
        self.dataNetwork[-1] = executeResult[1]
        self.curveNetwork.setData(self.dataNetwork)
        self.curveNetwork.setPos(self.networkStep, 0)
        # else:
        #     self.stopTimer()
        #     QtGui.QMessageBox.question(self, '系统提示', "没有监控到手机流量信息，请确认手机是否连接正常?", "确定")

    def timeOut(self):
        self.updateCpuMonitor()
        self.updateMemoryMonitor()
        self.updatePowerMonitor()
        self.updateNetWorkMonitor()
