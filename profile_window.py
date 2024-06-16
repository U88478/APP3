# profile_window.py
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont
from sqlalchemy.orm import sessionmaker

from models import Stat, Game, engine

Session = sessionmaker(bind=engine)
session = Session()


class Ui_ProfileWindow(object):
    def __init__(self, user):
        self.user = user

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(20, 20, 150, 20))
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernameLabel.setFont(QFont('Arial', 14))

        self.gamesPlayedLabel = QtWidgets.QLabel(self.centralwidget)
        self.gamesPlayedLabel.setGeometry(QtCore.QRect(20, 60, 150, 20))
        self.gamesPlayedLabel.setObjectName("gamesPlayedLabel")
        self.gamesPlayedLabel.setFont(QFont('Arial', 14))

        self.bestScoreLabel = QtWidgets.QLabel(self.centralwidget)
        self.bestScoreLabel.setGeometry(QtCore.QRect(20, 100, 150, 20))
        self.bestScoreLabel.setObjectName("bestScoreLabel")
        self.bestScoreLabel.setFont(QFont('Arial', 14))

        self.highestScoreLabel = QtWidgets.QLabel(self.centralwidget)
        self.highestScoreLabel.setGeometry(QtCore.QRect(20, 140, 150, 20))
        self.highestScoreLabel.setObjectName("highestScoreLabel")
        self.highestScoreLabel.setFont(QFont('Arial', 14))

        self.lowestScoreLabel = QtWidgets.QLabel(self.centralwidget)
        self.lowestScoreLabel.setGeometry(QtCore.QRect(20, 180, 150, 20))
        self.lowestScoreLabel.setObjectName("lowestScoreLabel")
        self.lowestScoreLabel.setFont(QFont('Arial', 14))

        self.gamesPlayedValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.gamesPlayedValueLabel.setGeometry(QtCore.QRect(180, 60, 100, 20))
        self.gamesPlayedValueLabel.setObjectName("gamesPlayedValueLabel")
        self.gamesPlayedValueLabel.setFont(QFont('Arial', 14))

        self.bestScoreValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.bestScoreValueLabel.setGeometry(QtCore.QRect(180, 100, 100, 20))
        self.bestScoreValueLabel.setObjectName("bestScoreValueLabel")
        self.bestScoreValueLabel.setFont(QFont('Arial', 14))

        self.highestScoreValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.highestScoreValueLabel.setGeometry(QtCore.QRect(180, 140, 100, 20))
        self.highestScoreValueLabel.setObjectName("highestScoreValueLabel")
        self.highestScoreValueLabel.setFont(QFont('Arial', 14))

        self.lowestScoreValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.lowestScoreValueLabel.setGeometry(QtCore.QRect(180, 180, 100, 20))
        self.lowestScoreValueLabel.setObjectName("lowestScoreValueLabel")
        self.lowestScoreValueLabel.setFont(QFont('Arial', 14))

        self.gameHistoryLabel = QtWidgets.QLabel(self.centralwidget)
        self.gameHistoryLabel.setGeometry(QtCore.QRect(20, 220, 150, 20))
        self.gameHistoryLabel.setObjectName("gameHistoryLabel")
        self.gameHistoryLabel.setFont(QFont('Arial', 14))

        self.gameHistoryListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.gameHistoryListWidget.setGeometry(QtCore.QRect(20, 250, 560, 120))
        self.gameHistoryListWidget.setObjectName("gameHistoryListWidget")

        self.updateProfile()

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Profile"))
        self.usernameLabel.setText(_translate("MainWindow", f"Username: {self.user.username}"))
        self.gamesPlayedLabel.setText(_translate("MainWindow", "Games Played:"))
        self.bestScoreLabel.setText(_translate("MainWindow", "Best Score:"))
        self.highestScoreLabel.setText(_translate("MainWindow", "Highest Score:"))
        self.lowestScoreLabel.setText(_translate("MainWindow", "Lowest Score:"))
        self.gameHistoryLabel.setText(_translate("MainWindow", "Game History:"))

    def updateProfile(self):
        stats = session.query(Stat).filter_by(user_id=self.user.id).first()
        if stats:
            self.gamesPlayedValueLabel.setText(str(stats.games_played))
            self.bestScoreValueLabel.setText(f"{stats.best_score:.1f}")
            self.highestScoreValueLabel.setText(f"{stats.highest_score:.1f}")
            self.lowestScoreValueLabel.setText(f"{stats.lowest_score:.1f}")

        games = session.query(Game).filter_by(user_id=self.user.id).order_by(Game.id.desc()).all()
        self.gameHistoryListWidget.clear()
        for game in games:
            self.gameHistoryListWidget.addItem(f"Game ID: {game.id}, Score: {game.score}, Date: {game.date}")


if __name__ == "__main__":
    import sys
    from auth import login

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    user = login("your_test_username", "your_test_password")  # Replace with actual credentials
    if user:
        ui = Ui_ProfileWindow(user)
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    else:
        print("Invalid login credentials")
