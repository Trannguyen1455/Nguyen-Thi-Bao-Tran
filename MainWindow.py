# Form implementation generated from reading ui file 'D:\Phương Nghi\UEL\TDLT\HelloWorld\Bai130\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 807)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 721, 741))
        self.groupBox.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(170, 20, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditGiaMuaMoi = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditGiaMuaMoi.setGeometry(QtCore.QRect(260, 80, 251, 21))
        self.lineEditGiaMuaMoi.setObjectName("lineEditGiaMuaMoi")
        self.lineEditPhiVanChuyen = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditPhiVanChuyen.setGeometry(QtCore.QRect(260, 110, 251, 21))
        self.lineEditPhiVanChuyen.setObjectName("lineEditPhiVanChuyen")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEditPhiLapDat = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditPhiLapDat.setGeometry(QtCore.QRect(260, 140, 251, 21))
        self.lineEditPhiLapDat.setObjectName("lineEditPhiLapDat")
        self.lineEditSoNamSuDungDuKien = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditSoNamSuDungDuKien.setGeometry(QtCore.QRect(260, 170, 251, 21))
        self.lineEditSoNamSuDungDuKien.setObjectName("lineEditSoNamSuDungDuKien")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButtonTinhKhauHao = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonTinhKhauHao.setGeometry(QtCore.QRect(260, 210, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonTinhKhauHao.setFont(font)
        self.pushButtonTinhKhauHao.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButtonTinhKhauHao.setObjectName("pushButtonTinhKhauHao")
        self.lineEditNguyenGiaTSCD = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditNguyenGiaTSCD.setGeometry(QtCore.QRect(260, 280, 251, 21))
        self.lineEditNguyenGiaTSCD.setObjectName("lineEditNguyenGiaTSCD")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 280, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEditMucTrichKhauHaoNam = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditMucTrichKhauHaoNam.setGeometry(QtCore.QRect(260, 320, 251, 21))
        self.lineEditMucTrichKhauHaoNam.setObjectName("lineEditMucTrichKhauHaoNam")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 320, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEditMucTrichKhauHaoThang = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditMucTrichKhauHaoThang.setGeometry(QtCore.QRect(260, 360, 251, 21))
        self.lineEditMucTrichKhauHaoThang.setObjectName("lineEditMucTrichKhauHaoThang")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 360, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButtonXemChiTietKhauHao = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonXemChiTietKhauHao.setGeometry(QtCore.QRect(20, 410, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonXemChiTietKhauHao.setFont(font)
        self.pushButtonXemChiTietKhauHao.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButtonXemChiTietKhauHao.setObjectName("pushButtonXemChiTietKhauHao")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(20, 460, 551, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Phuong Nghi_K234111403"))
        self.label.setText(_translate("MainWindow", "Chương Trình Tính Khấu Hao TSCD"))
        self.label_2.setText(_translate("MainWindow", "Giá Mua Mới:"))
        self.label_3.setText(_translate("MainWindow", "Phí vận chuyển:"))
        self.label_4.setText(_translate("MainWindow", "Phí lắp đặt"))
        self.label_5.setText(_translate("MainWindow", "Số năm sử dụng dự kiến:"))
        self.pushButtonTinhKhauHao.setText(_translate("MainWindow", "1. Tính Khấu Hao"))
        self.label_6.setText(_translate("MainWindow", "Nguyên giá TSCD:"))
        self.label_7.setText(_translate("MainWindow", "Mức trích khấu hao năm:"))
        self.label_8.setText(_translate("MainWindow", "Mức trích khấu hao tháng:"))
        self.pushButtonXemChiTietKhauHao.setText(_translate("MainWindow", "2. Xem chi tiết Khấu Hao"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Năm"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Sau khấu hao còn =>"))