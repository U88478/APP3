# main_window.py
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont
from sqlalchemy.orm import sessionmaker

from game_logic import generate_data, play_game
from leaderboard_window import Ui_LeaderboardWindow
from models import engine, User, Stat
from profile_window import Ui_ProfileWindow
from sorting_algorithms import compare_sorting_algorithms

Session = sessionmaker(bind=engine)
session = Session()


class Ui_MainWindow(object):
    def __init__(self, user):
        self.main_window = None
        self.user = user

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_window = MainWindow

        self.welcomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLabel.setGeometry(QtCore.QRect(150, 10, 300, 40))
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.welcomeLabel.setFont(QFont('Arial', 20, QFont.Bold))
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.gamesPlayedLabel = QtWidgets.QLabel(self.centralwidget)
        self.gamesPlayedLabel.setGeometry(QtCore.QRect(20, 70, 150, 20))
        self.gamesPlayedLabel.setObjectName("gamesPlayedLabel")
        self.gamesPlayedLabel.setFont(QFont('Arial', 14))

        self.gamesPlayedValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.gamesPlayedValueLabel.setGeometry(QtCore.QRect(180, 70, 100, 20))
        self.gamesPlayedValueLabel.setObjectName("gamesPlayedValueLabel")
        self.gamesPlayedValueLabel.setFont(QFont('Arial', 14))

        self.globalAverageLabel = QtWidgets.QLabel(self.centralwidget)
        self.globalAverageLabel.setGeometry(QtCore.QRect(20, 100, 150, 20))
        self.globalAverageLabel.setObjectName("globalAverageLabel")
        self.globalAverageLabel.setFont(QFont('Arial', 14))

        self.globalAverageValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.globalAverageValueLabel.setGeometry(QtCore.QRect(180, 100, 100, 20))
        self.globalAverageValueLabel.setObjectName("globalAverageValueLabel")
        self.globalAverageValueLabel.setFont(QFont('Arial', 14))

        self.bestScoreLabel = QtWidgets.QLabel(self.centralwidget)
        self.bestScoreLabel.setGeometry(QtCore.QRect(20, 130, 150, 20))
        self.bestScoreLabel.setObjectName("bestScoreLabel")
        self.bestScoreLabel.setFont(QFont('Arial', 14))

        self.bestScoreValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.bestScoreValueLabel.setGeometry(QtCore.QRect(180, 130, 100, 20))
        self.bestScoreValueLabel.setObjectName("bestScoreValueLabel")
        self.bestScoreValueLabel.setFont(QFont('Arial', 14))

        self.averageLabel = QtWidgets.QLabel(self.centralwidget)
        self.averageLabel.setGeometry(QtCore.QRect(380, 70, 150, 20))
        self.averageLabel.setObjectName("averageLabel")
        self.averageLabel.setFont(QFont('Arial', 14))

        self.averageValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.averageValueLabel.setGeometry(QtCore.QRect(530, 70, 50, 20))
        self.averageValueLabel.setObjectName("averageValueLabel")
        self.averageValueLabel.setFont(QFont('Arial', 14))

        self.highestLabel = QtWidgets.QLabel(self.centralwidget)
        self.highestLabel.setGeometry(QtCore.QRect(380, 100, 150, 20))
        self.highestLabel.setObjectName("highestLabel")
        self.highestLabel.setFont(QFont('Arial', 14))

        self.highestValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.highestValueLabel.setGeometry(QtCore.QRect(530, 100, 50, 20))
        self.highestValueLabel.setObjectName("highestValueLabel")
        self.highestValueLabel.setFont(QFont('Arial', 14))

        self.lowestLabel = QtWidgets.QLabel(self.centralwidget)
        self.lowestLabel.setGeometry(QtCore.QRect(380, 130, 150, 20))
        self.lowestLabel.setObjectName("lowestLabel")
        self.lowestLabel.setFont(QFont('Arial', 14))

        self.lowestValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.lowestValueLabel.setGeometry(QtCore.QRect(530, 130, 50, 20))
        self.lowestValueLabel.setObjectName("lowestValueLabel")
        self.lowestValueLabel.setFont(QFont('Arial', 14))

        self.rolledNumbersLabel = QtWidgets.QLabel(self.centralwidget)
        self.rolledNumbersLabel.setGeometry(QtCore.QRect(20, 200, 560, 20))
        self.rolledNumbersLabel.setObjectName("rolledNumbersLabel")
        self.rolledNumbersLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rolledNumbersLabel.setFont(QFont('Arial', 12))

        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(250, 230, 100, 40))
        self.playButton.setObjectName("playButton")
        self.playButton.setFont(QFont('Arial', 14, QFont.Bold))

        self.profileButton = QtWidgets.QPushButton(self.centralwidget)
        self.profileButton.setGeometry(QtCore.QRect(20, 230, 100, 40))
        self.profileButton.setObjectName("profileButton")
        self.profileButton.setFont(QFont('Arial', 12))
        self.profileButton.setText("Profile")

        self.logoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logoutButton.setGeometry(QtCore.QRect(20, 10, 50, 20))
        self.logoutButton.setObjectName("logoutButton")
        self.logoutButton.setFont(QFont('Arial', 8))
        self.logoutButton.setText("Log out")

        self.leaderboardButton = QtWidgets.QPushButton(self.centralwidget)
        self.leaderboardButton.setGeometry(QtCore.QRect(480, 230, 100, 40))
        self.leaderboardButton.setObjectName("leaderboardButton")
        self.leaderboardButton.setFont(QFont('Arial', 12))
        self.leaderboardButton.setText("Leaderboard")

        # Admin Panel
        if self.user.is_admin:
            self.adminPanelLabel = QtWidgets.QLabel(self.centralwidget)
            self.adminPanelLabel.setGeometry(QtCore.QRect(150, 290, 300, 20))
            self.adminPanelLabel.setObjectName("adminPanelLabel")
            self.adminPanelLabel.setFont(QFont('Arial', 16, QFont.Bold))
            self.adminPanelLabel.setAlignment(QtCore.Qt.AlignCenter)

            self.recordCountSpinBox = QtWidgets.QSpinBox(self.centralwidget)
            self.recordCountSpinBox.setGeometry(QtCore.QRect(20, 320, 100, 40))
            self.recordCountSpinBox.setMinimum(1)
            self.recordCountSpinBox.setMaximum(10000)
            self.recordCountSpinBox.setValue(100)
            self.recordCountSpinBox.setObjectName("recordCountSpinBox")
            self.recordCountSpinBox.setFont(QFont('Arial', 12))

            self.generateDataButton = QtWidgets.QPushButton(self.centralwidget)
            self.generateDataButton.setGeometry(QtCore.QRect(130, 320, 150, 40))
            self.generateDataButton.setObjectName("generateDataButton")
            self.generateDataButton.setFont(QFont('Arial', 12))

            self.compareSortButton = QtWidgets.QPushButton(self.centralwidget)
            self.compareSortButton.setGeometry(QtCore.QRect(290, 320, 150, 40))
            self.compareSortButton.setObjectName("compareSortButton")
            self.compareSortButton.setFont(QFont('Arial', 12))

            self.clearDataButton = QtWidgets.QPushButton(self.centralwidget)
            self.clearDataButton.setGeometry(QtCore.QRect(450, 320, 150, 40))
            self.clearDataButton.setObjectName("clearDataButton")
            self.clearDataButton.setFont(QFont('Arial', 12))

            self.generateDataButton.clicked.connect(self.generateData)
            self.compareSortButton.clicked.connect(self.compareSorting)
            self.clearDataButton.clicked.connect(self.clearGeneratedData)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuOverview = QtWidgets.QMenu(self.menuBar)
        self.menuOverview.setObjectName("menuOverview")
        self.menuProfile = QtWidgets.QMenu(self.menuBar)
        self.menuProfile.setObjectName("menuProfile")
        self.menuLeaderboard = QtWidgets.QMenu(self.menuBar)
        self.menuLeaderboard.setObjectName("menuLeaderboard")
        self.menuAdmin = QtWidgets.QMenu(self.menuBar)
        self.menuAdmin.setObjectName("menuAdmin")
        MainWindow.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menuOverview.menuAction())
        self.menuBar.addAction(self.menuProfile.menuAction())
        self.menuBar.addAction(self.menuLeaderboard.menuAction())
        self.menuBar.addAction(self.menuAdmin.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.updateLabels()
        self.playButton.clicked.connect(self.playGame)
        self.profileButton.clicked.connect(self.openProfile)
        self.logoutButton.clicked.connect(self.logOut)
        self.leaderboardButton.clicked.connect(self.openLeaderboard)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Window"))
        self.welcomeLabel.setText(_translate("MainWindow", f"Welcome, {self.user.username}"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.averageLabel.setText(_translate("MainWindow", "Average:"))
        self.highestLabel.setText(_translate("MainWindow", "Highest:"))
        self.lowestLabel.setText(_translate("MainWindow", "Lowest:"))
        self.gamesPlayedLabel.setText(_translate("MainWindow", "Games Played:"))
        self.globalAverageLabel.setText(_translate("MainWindow", "Global Average:"))
        self.bestScoreLabel.setText(_translate("MainWindow", "Best Score:"))
        if self.user.is_admin:
            self.adminPanelLabel.setText(_translate("MainWindow", "Admin Panel"))
            self.generateDataButton.setText(_translate("MainWindow", "Generate Data"))
            self.compareSortButton.setText(_translate("MainWindow", "Compare Sort"))
            self.clearDataButton.setText(_translate("MainWindow", "Clear Data"))
            self.leaderboardButton.setText(_translate("MainWindow", "Leaderboard"))

    def updateLabels(self):
        try:
            stats = session.query(Stat).filter_by(user_id=self.user.id).first()
            if stats:
                self.gamesPlayedValueLabel.setText(str(stats.games_played))
                self.globalAverageValueLabel.setText(f"{stats.average_score:.1f} (#{self.get_global_ranking()})")
                self.bestScoreValueLabel.setText(f"{stats.best_score:.1f}")
                self.averageValueLabel.setText(f"{stats.average_score:.1f}")
                self.highestValueLabel.setText(f"{stats.highest_score:.1f}")
                self.lowestValueLabel.setText(f"{stats.lowest_score:.1f}")
        except AttributeError as e:
            QtWidgets.QMessageBox.warning(None, 'Error', f'Error updating labels: {str(e)}')
        except Exception as e:
            QtWidgets.QMessageBox.warning(None, 'Error', f'Unexpected error updating labels: {str(e)}')

    def get_global_ranking(self):
        try:
            all_stats = session.query(Stat).order_by(Stat.average_score.desc()).all()
            for index, stat in enumerate(all_stats, start=1):
                if stat.user_id == self.user.id:
                    return index
            return "N/A"
        except Exception as e:
            QtWidgets.QMessageBox.warning(None, 'Error', f'Error fetching global ranking: {str(e)}')
            return "N/A"

    def playGame(self):
        try:
            rolled_numbers, average_score, global_ranking = play_game(self.user.id)
            self.rolledNumbersLabel.setText("Rolled Numbers: " + ", ".join(map(str, rolled_numbers)))
            self.updateLabels()
        except AttributeError as e:
            QtWidgets.QMessageBox.warning(None, 'Error', f'Error playing game: {str(e)}')
        except Exception as e:
            QtWidgets.QMessageBox.warning(None, 'Error', f'Unexpected error playing game: {str(e)}')

    def generateData(self):
        try:
            record_count = self.recordCountSpinBox.value()
            generate_data(record_count)
            QtWidgets.QMessageBox.information(None, 'Success', f'{record_count} records generated successfully.')
        except Exception as e:
            QtWidgets.QMessageBox.warning(None, 'Error', f'Error generating data: {str(e)}')

    def clearGeneratedData(self):
        try:
            session.query(Stat).filter(
                Stat.user_id.in_(session.query(User.id).filter(User.username.like('user_%')))).delete(
                synchronize_session='fetch')
            session.query(User).filter(User.username.like('user_%')).delete(synchronize_session='fetch')
            session.commit()
            QtWidgets.QMessageBox.information(None, 'Success', 'Generated data cleared successfully.')
        except Exception as e:
            QtWidgets.QMessageBox.warning(None, 'Error', f'Error clearing data: {str(e)}')

    def compareSorting(self):
        compare_sorting_algorithms()

    def openLeaderboard(self):
        try:
            self.leaderboard_window = QtWidgets.QMainWindow()
            self.ui = Ui_LeaderboardWindow()
            self.ui.setupUi(self.leaderboard_window)
            self.leaderboard_window.show()
        except Exception as e:
            print(e)

    def openProfile(self):
        self.profile_window = QtWidgets.QMainWindow()
        self.ui = Ui_ProfileWindow(self.user)
        self.ui.setupUi(self.profile_window)
        self.profile_window.show()

    def logOut(self):
        try:
            # Close the main window
            self.main_window.close()

            from login_window import Ui_LoginWindow

            # Create a new login window
            self.login_window = QtWidgets.QMainWindow()
            self.ui = Ui_LoginWindow()
            self.ui.setupUi(self.login_window)
            self.ui.main_window = self.login_window
            self.login_window.show()
        except Exception as e:
            print(e)

    if __name__ == "__main__":
        import sys

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
