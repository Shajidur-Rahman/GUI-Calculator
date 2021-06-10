from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(200, 40, 301, 41))

        font = QtGui.QFont()
        font.setPointSize(20)

        self.header.setFont(font)
        self.header.setObjectName("header")

        # cal
        self.cal = QtWidgets.QTextEdit(self.centralwidget, plainText='')
        self.cal.setGeometry(QtCore.QRect(10, 90, 611, 81))
        self.cal.setObjectName("cal")


        #seven
        self.seven = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: seven())
        self.seven.setGeometry(QtCore.QRect(30, 180, 141, 71))
        self.seven.setObjectName("seven")
        # function of seven
        def seven():
            # self.cal.setPlainText("7")
            seven = self.cal.toPlainText() + '7'
            self.cal.setPlainText(seven)



        # eight
        self.eight = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: eight())
        self.eight.setGeometry(QtCore.QRect(250, 180, 141, 71))
        self.eight.setObjectName("eight")
        # function of eight
        def eight():
            # self.cal.setPlainText("8")
            eight = self.cal.toPlainText() + '8'
            self.cal.setPlainText(eight)


        # nine
        self.nine = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: nine())
        self.nine.setGeometry(QtCore.QRect(460, 180, 131, 71))
        self.nine.setObjectName("nine")
        # function of nine
        def nine():
            nine = self.cal.toPlainText() + '9'
            self.cal.setPlainText(nine)


        # four
        self.four = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: four())
        self.four.setGeometry(QtCore.QRect(30, 260, 141, 71))
        self.four.setObjectName("four")
        #function of four
        def four():
            four = self.cal.toPlainText() + '4'
            self.cal.setPlainText(four)


        #five
        self.five = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: five())
        self.five.setGeometry(QtCore.QRect(250, 270, 141, 71))
        self.five.setObjectName("five")
        # function of five
        def five():
            five = self.cal.toPlainText() + '5'
            self.cal.setPlainText(five)


        # six
        self.six = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: six())
        self.six.setGeometry(QtCore.QRect(460, 270, 131, 71))
        self.six.setObjectName("six")
        # function of six
        def six():
            six = self.cal.toPlainText() + '6'
            self.cal.setPlainText(six)


        # one
        self.one = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: one())
        self.one.setGeometry(QtCore.QRect(30, 360, 141, 71))
        self.one.setObjectName("one")
        # function of one
        def one():
            one = self.cal.toPlainText() + '1'
            self.cal.setPlainText(one)


        # two
        self.two = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: two())
        self.two.setGeometry(QtCore.QRect(250, 360, 141, 71))
        self.two.setObjectName("two")
        # function of two
        def two():
            two = self.cal.toPlainText() + '2'
            self.cal.setPlainText(two)


        # zero
        self.zero = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: zero())
        self.zero.setGeometry(QtCore.QRect(460, 360, 131, 71))
        self.zero.setObjectName("zero")
        # function of zero
        def zero():
            zero = self.cal.toPlainText() + '0'
            self.cal.setPlainText(zero)


        # plus
        self.plus = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: plus())
        self.plus.setGeometry(QtCore.QRect(30, 440, 61, 41))
        self.plus.setObjectName("plus")
        # the function of plus
        def plus():
            plus = self.cal.toPlainText() + '+'
            self.cal.setPlainText(plus)


        # negetive
        self.nege = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: nege())
        self.nege.setGeometry(QtCore.QRect(110, 440, 61, 41))
        self.nege.setObjectName("nege")
        # function of negetive
        def nege():
            nege = self.cal.toPlainText() + '-'
            self.cal.setPlainText(nege)


        # mul
        self.mul = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: mul())
        self.mul.setGeometry(QtCore.QRect(30, 490, 61, 41))
        self.mul.setObjectName("mul")
        # function of multiplication
        def mul():
            mul = self.cal.toPlainText() + '*'
            self.cal.setPlainText(mul)

        # divition
        self.divi = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: divi())
        self.divi.setGeometry(QtCore.QRect(110, 490, 61, 41))
        self.divi.setObjectName("divi")
        # function of divition
        def divi():
            divi = self.cal.toPlainText() + '/'
            self.cal.setPlainText(divi)


        # clear
        self.clear = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: clear())
        self.clear.setGeometry(QtCore.QRect(250, 440, 361, 61))
        self.clear.setObjectName("clear")
        # function of clear
        def clear():
            self.cal.setPlainText('')


        # equal
        self.equal = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: equal())
        self.equal.setGeometry(QtCore.QRect(250, 510, 361, 41))
        self.equal.setObjectName("equal")
        # function of equal


        def equal():
            # self.header.setText(f'{self.cal.toPlainText().split()}')
            text = self.cal.toPlainText()
            if '+' in text:
                text = text.split('+')
                self.cal.setPlainText(f"{float(text[0]) + float(text[-1])}")
            elif '-' in text:
                text = text.split('-')
                self.cal.setPlainText(f"{float(text[0]) - float(text[-1])}")
            elif '*' in text:
                text = text.split('*')
                self.cal.setPlainText(f"{float(text[0]) * float(text[-1])}")
            elif '/' in text:
                text = text.split('/')
                self.cal.setPlainText(f"{float(text[0]) / float(text[-1])}")
            elif '%' in text:
                text = text.split('%')
                self.cal.setPlainText(f"{float(text[0]) % float(text[-1])}")
                


        # reminder
        self.remainder = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: reminder())
        self.remainder.setGeometry(QtCore.QRect(30, 540, 141, 21))
        self.remainder.setObjectName("remainder")
        # function of reminder
        def reminder():
            reminder = self.cal.toPlainText() + '%'
            self.cal.setPlainText(reminder)



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My calculator"))
        self.header.setText(_translate("MainWindow", "My calculator"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.four.setText(_translate("MainWindow", "4"))
        self.five.setText(_translate("MainWindow", "5"))
        self.six.setText(_translate("MainWindow", "6"))
        self.one.setText(_translate("MainWindow", "1"))
        self.two.setText(_translate("MainWindow", "2"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.nege.setText(_translate("MainWindow", "-"))
        self.mul.setText(_translate("MainWindow", "*"))
        self.divi.setText(_translate("MainWindow", "/"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.equal.setText(_translate("MainWindow", "="))
        self.remainder.setText(_translate("MainWindow", "%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
