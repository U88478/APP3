# sign_up_window.py
from PyQt5 import QtCore, QtWidgets

from auth import register


class Ui_SignUpWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(347, 250)
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
        self.adminCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.adminCheckBox.setGeometry(QtCore.QRect(130, 120, 113, 20))
        self.adminCheckBox.setObjectName("adminCheckBox")
        self.termsCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.termsCheckBox.setGeometry(QtCore.QRect(130, 150, 113, 20))
        self.termsCheckBox.setObjectName("termsCheckBox")
        self.signupButton = QtWidgets.QPushButton(self.centralwidget)
        self.signupButton.setGeometry(QtCore.QRect(145, 180, 75, 23))
        self.signupButton.setObjectName("signupButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.signupButton.clicked.connect(self.handle_signup)
        self.main_window = MainWindow  # Reference to main window

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sign Up"))
        self.usernameLabel.setText(_translate("MainWindow", "Username"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.adminCheckBox.setText(_translate("MainWindow", "Admin"))
        self.termsCheckBox.setText(_translate("MainWindow", "Accept Terms"))
        self.signupButton.setText(_translate("MainWindow", "Sign up"))

    def handle_signup(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        is_admin = self.adminCheckBox.isChecked()
        accept_terms = self.termsCheckBox.isChecked()
        if not accept_terms:
            QtWidgets.QMessageBox.warning(None, 'Error', 'You must accept the terms to sign up.')
            return
        try:
            register(username, password, is_admin)
            QtWidgets.QMessageBox.information(None, 'Success', 'Account created successfully')
            self.main_window.close()  # Close the sign-up window
        except ValueError as e:
            QtWidgets.QMessageBox.warning(None, 'Error', str(e))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_SignUpWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
