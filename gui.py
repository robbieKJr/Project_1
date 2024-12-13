from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    """UI class for the main window"""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Bank")
        MainWindow.resize(800, 600)


        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(220, 20, 371, 501))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.ATM = QtWidgets.QLabel(parent=self.frame)
        self.ATM.setGeometry(QtCore.QRect(169, 30, 31, 20))
        self.ATM.setObjectName("ATM")

        self.first_name = QtWidgets.QLabel(parent=self.frame)
        self.first_name.setGeometry(QtCore.QRect(30, 80, 71, 16))
        self.first_name.setObjectName("first_name")

        self.last_name = QtWidgets.QLabel(parent=self.frame)
        self.last_name.setGeometry(QtCore.QRect(30, 110, 71, 16))
        self.last_name.setObjectName("last_name")

        self.enter_pin = QtWidgets.QLabel(parent=self.frame)
        self.enter_pin.setGeometry(QtCore.QRect(30, 140, 60, 16))
        self.enter_pin.setObjectName("enter_pin")

        self.first_box = QtWidgets.QTextEdit(parent=self.frame)
        self.first_box.setGeometry(QtCore.QRect(120, 80, 181, 21))
        self.first_box.setObjectName("first_box")

        self.last_box = QtWidgets.QTextEdit(parent=self.frame)
        self.last_box.setGeometry(QtCore.QRect(120, 110, 181, 21))
        self.last_box.setObjectName("last_box")

        self.decision = QtWidgets.QLabel(parent=self.frame)
        self.decision.setGeometry(QtCore.QRect(100, 240, 200, 15))
        self.decision.setText("What would you like to do?")
        self.decision.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.decision.setStyleSheet("font-size: 14px; color: black;")


        # Using QLineEdit for the pin box
        self.pin_box = QtWidgets.QLineEdit(parent=self.frame)
        self.pin_box.setGeometry(QtCore.QRect(120, 140, 181, 21))
        self.pin_box.setObjectName("pin_box")
        self.pin_box.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Mask input as dots

        self.deposit_button = QtWidgets.QRadioButton(parent=self.frame)
        self.deposit_button.setGeometry(QtCore.QRect(210, 270, 100, 20))
        self.deposit_button.setObjectName("deposit_button")

        self.withdraw_button = QtWidgets.QRadioButton(parent=self.frame)
        self.withdraw_button.setGeometry(QtCore.QRect(90, 270, 100, 20))
        self.withdraw_button.setObjectName("withdraw_button")

        self.amount = QtWidgets.QLabel(parent=self.frame)
        self.amount.setGeometry(QtCore.QRect(30, 330, 60, 16))
        self.amount.setObjectName("amount")

        self.amount_box = QtWidgets.QTextEdit(parent=self.frame)
        self.amount_box.setGeometry(QtCore.QRect(120, 330, 181, 21))
        self.amount_box.setObjectName("amount_box")

        self.enter_button = QtWidgets.QPushButton(parent=self.frame)
        self.enter_button.setGeometry(QtCore.QRect(40, 440, 113, 32))
        self.enter_button.setObjectName("enter_button")

        self.exit_button = QtWidgets.QPushButton(parent=self.frame)
        self.exit_button.setGeometry(QtCore.QRect(210, 440, 113, 32))
        self.exit_button.setObjectName("exit_button")

        self.search_button = QtWidgets.QPushButton(parent=self.frame)
        self.search_button.setGeometry(QtCore.QRect(140, 170, 113, 32))
        self.search_button.setObjectName("search_button")

        # Add QLabel for the welcome message
        self.welcome_message = QtWidgets.QLabel(parent=self.frame)
        self.welcome_message.setGeometry(QtCore.QRect(110, 220, 180, 14))
        self.welcome_message.setObjectName("welcome_message")
        self.welcome_message.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.welcome_message.setStyleSheet("font-size: 14px; color: black;")
        self.welcome_message.setText("")

        self.balance_message = QtWidgets.QLabel(parent=self.frame)
        self.balance_message.setGeometry(QtCore.QRect(30, 380, 271, 21))
        self.balance_message.setObjectName("balance_message")
        self.balance_message.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.balance_message.setStyleSheet("font-size: 14px; color: black;")



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.error_message = QtWidgets.QLabel(self.centralwidget)
        self.error_message.setGeometry(QtCore.QRect(200, 430, 400, 16))
        self.error_message.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.error_message.setStyleSheet("font-size: 14px; color: red;")
        self.error_message.setObjectName("error_message")
        self.error_message.setText("")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Bank", "Bank"))
        self.ATM.setText(_translate("Bank", "ATM"))
        self.first_name.setText(_translate("Bank", "First Name"))
        self.last_name.setText(_translate("Bank", "Last Name"))
        self.enter_pin.setText(_translate("Bank", "Enter Pin"))
        self.deposit_button.setText(_translate("Bank", "DEPOSIT"))
        self.withdraw_button.setText(_translate("Bank", "WITHDRAW"))
        self.amount.setText(_translate("Bank", "Amount"))
        self.enter_button.setText(_translate("Bank", "Enter"))
        self.exit_button.setText(_translate("Bank", "Exit"))
        self.search_button.setText(_translate("Bank", "SEARCH"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
