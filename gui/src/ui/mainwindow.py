# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1005, 713)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/logo/logo_noback.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"#left_side QPushButton {\n"
"  background-color: transparent;\n"
"  border: none;\n"
"}\n"
"\n"
"#left_side QPushButton:hover {\n"
"  background-color: #F5F5F5;\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"#main_loginPage #login_page_widget{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#main_loginPage QLineEdit {\n"
"    border-radius: 6px;\n"
"    border: 2px solid rgb(67, 185, 181);\n"
"}\n"
"\n"
"#main_loginPage QPushButton {\n"
"    border-radius: 6px;\n"
"    border: 2px solid rgb(67, 185, 181);\n"
"    background-color:  rgb(67, 185, 181);\n"
"}\n"
"\n"
"#main_loginPage QPushButton:hover {\n"
"    border-radius: 6px;\n"
"    border: 2px solid rgb(54, 150, 145);\n"
"    background-color: rgb(54, 150, 145);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_loginPage = QtWidgets.QWidget()
        self.main_loginPage.setObjectName("main_loginPage")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.main_loginPage)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.main_loginPage)
        self.frame.setMaximumSize(QtCore.QSize(468, 415))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.loginStackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.loginStackedWidget.setStyleSheet("")
        self.loginStackedWidget.setObjectName("loginStackedWidget")
        self.login_page_widget = QtWidgets.QWidget()
        self.login_page_widget.setObjectName("login_page_widget")
        self.logoLabel = QtWidgets.QLabel(self.login_page_widget)
        self.logoLabel.setGeometry(QtCore.QRect(120, 40, 201, 111))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap(":/logo/logo/logo.jpeg"))
        self.logoLabel.setObjectName("logoLabel")
        self.input_email = QtWidgets.QLineEdit(self.login_page_widget)
        self.input_email.setGeometry(QtCore.QRect(110, 200, 221, 31))
        self.input_email.setObjectName("input_email")
        self.input_password = QtWidgets.QLineEdit(self.login_page_widget)
        self.input_password.setGeometry(QtCore.QRect(110, 250, 221, 31))
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.loginBtn = QtWidgets.QPushButton(self.login_page_widget)
        self.loginBtn.setGeometry(QtCore.QRect(110, 310, 221, 31))
        self.loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginBtn.setObjectName("loginBtn")
        self.registerBtn = QtWidgets.QPushButton(self.login_page_widget)
        self.registerBtn.setGeometry(QtCore.QRect(160, 350, 121, 23))
        self.registerBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerBtn.setStyleSheet("background-color: transparent;\n"
"border: none;")
        self.registerBtn.setObjectName("registerBtn")
        self.errorLabel = QtWidgets.QLabel(self.login_page_widget)
        self.errorLabel.setGeometry(QtCore.QRect(110, 180, 221, 16))
        self.errorLabel.setStyleSheet("color: red;")
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.loginStackedWidget.addWidget(self.login_page_widget)
        self.register_page_widget = QtWidgets.QWidget()
        self.register_page_widget.setObjectName("register_page_widget")
        self.createBtn = QtWidgets.QPushButton(self.register_page_widget)
        self.createBtn.setGeometry(QtCore.QRect(110, 330, 221, 31))
        self.createBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.createBtn.setObjectName("createBtn")
        self.alreadyloginBtn = QtWidgets.QPushButton(self.register_page_widget)
        self.alreadyloginBtn.setGeometry(QtCore.QRect(110, 370, 221, 23))
        self.alreadyloginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.alreadyloginBtn.setStyleSheet("background-color: transparent;\n"
"border: none;")
        self.alreadyloginBtn.setObjectName("alreadyloginBtn")
        self.input_email_register = QtWidgets.QLineEdit(self.register_page_widget)
        self.input_email_register.setGeometry(QtCore.QRect(110, 150, 221, 31))
        self.input_email_register.setObjectName("input_email_register")
        self.logoLabel_2 = QtWidgets.QLabel(self.register_page_widget)
        self.logoLabel_2.setGeometry(QtCore.QRect(120, 0, 201, 111))
        self.logoLabel_2.setText("")
        self.logoLabel_2.setPixmap(QtGui.QPixmap(":/logo/logo/logo.jpeg"))
        self.logoLabel_2.setObjectName("logoLabel_2")
        self.input_password_register = QtWidgets.QLineEdit(self.register_page_widget)
        self.input_password_register.setGeometry(QtCore.QRect(110, 230, 221, 31))
        self.input_password_register.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password_register.setObjectName("input_password_register")
        self.errorLabel_register = QtWidgets.QLabel(self.register_page_widget)
        self.errorLabel_register.setGeometry(QtCore.QRect(110, 128, 221, 16))
        self.errorLabel_register.setStyleSheet("")
        self.errorLabel_register.setText("")
        self.errorLabel_register.setObjectName("errorLabel_register")
        self.conf_password_register = QtWidgets.QLineEdit(self.register_page_widget)
        self.conf_password_register.setGeometry(QtCore.QRect(110, 270, 221, 31))
        self.conf_password_register.setEchoMode(QtWidgets.QLineEdit.Password)
        self.conf_password_register.setObjectName("conf_password_register")
        self.input_username_register = QtWidgets.QLineEdit(self.register_page_widget)
        self.input_username_register.setGeometry(QtCore.QRect(110, 190, 221, 31))
        self.input_username_register.setObjectName("input_username_register")
        self.loginStackedWidget.addWidget(self.register_page_widget)
        self.horizontalLayout_4.addWidget(self.loginStackedWidget)
        self.horizontalLayout_3.addWidget(self.frame)
        self.stackedWidget.addWidget(self.main_loginPage)
        self.main_mainPage = QtWidgets.QWidget()
        self.main_mainPage.setObjectName("main_mainPage")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_mainPage)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_side = QtWidgets.QFrame(self.main_mainPage)
        self.left_side.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_side.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_side.setObjectName("left_side")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left_side)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.left_side)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/logo/logo/logo_2.jpeg"))
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.main = QtWidgets.QFrame(self.left_side)
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.homeBtn = QtWidgets.QPushButton(self.main)
        self.homeBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QtCore.QSize(30, 30))
        self.homeBtn.setObjectName("homeBtn")
        self.verticalLayout.addWidget(self.homeBtn)
        self.toolsBtn = QtWidgets.QPushButton(self.main)
        self.toolsBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/grid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolsBtn.setIcon(icon2)
        self.toolsBtn.setIconSize(QtCore.QSize(30, 30))
        self.toolsBtn.setObjectName("toolsBtn")
        self.verticalLayout.addWidget(self.toolsBtn)
        self.settingsBtn = QtWidgets.QPushButton(self.main)
        self.settingsBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsBtn.setIcon(icon3)
        self.settingsBtn.setIconSize(QtCore.QSize(30, 30))
        self.settingsBtn.setObjectName("settingsBtn")
        self.verticalLayout.addWidget(self.settingsBtn)
        self.helpBtn = QtWidgets.QPushButton(self.main)
        self.helpBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpBtn.setIcon(icon4)
        self.helpBtn.setIconSize(QtCore.QSize(30, 30))
        self.helpBtn.setObjectName("helpBtn")
        self.verticalLayout.addWidget(self.helpBtn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.main)
        self.horizontalLayout_2.addWidget(self.left_side)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.main_mainPage)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget_2.addWidget(self.page_2)
        self.horizontalLayout_2.addWidget(self.stackedWidget_2)
        self.stackedWidget.addWidget(self.main_mainPage)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.loginStackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sonic Scholar"))
        self.input_email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.input_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.loginBtn.setText(_translate("MainWindow", "Login"))
        self.registerBtn.setText(_translate("MainWindow", "Create an account?"))
        self.createBtn.setText(_translate("MainWindow", "Create Account"))
        self.alreadyloginBtn.setText(_translate("MainWindow", "Already have an account? login"))
        self.input_email_register.setPlaceholderText(_translate("MainWindow", "Email"))
        self.input_password_register.setPlaceholderText(_translate("MainWindow", "Enter password"))
        self.conf_password_register.setPlaceholderText(_translate("MainWindow", "Confirm password"))
        self.input_username_register.setPlaceholderText(_translate("MainWindow", "Username"))
import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
