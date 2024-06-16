# admin_panel.py
from PyQt5 import QtCore, QtWidgets
from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()


class Ui_AdminPanel(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 580, 350))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["User ID", "Username", "Admin"])

        self.loadUserData()

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Admin Panel"))

    def loadUserData(self):
        users = session.query(User).all()
        self.tableWidget.setRowCount(len(users))
        for row_idx, user in enumerate(users):
            self.tableWidget.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(str(user.id)))
            self.tableWidget.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(user.username))
            self.tableWidget.setItem(row_idx, 2, QtWidgets.QTableWidgetItem("Yes" if user.is_admin else "No"))


if __name__ == "__main__":
    import sys
    from auth import login

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    user = login("ad", "ad")
    if user and user.is_admin:
        ui = Ui_AdminPanel()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    else:
        print("Invalid admin credentials or not an admin")
