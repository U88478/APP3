from PyQt5 import QtCore, QtWidgets
from pycallgraph2 import PyCallGraph, Config
from pycallgraph2.globbing_filter import GlobbingFilter
from pycallgraph2.output import GraphvizOutput

from auth import login
from main_window import Ui_MainWindow
from sign_up_window import Ui_SignUpWindow


class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(347, 206)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.usernameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameLineEdit.setGeometry(QtCore.QRect(130, 50, 113, 20))
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.passwordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setGeometry(QtCore.QRect(130, 90, 113, 20))
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(70, 59, 47, 13))
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(70, 99, 47, 13))
        self.passwordLabel.setObjectName("passwordLabel")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(145, 140, 75, 23))
        self.loginButton.setObjectName("loginButton")
        self.signupButton = QtWidgets.QPushButton(self.centralwidget)
        self.signupButton.setGeometry(QtCore.QRect(60, 140, 75, 23))
        self.signupButton.setObjectName("signupButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.loginButton.clicked.connect(self.handle_login)
        self.signupButton.clicked.connect(self.handle_signup)
        self.main_window = None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.usernameLabel.setText(_translate("MainWindow", "Username"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.loginButton.setText(_translate("MainWindow", "Log in"))
        self.signupButton.setText(_translate("MainWindow", "Sign up"))

    def handle_login(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        user = login(username, password)
        if user:
            self.openMainWindow(user)
            self.main_window.close()
        else:
            QtWidgets.QMessageBox.warning(None, 'Error', 'Invalid username or password')

    def handle_signup(self):
        self.signup_window = QtWidgets.QMainWindow()
        self.ui = Ui_SignUpWindow()
        self.ui.setupUi(self.signup_window)
        self.signup_window.show()

    def openMainWindow(self, user):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(user)
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys

    config = Config()
    config.trace_filter = GlobbingFilter(include=[
        'login_window.*',
        'main_window.*',
        'profile_window.*',
        'leaderboard_window.*',
        'game_logic.*',
        'models.*',
        'sorting_algorithms.*',
        'themes.*',
    ])

    graphviz = GraphvizOutput()
    graphviz.output_file = 'call_graph.png'

    with PyCallGraph(output=graphviz, config=config):
        app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QMainWindow()
        ui = Ui_LoginWindow()
        ui.setupUi(main_window)
        ui.main_window = main_window
        main_window.show()
        sys.exit(app.exec_())
