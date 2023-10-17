from PySide6.QtCore import (QCoreApplication,QMetaObject,QRect, QSize, Qt)
from PySide6.QtWidgets import (QComboBox, QFrame, QHBoxLayout,QLabel,QPushButton, QSizePolicy,QSpacerItem, QVBoxLayout, QWidget)
from logicks import logics

class Ui_MainWindow(object):
    log = logics()
    info = []
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1121, 853)
        MainWindow.setMinimumSize(QSize(1000, 700))
        MainWindow.setMaximumSize(QSize(1100, 900))
        MainWindow.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0.98595, y1:0.028, x2:0, y2:1, stop:0.0348259 rgba(0, 0, 0, 224), stop:1 rgba(238, 140, 218, 255))")
        MainWindow.setIconSize(QSize(33, 30))
        MainWindow.setAnimated(False)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1120, 853))
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color:rgb(255, 255, 255, 0) ;\n"
"font: 87 9pt Arial Black;\n"
"border: 0px \n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(350, 100, 381, 101))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color:rgb(255, 255, 255, 150) ;\n"
"font: 87 9pt Arial Black;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"border-radius: 5px")

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.layoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"background-color:rgb(255, 255, 255, 150) ;\n"
"font: 87 9pt Arial Black;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"border-radius: 5px")

        self.horizontalLayout_4.addWidget(self.comboBox_2)

        self.comboBox_3 = QComboBox(self.layoutWidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setStyleSheet(u"background-color:rgb(255, 255, 255, 150) ;\n"
"font: 87 9pt Arial Black;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"border-radius: 5px")

        self.horizontalLayout_4.addWidget(self.comboBox_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color:rgba(255, 255, 255, 150);\n"
"border: 1px solid rgba(255,255,255,30);\n"
"border-radius: 5px;\n"
"font: 87 9pt Arial Black\n"
"}\n"
"\n"
"QPushButton:pressed{ \n"
" background-color:rgba(255, 255, 255, 30) ;\n"
"}")
        self.pushButton.setChecked(True)
        self.pushButton.clicked.connect(self.button_click)# button--------------

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 10, 93, 28))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background-color:rgba(255, 255, 255, 150);\n"
"border: 1px solid rgba(255,255,255,30);\n"
"border-radius: 5px;\n"
"font: 87 9pt Arial Black\n"
"}\n"
"\n"
"QPushButton:pressed{ \n"
" background-color:rgba(255, 255, 255, 30) ;\n"
"}")
        self.pushButton_2.setCheckable(True)
        # self.pushButton_2.clicked.connect()
        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(1500, 1500))
        self.frame.setStyleSheet(u"background-color:rgba(255, 255, 255, 150) ;\n"
"font: 87 9pt Arial Black;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"border-radius: 5px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SITE = QLabel(self.frame)
        self.SITE.setObjectName(u"SITE")
        self.SITE.setMaximumSize(QSize(16777215, 50))
        self.SITE.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.SITE)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.AVAILABLE1 = QLabel(self.frame)
        self.AVAILABLE1.setObjectName(u"AVAILABLE1")
        self.AVAILABLE1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.AVAILABLE1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.FIAT_1 = QLabel(self.frame)
        self.FIAT_1.setObjectName(u"FIAT_1")
        self.FIAT_1.setMaximumSize(QSize(100, 100))
        self.FIAT_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.FIAT_1)

        self.ARROW = QLabel(self.frame)
        self.ARROW.setObjectName(u"ARROW")
        self.ARROW.setMaximumSize(QSize(100, 100))
        self.ARROW.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.ARROW)

        self.FIAT_2 = QLabel(self.frame)
        self.FIAT_2.setObjectName(u"FIAT_2")
        self.FIAT_2.setMaximumSize(QSize(100, 100))
        self.FIAT_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.FIAT_2)

        self.PRICE = QLabel(self.frame)
        self.PRICE.setObjectName(u"PRICE")
        self.PRICE.setMaximumSize(QSize(100, 100))
        self.PRICE.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.PRICE)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.MIN_LIMIT_1 = QLabel(self.frame)
        self.MIN_LIMIT_1.setObjectName(u"MIN_LIMIT_1")
        self.MIN_LIMIT_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.MIN_LIMIT_1)

        self.MAX_LIMIT_1 = QLabel(self.frame)
        self.MAX_LIMIT_1.setObjectName(u"MAX_LIMIT_1")
        self.MAX_LIMIT_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.MAX_LIMIT_1)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.AVAILABLE2 = QLabel(self.frame)
        self.AVAILABLE2.setObjectName(u"AVAILABLE2")
        self.AVAILABLE2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.AVAILABLE2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.FIAT_21 = QLabel(self.frame)
        self.FIAT_21.setObjectName(u"FIAT_21")
        self.FIAT_21.setMaximumSize(QSize(100, 100))
        self.FIAT_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.FIAT_21)

        self.ARROW2 = QLabel(self.frame)
        self.ARROW2.setObjectName(u"ARROW2")
        self.ARROW2.setMaximumSize(QSize(100, 100))
        self.ARROW2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.ARROW2)

        self.FIAT_11 = QLabel(self.frame)
        self.FIAT_11.setObjectName(u"FIAT_11")
        self.FIAT_11.setMaximumSize(QSize(100, 100))
        self.FIAT_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.FIAT_11)

        self.PRICE_2 = QLabel(self.frame)
        self.PRICE_2.setObjectName(u"PRICE_2")
        self.PRICE_2.setMaximumSize(QSize(100, 100))
        self.PRICE_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.PRICE_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.MIN_LIMIT_2 = QLabel(self.frame)
        self.MIN_LIMIT_2.setObjectName(u"MIN_LIMIT_2")
        self.MIN_LIMIT_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.MIN_LIMIT_2)

        self.MAX_LIMIT_2 = QLabel(self.frame)
        self.MAX_LIMIT_2.setObjectName(u"MAX_LIMIT_2")
        self.MAX_LIMIT_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.MAX_LIMIT_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_6)

        self.SPRED = QLabel(self.frame)
        self.SPRED.setObjectName(u"SPRED")
        self.SPRED.setMaximumSize(QSize(200, 200))
        self.SPRED.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.SPRED)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 50))
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_17)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(u"\ud83d\udc31 Harley")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0421\u0415", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"GBP", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"USD", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"CZK", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0421\u0415", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Revolut", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Wise", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"QIWI", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Юmoney", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0421\u0415", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"BINANCE", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"BYBIT", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"KUKOIN", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0411\u041d\u041e\u0412\u0418\u0422\u042c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0421\u0422\u041e\u0420\u0418\u042f", None))

        self.SITE.setText(QCoreApplication.translate("MainWindow", u"SITE", None))
        self.AVAILABLE1.setText(QCoreApplication.translate("MainWindow", u"AVAILABLE", None))
        self.FIAT_1.setText(QCoreApplication.translate("MainWindow", u"FIAT(1)", None))
        self.ARROW.setText(QCoreApplication.translate("MainWindow", u"\u279c", None))
        self.FIAT_2.setText(QCoreApplication.translate("MainWindow", u"FIAT(2)", None))
        self.PRICE.setText(QCoreApplication.translate("MainWindow", u"PRICE", None))
        self.MIN_LIMIT_1.setText(QCoreApplication.translate("MainWindow", u"MIN LIMIT", None))
        self.MAX_LIMIT_1.setText(QCoreApplication.translate("MainWindow", u"MAX LIMIT", None))
        self.AVAILABLE2.setText(QCoreApplication.translate("MainWindow", u"AVAILABLE", None))
        self.FIAT_21.setText(QCoreApplication.translate("MainWindow", u"FIAT(2)", None))
        self.ARROW2.setText(QCoreApplication.translate("MainWindow", u"\u279c", None))
        self.FIAT_11.setText(QCoreApplication.translate("MainWindow", u"FIAT(1)", None))
        self.PRICE_2.setText(QCoreApplication.translate("MainWindow", u"PRICE", None))
        self.MIN_LIMIT_2.setText(QCoreApplication.translate("MainWindow", u"MIN LIMIT", None))
        self.MAX_LIMIT_2.setText(QCoreApplication.translate("MainWindow", u"MAX LIMIT", None))
        self.SPRED.setText(QCoreApplication.translate("MainWindow", u"SPRED", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"WALLET", None))
    # retranslateUi

    def button_click(self):
        try:
            self.info.clear()
            self.info.append(self.log.reload(fiat=self.comboBox.currentText(), wallet=self.comboBox_2.currentText(), site=self.comboBox_3.currentText()))

            self.SPRED.setText(str(self.info[0][0]))

            self.FIAT_1.setText(str(self.info[0][1][0][1]))
            self.FIAT_2.setText(str(self.info[0][1][0][2]))
            self.PRICE.setText(str(self.info[0][1][0][3]))
            self.MIN_LIMIT_1.setText(str(self.info[0][1][0][5]))
            self.MAX_LIMIT_1.setText(str(self.info[0][1][0][6]))
            self.AVAILABLE1.setText(str(self.info[0][1][0][4]))

            self.FIAT_21.setText(str(self.info[0][1][1][2]))
            self.FIAT_11.setText(str(self.info[0][1][1][1]))
            self.PRICE_2.setText(str(self.info[0][1][1][3]))
            self.MIN_LIMIT_2.setText(str(self.info[0][1][1][5]))
            self.MAX_LIMIT_2.setText(str(self.info[0][1][1][6]))
            self.AVAILABLE2.setText(str(self.info[0][1][1][4]))

            self.SITE.setText(str(self.info[0][1][2]))
            self.label_17.setText(str(str(self.info[0][1][3])))
        except TypeError:
            self.SITE.setText("Такого индекса нет проверьте вводимые данные")