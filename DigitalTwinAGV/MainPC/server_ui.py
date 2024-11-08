from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import time
import traceback, sys
import os


parent_dir=os.getcwd()
#Server
class Server(QThread):
    '''
    Worker thread
    '''
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Server started")
        sys.path.append(parent_dir)
        import server
        server.recieve()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(987, 563)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(144, 144, 144);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.logs_window = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.logs_window.setFont(font)
        self.logs_window.setStyleSheet("color: rgb(4, 4, 4);\n"
"border-color: rgb(8, 8, 8);\n"
"background-color: rgb(255, 255, 255);")
        self.logs_window.setFrameShape(QtWidgets.QFrame.Box)
        self.logs_window.setLineWidth(2)
        self.logs_window.setMidLineWidth(2)

        # Logs Window
        self.logs_window.setObjectName("logs_window")
        self.gridLayout.addWidget(self.logs_window, 3, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(8, 8, 8);\n"
"border-color: rgb(6, 6, 6);\n"
"background-color: rgb(92, 190, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(50)
        self.label.setMidLineWidth(17)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        # Object Name Lable : Server User Interface
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 15, -1, 15)
        self.verticalLayout.setSpacing(60)
        self.verticalLayout.setObjectName("verticalLayout")
        self.server_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)

        # Buttons

        #Server Button
        font.setWeight(75)
        self.server_button.setFont(font)
        self.server_button.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.server_button.setObjectName("server_button")
        #Mapping of Server Line Edit inputs for port and IP Address to Initialize button
        self.server_button.clicked.connect(self.server_initialization)
        self.verticalLayout.addWidget(self.server_button)
        self.Platform = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)

        # Platform
        font.setWeight(75)
        font.setKerning(False)
        self.Platform.setFont(font)
        self.Platform.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Platform.setObjectName("Platform")
        # Mapping of Platform button to platform_click function
        self.Platform.clicked.connect(self.platform_click)
        self.verticalLayout.addWidget(self.Platform)
        self.gridLayout.addLayout(self.verticalLayout, 2, 2, 1, 1)
        self.server_frame = QtWidgets.QFrame(self.centralwidget)
        self.server_frame.setAutoFillBackground(False)
        self.server_frame.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.server_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.server_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.server_frame.setLineWidth(1)

        # Server Frame
        self.server_frame.setObjectName("server_frame")
        self.layoutWidget = QtWidgets.QWidget(self.server_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 80, 531, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 1, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.IP_Address = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)

        # Server IP Address
        font.setWeight(75)
        self.IP_Address.setFont(font)
        self.IP_Address.setObjectName("IP_Address")
        self.horizontalLayout.addWidget(self.IP_Address)
        self.lineEdit_server_ip = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_server_ip.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_server_ip.setObjectName("lineEdit_server_ip")
        self.horizontalLayout.addWidget(self.lineEdit_server_ip)
        self.layoutWidget1 = QtWidgets.QWidget(self.server_frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(80, 20, 531, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Port_No = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)

        # Server Port Number
        font.setWeight(75)
        self.Port_No.setFont(font)
        self.Port_No.setObjectName("Port_No")
        self.horizontalLayout_2.addWidget(self.Port_No)
        self.lineEdit_server_port = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_server_port.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_server_port.setObjectName("lineEdit_server_port")
        self.horizontalLayout_2.addWidget(self.lineEdit_server_port)
        self.gridLayout.addWidget(self.server_frame, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 987, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionApplication_and_Service = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.actionApplication_and_Service.setFont(font)
        self.actionApplication_and_Service.setObjectName("actionApplication_and_Service")
        self.actionO_M = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.actionO_M.setFont(font)
        self.actionO_M.setObjectName("actionO_M")
        self.Install = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.Install.setFont(font)
        self.Install.setObjectName("Install")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logs_window.setText(_translate("MainWindow", "Logs Window"))
        self.label.setText(_translate("MainWindow", "Server UI"))
        self.server_button.setText(_translate("MainWindow", "Activate Server"))
        self.Platform.setText(_translate("MainWindow", "Platform"))
        self.IP_Address.setText(_translate("MainWindow", "IP Address : "))
        self.Port_No.setText(_translate("MainWindow", "Port No. : "))
        self.actionApplication_and_Service.setText(_translate("MainWindow", "Application and Service"))
        self.actionO_M.setText(_translate("MainWindow", "Operation and Maintenance"))
        self.Install.setText(_translate("MainWindow", "Install"))

    # # Methods to execute functionalities in interface
    def platform_click(self):
        # Write the functionalities that need to be executed here after pressing platform button
        self.logs_window.setText("Platform is launched")
        from project_platform import test
        
    def server_initialization(self):
        # Provide Server Port Number and IP Address here
        port=self.lineEdit_server_port.text()
        ip_add=self.lineEdit_server_ip.text()
        self.logs_window.setText("Port No. for Server Initialization is : "+port+" and IP Address is : "+ip_add)
        with open(r'server_ip.txt', 'w') as f:
            line1 = port+"\n"
            line2 = ip_add
            f.writelines([line1, line2])
        self.worker = Server()
        self.worker.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
