# leaderboard_window.py
from PyQt5 import QtCore, QtWidgets
from sqlalchemy.orm import sessionmaker

from models import Stat, User, engine

Session = sessionmaker(bind=engine)
session = Session()


class Ui_LeaderboardWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(335, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 320, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Username", "Average Score", "Games Played"])

        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(130, 330, 100, 30))
        self.refreshButton.setObjectName("refreshButton")
        self.refreshButton.setText("Refresh")
        self.refreshButton.clicked.connect(self.loadLeaderboardData)

        self.loadLeaderboardData()

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Leaderboard"))

    def loadLeaderboardData(self):
        try:
            stats = session.query(Stat).join(User).order_by(Stat.average_score.desc()).limit(100).all()
            self.tableWidget.setRowCount(len(stats))
            for row_idx, stat in enumerate(stats):
                self.tableWidget.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(stat.user.username))
                self.tableWidget.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(f"{stat.average_score:.1f}"))
                self.tableWidget.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(str(stat.games_played)))
        except Exception as e:
            QtWidgets.QMessageBox.warning(None, 'Error', f'Error loading leaderboard data: {str(e)}')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LeaderboardWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
