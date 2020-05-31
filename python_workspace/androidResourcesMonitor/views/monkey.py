from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QColor
from PyQt4.QtGui import QTableWidgetItem
from utils.monkeyUtil import MonkeyUtil
from utils.reportUtil import ReportUtil
from utils.commonUtil import CommonUtil
import os


# 资源监控视图
class MonkeyWidget(QtGui.QMainWindow):
    # 构造函数初始化
    def __init__(self, parent=None):
        super(MonkeyWidget, self).__init__(parent)
        self.initMonkeyContent()
        self.initToolbar()
        self.initInputAndOutput()
        self.initDebugParameger()
        self.initOperateAction()
        self.initOperateAction2()
        self.initConsoleOutput()

    # 初始化工具栏
    def initToolbar(self):
        startAction = QtGui.QAction(QtGui.QIcon(':/icons/start.png'), '开始', self)
        stopAction = QtGui.QAction(QtGui.QIcon(':/icons/stop.png'), '停止', self)

        startAction.setShortcut('Ctrl+N')
        stopAction.setShortcut('Delete')
        startAction.triggered.connect(self.startMonkeyTask)
        stopAction.triggered.connect(self.stopMonkeyTask)

        self.tb_start = self.addToolBar('Start')
        self.tb_stop = self.addToolBar('Stop')
        self.tb_start.addAction(startAction)
        self.tb_stop.addAction(stopAction)

    def startMonkeyTask(self):
        actionPersent = 0
        # 事件参数
        if self.touchAction.isChecked():
            actionPersent = actionPersent + int(self.touchActionSpinBox.text())
        if self.trackballAction.isChecked():
            actionPersent = actionPersent + int(self.trackballActionSpinBox.text())
        if self.rotationAction.isChecked():
            actionPersent = actionPersent + int(self.rotationActionSpinBox.text())
        if self.navAction.isChecked():
            actionPersent = actionPersent + int(self.navActionSpinBox.text())
        if self.sysAction.isChecked():
            actionPersent = actionPersent + int(self.sysActionSpinBox.text())
        if self.appswitchAction.isChecked():
            actionPersent = actionPersent + int(self.appswitchActionSpinBox.text())
        if self.flipAction.isChecked():
            actionPersent = actionPersent + int(self.flipActionSpinBox.text())
        if self.otherAction.isChecked():
            actionPersent = actionPersent + int(self.otherActionSpinBox.text())

        if self.packageName.text() and self.logPath.text() and int(
                self.countValueEdit.text().strip()) > 0 and actionPersent <= 100:
            self.consoleOutputEdit.clear()
            self.monkeyTaskThread = MonkeyUtil(self.setParameter(self.packageName.text()), self.logPath.text())
            self.monkeyTaskThread.render()
            self.statusBar().showMessage('正在执行Monkey测试')
            self.connect(self.monkeyTaskThread, SIGNAL("output(QString)"), self.printLog)
            self.connect(self.monkeyTaskThread, SIGNAL("output(QString,QString)"), self.printReport)
        else:
            if not self.packageName.text():
                QtGui.QMessageBox.critical(self, '系统提示', "请输入要测试的应用包名!", "确定")
                return
            if not self.logPath.text():
                QtGui.QMessageBox.critical(self, '系统提示', "请选择日志的存储路径!", "确定")
                return
            if int(self.countValueEdit.text().strip()) <= 0:
                QtGui.QMessageBox.critical(self, '系统提示', "Monkey的测试次数要大于零!", "确定")
                return
            # 验证事件的比例不能大于100%
            if actionPersent > 100:
                QtGui.QMessageBox.critical(self, '系统提示', "Monkey的件比例总和不能大于100", "确定")
                return

    def stopMonkeyTask(self):
        commonUtil = CommonUtil("monkey", 1)
        monkeyPid = commonUtil.getPid()
        if monkeyPid:
            # kill 进程终止monkey
            os.popen("adb shell kill -9 " + monkeyPid)
            self.printReport(self.monkeyTaskThread.logFile, "True")

    def printLog(self, log):
        # print(log)
        self.consoleOutputEdit.append(log)

    def printReport(self, report, flag):
        if flag:
            self.statusBar().showMessage('请稍等，正在为您解析日志信息!!!')
            self.reportTable.clearContents()
        self.reportUtil = ReportUtil(report)
        self.reportData = self.reportUtil.analysisLog(flag)
        errorCount = 0
        for i in range(9):
            for j in range(3):
                newItem = QTableWidgetItem(str(self.reportData[i][j]))
                if j == 1:
                    if (int(self.reportData[i][j]) > 0):
                        errorCount = errorCount + int(self.reportData[i][j])
                        newItem.setBackgroundColor(QColor(255, 0, 0))
                self.reportTable.setItem(i, j, newItem)

        if flag:
            self.statusBar().showMessage('当前日志路径为：' + report)

        if errorCount > 0:
            QtGui.QMessageBox.critical(self, '系统提示', "Monkey的测试结果有异常，请核对高亮显示的错误信息！！！", "确定")
            return

    def initMonkeyContent(self):
        self.workspace = QtGui.QWidget()
        self.setCentralWidget(self.workspace)

        # 第一行Monkey输入输出参数
        self.firstHbox = QtGui.QHBoxLayout()
        self.monkeyInputAndOutputBox = QtGui.QGroupBox()

        # 第二行调试参数
        self.debugParameterBox = QtGui.QGroupBox("调试参数")

        # 第三行操作事件
        self.operateActionBox = QtGui.QGroupBox("操作事件1")
        self.operateActionBox2 = QtGui.QGroupBox("操作事件2")

        # 第四行输出控制台
        self.consoleGroupBox = QtGui.QGroupBox("控制台输出")

        thirdHbox = QtGui.QHBoxLayout()
        thirdHbox.addWidget(self.operateActionBox)
        thirdHbox.addWidget(self.operateActionBox2)

        forthHbox = QtGui.QHBoxLayout()
        forthHbox.addWidget(self.consoleGroupBox)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.monkeyInputAndOutputBox)
        vbox.addWidget(self.debugParameterBox)
        vbox.addLayout(thirdHbox)
        vbox.addLayout(forthHbox)
        self.workspace.setLayout(vbox)

    def selectFolder(self):
        absolute_path = QtGui.QFileDialog.getExistingDirectory(self, "请选择结果保存路径...", "./")
        if absolute_path:
            self.logPath.setText(absolute_path)

    # 初始化输入输出
    def initInputAndOutput(self):
        packageNameHbox = QtGui.QHBoxLayout()
        packageNameHbox.addWidget(QtGui.QLabel("应用包名："))
        self.packageName = QtGui.QLineEdit()
        self.packageName.setText("com.eclite.activity")
        packageNameHbox.addWidget(self.packageName)

        logPathHbox = QtGui.QHBoxLayout()
        logPathHbox.addWidget(QtGui.QLabel("日志路径："))
        self.logPath = QtGui.QLineEdit()
        self.logPath.setReadOnly(True)
        self.logPathSelect = QtGui.QPushButton()
        self.logPathSelect.setObjectName("browse")
        self.logPathSelect.setText("浏览")
        logPathHbox.addWidget(self.logPath)
        logPathHbox.addWidget(self.logPathSelect)
        QtCore.QObject.connect(self.logPathSelect, QtCore.SIGNAL('clicked()'), self.selectFolder)

        self.firstHbox.addLayout(packageNameHbox)
        self.firstHbox.addLayout(logPathHbox)
        self.monkeyInputAndOutputBox.setLayout(self.firstHbox)

    # 初始化调试参数
    def initDebugParameger(self):
        self.leftDebugParameterHbox = QtGui.QHBoxLayout()
        self.ignoreCrashesCheckBox = QtGui.QCheckBox("忽略奔溃")
        self.ignoreTimeoutsCheckBox = QtGui.QCheckBox("忽略超时")
        self.ignoreSecurityExceptionsCheckBox = QtGui.QCheckBox("忽略Monkey异常")
        self.monitorNativeCrashesCheckBox = QtGui.QCheckBox("报告奔溃事件")
        self.leftDebugParameterHbox.addWidget(self.ignoreCrashesCheckBox)
        self.leftDebugParameterHbox.addWidget(self.ignoreTimeoutsCheckBox)
        self.leftDebugParameterHbox.addWidget(self.ignoreSecurityExceptionsCheckBox)
        self.leftDebugParameterHbox.addWidget(self.monitorNativeCrashesCheckBox)

        self.rightDebugParameterHbox = QtGui.QHBoxLayout()
        seedValueHbox = QtGui.QHBoxLayout()
        seedValueHbox.addWidget(QtGui.QLabel("种子值："))
        self.seedValueEdit = QtGui.QLineEdit()
        self.seedValueEdit.setText("0")
        seedValueHbox.addWidget(self.seedValueEdit)

        throttleHbox = QtGui.QHBoxLayout()
        throttleHbox.addWidget(QtGui.QLabel("延时："))
        self.throttleValueEdit = QtGui.QLineEdit()
        self.throttleValueEdit.setText("0")
        throttleHbox.addWidget(self.throttleValueEdit)

        countHbox = QtGui.QHBoxLayout()
        countHbox.addWidget(QtGui.QLabel("次数："))
        self.countValueEdit = QtGui.QLineEdit()
        self.countValueEdit.setText("30000")
        countHbox.addWidget(self.countValueEdit)

        self.rightDebugParameterHbox.addLayout(seedValueHbox)
        self.rightDebugParameterHbox.addLayout(throttleHbox)
        self.rightDebugParameterHbox.addLayout(countHbox)

        self.ignoreCrashesCheckBox.setChecked(True)
        self.ignoreTimeoutsCheckBox.setChecked(True)
        self.ignoreSecurityExceptionsCheckBox.setChecked(True)
        self.monitorNativeCrashesCheckBox.setChecked(True)
        debugParamegerHbox = QtGui.QHBoxLayout()
        debugParamegerHbox.addLayout(self.leftDebugParameterHbox)
        debugParamegerHbox.addLayout(self.rightDebugParameterHbox)
        self.debugParameterBox.setLayout(debugParamegerHbox)

    # 初始化操作事件视图
    def initOperateAction(self):
        # 点击事件
        operateActionVbox = QtGui.QVBoxLayout()
        self.touchActionHbox = QtGui.QHBoxLayout()
        self.touchAction = QtGui.QCheckBox("点击")
        self.touchActionSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.touchActionSpinBox = QtGui.QSpinBox()
        self.touchActionSlider.setRange(0, 100)
        self.touchActionSpinBox.setRange(0, 100)
        self.touchActionSpinBox.setDisabled(True)
        self.touchActionSlider.setDisabled(True)
        self.touchActionHbox.addWidget(self.touchAction)
        self.touchActionHbox.addWidget(self.touchActionSlider)
        self.touchActionHbox.addWidget(self.touchActionSpinBox)

        QtCore.QObject.connect(self.touchActionSlider, QtCore.SIGNAL("valueChanged(int)"), self.touchActionSpinBox,
                               QtCore.SLOT("setValue(int)"))
        QtCore.QObject.connect(self.touchActionSpinBox, QtCore.SIGNAL("valueChanged(int)"), self.touchActionSlider,
                               QtCore.SLOT("setValue(int)"))

        # 滑动事件
        self.trackballActionHbox = QtGui.QHBoxLayout()
        self.trackballAction = QtGui.QCheckBox("滑动")
        self.trackballActionSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.trackballActionSpinBox = QtGui.QSpinBox()
        self.trackballActionSlider.setRange(0, 100)
        self.trackballActionSpinBox.setRange(0, 100)
        self.trackballActionSlider.setDisabled(True)
        self.trackballActionSpinBox.setDisabled(True)
        self.trackballActionHbox.addWidget(self.trackballAction)
        self.trackballActionHbox.addWidget(self.trackballActionSlider)
        self.trackballActionHbox.addWidget(self.trackballActionSpinBox)

        QtCore.QObject.connect(self.trackballActionSlider, QtCore.SIGNAL("valueChanged(int)"),
                               self.trackballActionSpinBox,
                               QtCore.SLOT("setValue(int)"))
        QtCore.QObject.connect(self.trackballActionSpinBox, QtCore.SIGNAL("valueChanged(int)"),
                               self.trackballActionSlider,
                               QtCore.SLOT("setValue(int)"))

        # 旋转事件
        self.rotationActionHbox = QtGui.QHBoxLayout()
        self.rotationAction = QtGui.QCheckBox("旋转")
        self.rotationActionSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.rotationActionSpinBox = QtGui.QSpinBox()
        self.rotationActionSlider.setRange(0, 100)
        self.rotationActionSpinBox.setRange(0, 100)
        self.rotationActionSlider.setDisabled(True)
        self.rotationActionSpinBox.setDisabled(True)
        self.rotationActionHbox.addWidget(self.rotationAction)
        self.rotationActionHbox.addWidget(self.rotationActionSlider)
        self.rotationActionHbox.addWidget(self.rotationActionSpinBox)

        QtCore.QObject.connect(self.rotationActionSlider, QtCore.SIGNAL("valueChanged(int)"),
                               self.rotationActionSpinBox,
                               QtCore.SLOT("setValue(int)"))
        QtCore.QObject.connect(self.rotationActionSpinBox, QtCore.SIGNAL("valueChanged(int)"),
                               self.rotationActionSlider,
                               QtCore.SLOT("setValue(int)"))

        # 导航事件
        self.navActionHbox = QtGui.QHBoxLayout()
        self.navAction = QtGui.QCheckBox("导航")
        self.navActionSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.navActionSpinBox = QtGui.QSpinBox()
        self.navActionSlider.setRange(0, 100)
        self.navActionSpinBox.setRange(0, 100)
        self.navActionSlider.setDisabled(True)
        self.navActionSpinBox.setDisabled(True)
        self.navActionHbox.addWidget(self.navAction)
        self.navActionHbox.addWidget(self.navActionSlider)
        self.navActionHbox.addWidget(self.navActionSpinBox)

        QtCore.QObject.connect(self.navActionSlider, QtCore.SIGNAL("valueChanged(int)"),
                               self.navActionSpinBox,
                               QtCore.SLOT("setValue(int)"))
        QtCore.QObject.connect(self.navActionSpinBox, QtCore.SIGNAL("valueChanged(int)"),
                               self.navActionSlider,
                               QtCore.SLOT("setValue(int)"))

        operateActionVbox.addLayout(self.touchActionHbox)
        operateActionVbox.addLayout(self.trackballActionHbox)
        operateActionVbox.addLayout(self.rotationActionHbox)
        operateActionVbox.addLayout(self.navActionHbox)
        self.operateActionBox.setLayout(operateActionVbox)

        self.touchAction.clicked.connect(lambda: self.enableAction("touchAction"))
        self.trackballAction.clicked.connect(lambda: self.enableAction("trackballAction"))
        self.rotationAction.clicked.connect(lambda: self.enableAction("rotationAction"))
        self.navAction.clicked.connect(lambda: self.enableAction("navAction"))

    # 选择action
    def enableAction(self, action=''):
        if action == "touchAction":
            if self.touchAction.isChecked():
                self.touchActionSlider.setDisabled(False)
                self.touchActionSpinBox.setDisabled(False)
            else:
                self.touchActionSlider.setDisabled(True)
                self.touchActionSpinBox.setDisabled(True)
        if action == "trackballAction":
            if self.trackballAction.isChecked():
                self.trackballActionSlider.setDisabled(False)
                self.trackballActionSpinBox.setDisabled(False)
            else:
                self.trackballActionSlider.setDisabled(True)
                self.trackballActionSpinBox.setDisabled(True)
        if action == "rotationAction":
            if self.rotationAction.isChecked():
                self.rotationActionSlider.setDisabled(False)
                self.rotationActionSpinBox.setDisabled(False)
            else:
                self.rotationActionSlider.setDisabled(True)
                self.rotationActionSpinBox.setDisabled(True)
        if action == "navAction":
            if self.navAction.isChecked():
                self.navActionSlider.setDisabled(False)
                self.navActionSpinBox.setDisabled(False)
            else:
                self.navActionSlider.setDisabled(True)
                self.navActionSpinBox.setDisabled(True)
        if action == "sysAction":
            if self.sysAction.isChecked():
                self.sysActionSlider.setDisabled(False)
                self.sysActionSpinBox.setDisabled(False)
            else:
                self.sysActionSlider.setDisabled(True)
                self.sysActionSpinBox.setDisabled(True)
        if action == "appswitchAction":
            if self.appswitchAction.isChecked():
                self.appswitchActionSlider.setDisabled(False)
                self.appswitchActionSpinBox.setDisabled(False)
            else:
                self.appswitchActionSlider.setDisabled(True)
                self.appswitchActionSpinBox.setDisabled(True)
        if action == "flipAction":
            if self.flipAction.isChecked():
                self.flipActionSlider.setDisabled(False)
                self.flipActionSpinBox.setDisabled(False)
            else:
                self.flipActionSlider.setDisabled(True)
                self.flipActionSpinBox.setDisabled(True)
        if action == "otherAction":
            if self.otherAction.isChecked():
                self.otherActionSlider.setDisabled(False)
                self.otherActionSpinBox.setDisabled(False)
            else:
                self.otherActionSlider.setDisabled(True)
                self.otherActionSpinBox.setDisabled(True)

    # 设置monkey参数
    def setParameter(self, monkeyParameter):
        # 事件参数
        if self.touchAction.isChecked():
            self.touchActionParameter = "--pct-touch " + self.touchActionSpinBox.text()
            monkeyParameter = monkeyParameter + " " + self.touchActionParameter
        if self.trackballAction.isChecked():
            self.trackballActionParameter = "--pct-trackball " + self.trackballActionSpinBox.text()
            monkeyParameter = monkeyParameter + " " + self.trackballActionParameter
        if self.rotationAction.isChecked():
            self.rotationActionParameter = "--pct-rotation " + self.rotationActionSpinBox.text()
            monkeyParameter = monkeyParameter + " " + self.rotationActionParameter
        if self.navAction.isChecked():
            self.navActionParameter = "--pct-nav " + self.navActionSpinBox.text()
            monkeyParameter = monkeyParameter + " " + self.navActionParameter
        if self.sysAction.isChecked():
            self.sysActionParameter = "--pct-syskeys " + self.sysActionSpinBox.text()
            monkeyParameter = monkeyParameter + " " + self.sysActionParameter
        if self.appswitchAction.isChecked():
            self.appswitchActionParameter = "--pct-appswitch " + self.appswitchActionSpinBox.text()
            monkeyParameter = monkeyParameter + " " + self.appswitchActionParameter
        if self.flipAction.isChecked():
            self.flipActionActionParameter = "--pct-flip " + self.flipActionSpinBox.text()
            monkeyParameter = monkeyParameter + " " + self.flipActionActionParameter
        if self.otherAction.isChecked():
            self.otherActionParameter = "--pct-anyevent " + self.otherActionSpinBox.text()
            monkeyParameter = monkeyParameter + " " + self.otherActionParameter

        # 调试参数
        if self.ignoreCrashesCheckBox.isChecked():
            monkeyParameter = monkeyParameter + " " + "--ignore-crashes"
        if self.ignoreTimeoutsCheckBox.isChecked():
            monkeyParameter = monkeyParameter + " " + "--ignore-timeouts"
        if self.ignoreSecurityExceptionsCheckBox.isChecked():
            monkeyParameter = monkeyParameter + " " + "--ignore-security-exceptions"
        if self.monitorNativeCrashesCheckBox.isChecked():
            monkeyParameter = monkeyParameter + " " + "--monitor-native-crashes"

        # 必填参数
        if self.seedValueEdit.text() != "0":
            monkeyParameter = monkeyParameter + " " + "-s " + self.seedValueEdit.text()
        if self.throttleValueEdit.text() != "0":
            monkeyParameter = monkeyParameter + " --throttle " + self.throttleValueEdit.text()
        monkeyParameter = monkeyParameter + " -v -v -v " + self.countValueEdit.text()

        # monkeyParameter=monkeyParameter+" "+"-s "+self.seedValueEdit.text()+" --throttle "+self.throttleValueEdit.text()+" -v -v -v "+self.countValueEdit.text()
        print("monkeyParameter:" + monkeyParameter)
        return monkeyParameter

    # 初始化操作事件2视图
    def initOperateAction2(self):
        self.operateActionVbox2 = QtGui.QVBoxLayout()

        # 系统事件
        self.sysActionHbox = QtGui.QHBoxLayout()
        self.sysAction = QtGui.QCheckBox("系统")
        self.sysActionSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.sysActionSpinBox = QtGui.QSpinBox()
        self.sysActionSlider.setRange(0, 100)
        self.sysActionSpinBox.setRange(0, 100)
        self.sysActionSlider.setDisabled(True)
        self.sysActionSpinBox.setDisabled(True)
        self.sysActionHbox.addWidget(self.sysAction)
        self.sysActionHbox.addWidget(self.sysActionSlider)
        self.sysActionHbox.addWidget(self.sysActionSpinBox)

        QtCore.QObject.connect(self.sysActionSlider, QtCore.SIGNAL("valueChanged(int)"),
                               self.sysActionSpinBox,
                               QtCore.SLOT("setValue(int)"))
        QtCore.QObject.connect(self.sysActionSpinBox, QtCore.SIGNAL("valueChanged(int)"),
                               self.sysActionSlider,
                               QtCore.SLOT("setValue(int)"))

        # 切换事件
        self.appswitchActionHbox = QtGui.QHBoxLayout()
        self.appswitchAction = QtGui.QCheckBox("切换")
        self.appswitchActionSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.appswitchActionSpinBox = QtGui.QSpinBox()
        self.appswitchActionSlider.setRange(0, 100)
        self.appswitchActionSpinBox.setRange(0, 100)
        self.appswitchActionSlider.setDisabled(True)
        self.appswitchActionSpinBox.setDisabled(True)
        self.appswitchActionHbox.addWidget(self.appswitchAction)
        self.appswitchActionHbox.addWidget(self.appswitchActionSlider)
        self.appswitchActionHbox.addWidget(self.appswitchActionSpinBox)

        QtCore.QObject.connect(self.appswitchActionSlider, QtCore.SIGNAL("valueChanged(int)"),
                               self.appswitchActionSpinBox,
                               QtCore.SLOT("setValue(int)"))
        QtCore.QObject.connect(self.appswitchActionSpinBox, QtCore.SIGNAL("valueChanged(int)"),
                               self.appswitchActionSlider,
                               QtCore.SLOT("setValue(int)"))

        # 键盘事件
        self.flipActionHbox = QtGui.QHBoxLayout()
        self.flipAction = QtGui.QCheckBox("键盘")
        self.flipActionSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.flipActionSpinBox = QtGui.QSpinBox()
        self.flipActionSlider.setRange(0, 100)
        self.flipActionSpinBox.setRange(0, 100)
        self.flipActionSlider.setDisabled(True)
        self.flipActionSpinBox.setDisabled(True)
        self.flipActionHbox.addWidget(self.flipAction)
        self.flipActionHbox.addWidget(self.flipActionSlider)
        self.flipActionHbox.addWidget(self.flipActionSpinBox)

        QtCore.QObject.connect(self.flipActionSlider, QtCore.SIGNAL("valueChanged(int)"),
                               self.flipActionSpinBox,
                               QtCore.SLOT("setValue(int)"))
        QtCore.QObject.connect(self.flipActionSpinBox, QtCore.SIGNAL("valueChanged(int)"),
                               self.flipActionSlider,
                               QtCore.SLOT("setValue(int)"))

        # 其他事件
        self.otherActionHbox = QtGui.QHBoxLayout()
        self.otherAction = QtGui.QCheckBox("其他")
        self.otherActionSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.otherActionSpinBox = QtGui.QSpinBox()
        self.otherActionSlider.setRange(0, 100)
        self.otherActionSpinBox.setRange(0, 100)
        self.otherActionSlider.setDisabled(True)
        self.otherActionSpinBox.setDisabled(True)
        self.otherActionHbox.addWidget(self.otherAction)
        self.otherActionHbox.addWidget(self.otherActionSlider)
        self.otherActionHbox.addWidget(self.otherActionSpinBox)

        QtCore.QObject.connect(self.otherActionSlider, QtCore.SIGNAL("valueChanged(int)"),
                               self.otherActionSpinBox,
                               QtCore.SLOT("setValue(int)"))
        QtCore.QObject.connect(self.otherActionSpinBox, QtCore.SIGNAL("valueChanged(int)"),
                               self.otherActionSlider,
                               QtCore.SLOT("setValue(int)"))

        self.operateActionVbox2.addLayout(self.sysActionHbox)
        self.operateActionVbox2.addLayout(self.appswitchActionHbox)
        self.operateActionVbox2.addLayout(self.flipActionHbox)
        self.operateActionVbox2.addLayout(self.otherActionHbox)
        self.operateActionBox2.setLayout(self.operateActionVbox2)

        self.sysAction.clicked.connect(lambda: self.enableAction("sysAction"))
        self.appswitchAction.clicked.connect(lambda: self.enableAction("appswitchAction"))
        self.flipAction.clicked.connect(lambda: self.enableAction("flipAction"))
        self.otherAction.clicked.connect(lambda: self.enableAction("otherAction"))

    def initConsoleOutput(self):
        # 定义一个日志对话框
        self.logWidget = QtGui.QDialog()
        self.consoleOutputVbox = QtGui.QVBoxLayout()
        self.consoleOutputEdit = QtGui.QTextEdit()
        self.consoleOutputEdit.setStyleSheet("background: black")
        self.consoleOutputEdit.setTextColor(QtGui.QColor("green"))
        self.consoleOutputEdit.setFontPointSize(12)
        self.consoleOutputEdit.setReadOnly(True)
        self.consoleOutputVbox.addWidget(self.consoleOutputEdit)
        self.logWidget.setLayout(self.consoleOutputVbox)
        # 定义一个报告对话框
        self.reportWidget = QtGui.QDialog()
        self.reportWidgetVbox = QtGui.QVBoxLayout()
        self.reportTable = QtGui.QTableWidget(9, 3)
        self.reportTable.setColumnWidth(0, 300)
        self.reportTable.setHorizontalHeaderLabels(['异常类型', '数量', '备注'])
        self.reportWidgetVbox.addWidget(self.reportTable)
        # 装载一个空的表格，用来当做帮助使用，免得是一个空的表格
        self.printReport("", "")
        self.reportWidget.setLayout(self.reportWidgetVbox)
        # 定义一个TAB
        self.consoleWidget = QtGui.QTabWidget()
        self.consoleWidget.addTab(self.logWidget, u"日志")
        self.consoleWidget.addTab(self.reportWidget, u"报告")
        self.consoleOutputVbox = QtGui.QVBoxLayout()
        self.consoleOutputVbox.addWidget(self.consoleWidget)
        self.consoleGroupBox.setLayout(self.consoleOutputVbox)
