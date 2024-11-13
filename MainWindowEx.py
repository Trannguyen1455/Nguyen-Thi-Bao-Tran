
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QMessageBox
from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        self.pushButtonTinhKhauHao.clicked.connect(self.calculate_depreciation)
        self.pushButtonXemChiTietKhauHao.clicked.connect(self.show_detailed_depreciation)

        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)

    def calculate_depreciation(self):
        try:
            # Get input values
            purchase_price = float(self.lineEditGiaMuaMoi.text())
            shipping_cost = float(self.lineEditPhiVanChuyen.text())
            installation_cost = float(self.lineEditPhiLapDat.text())
            years_of_use = int(self.lineEditSoNamSuDungDuKien.text())

            # Calculate total cost (nguyên giá TSCD)
            total_cost = purchase_price + shipping_cost + installation_cost
            self.lineEditNguyenGiaTSCD.setText(f"{total_cost:.2f}")

            # Calculate yearly and monthly depreciation
            yearly_depreciation = total_cost / years_of_use
            monthly_depreciation = yearly_depreciation / 12

            self.lineEditMucTrichKhauHaoNam.setText(f"{yearly_depreciation:.2f}")
            self.lineEditMucTrichKhauHaoThang.setText(f"{monthly_depreciation:.2f}")

            QMessageBox.information(self.MainWindow, "Success", "Depreciation calculated successfully!")
        except ValueError:
            QMessageBox.warning(self.MainWindow, "Input Error", "Please enter valid numeric values in all fields.")
        except ZeroDivisionError:
            QMessageBox.warning(self.MainWindow, "Input Error", "Years of use cannot be zero.")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", f"An unexpected error occurred: {str(e)}")

    def show_detailed_depreciation(self):
        try:
            total_cost = float(self.lineEditNguyenGiaTSCD.text())
            yearly_depreciation = float(self.lineEditMucTrichKhauHaoNam.text())
            years_of_use = int(self.lineEditSoNamSuDungDuKien.text())

            # Clear existing rows
            self.tableWidget.setRowCount(0)

            remaining_value = total_cost
            for year in range(1, years_of_use + 1):
                remaining_value -= yearly_depreciation
                self.tableWidget.insertRow(year - 1)
                self.tableWidget.setItem(year - 1, 0, QtWidgets.QTableWidgetItem(str(year)))
                self.tableWidget.setItem(year - 1, 1, QtWidgets.QTableWidgetItem(f"{max(remaining_value, 0):.2f}"))

            QMessageBox.information(self.MainWindow, "Success", "Detailed depreciation table updated!")
        except ValueError:
            QMessageBox.warning(self.MainWindow, "Input Error", "Please calculate depreciation first.")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", f"An unexpected error occurred: {str(e)}")

    def showWindow(self):
        self.MainWindow.show()