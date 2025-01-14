# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Product.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(424, 401)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 91, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelID = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelID.setObjectName("labelID")
        self.verticalLayout.addWidget(self.labelID)
        self.labelBarkode = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelBarkode.setObjectName("labelBarkode")
        self.verticalLayout.addWidget(self.labelBarkode)
        self.labelNama = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelNama.setObjectName("labelNama")
        self.verticalLayout.addWidget(self.labelNama)
        self.labelKategori = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelKategori.setObjectName("labelKategori")
        self.verticalLayout.addWidget(self.labelKategori)
        self.labelQty = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelQty.setObjectName("labelQty")
        self.verticalLayout.addWidget(self.labelQty)
        self.labelHarga = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelHarga.setObjectName("labelHarga")
        self.verticalLayout.addWidget(self.labelHarga)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(110, 20, 160, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditID = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditID.setObjectName("lineEditID")
        self.verticalLayout_2.addWidget(self.lineEditID)
        self.lineEditBarkode = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditBarkode.setObjectName("lineEditBarkode")
        self.verticalLayout_2.addWidget(self.lineEditBarkode)
        self.lineEditNama = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditNama.setObjectName("lineEditNama")
        self.verticalLayout_2.addWidget(self.lineEditNama)
        self.lineEditKategori = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditKategori.setObjectName("lineEditKategori")
        self.verticalLayout_2.addWidget(self.lineEditKategori)
        self.lineEditQty = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditQty.setObjectName("lineEditQty")
        self.verticalLayout_2.addWidget(self.lineEditQty)
        self.lineEditHarga = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditHarga.setObjectName("lineEditHarga")
        self.verticalLayout_2.addWidget(self.lineEditHarga)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 190, 251, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonTambahkan = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonTambahkan.setObjectName("pushButtonTambahkan")
        self.horizontalLayout.addWidget(self.pushButtonTambahkan)
        self.pushButtonHapus = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonHapus.setObjectName("pushButtonHapus")
        self.horizontalLayout.addWidget(self.pushButtonHapus)
        self.pushButtonUbah = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonUbah.setObjectName("pushButtonUbah")
        self.horizontalLayout.addWidget(self.pushButtonUbah)
        self.pushButtonLoad = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonLoad.setObjectName("pushButtonLoad")
        self.horizontalLayout.addWidget(self.pushButtonLoad)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 220, 451, 131))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 360, 221, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButtonSearch = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.horizontalLayout_3.addWidget(self.pushButtonSearch)
        self.lineEditSearch = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.horizontalLayout_3.addWidget(self.lineEditSearch)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButtonTambahkan.clicked.connect(self.insertproduct)
        self.pushButtonHapus.clicked.connect(self.hapusproduct)
        self.pushButtonUbah.clicked.connect(self.ubahproduct)
        self.pushButtonLoad.clicked.connect(self.loadproduct)
        self.pushButtonSearch.clicked.connect(self.searchproduct)
        self.tableWidget.cellClicked.connect(self.on_table_item_clicked)

    def koneksi_db(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="dbpenjualan"
            )
            return mydb
        except mc.Error as e:
            QMessageBox.critical(None, "Database Error", f"Koneksi ke database gagal: {e}")
            return None

    def insertproduct(self):
        try:
            mydb = self.koneksi_db()
            if not mydb:
                return
            cursor = mydb.cursor()
            sql = "INSERT INTO product (id, barkode, name, kategori, qty, harga) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (
                self.lineEditID.text(),
                self.lineEditBarkode.text(),
                self.lineEditNama.text(),
                self.lineEditKategori.text(),
                self.lineEditQty.text(),
                self.lineEditHarga.text()
            )
            cursor.execute(sql, val)
            mydb.commit()
            QMessageBox.information(None, "Success", "Data product berhasil ditambahkan")
            self.clear_form()
            self.loadproduct()
        except mc.Error as e:
            QMessageBox.critical(None, "Error", f"Gagal menambahkan data: {e}")

    def loadproduct(self):
        try:
            mydb = self.koneksi_db()
            if not mydb:
                return
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM product")
            result = cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except mc.Error as e:
            QMessageBox.critical(None, "Error", f"Gagal memuat data: {e}")

    def hapusproduct(self):
        try:
            selected_row = self.tableWidget.currentRow()
            if selected_row == -1:
                QMessageBox.warning(None, "Warning", "Pilih baris yang ingin dihapus")
                return
            npm = self.tableWidget.item(selected_row, 0).text()
            mydb = self.koneksi_db()
            if not mydb:
                return
            cursor = mydb.cursor()
            sql = "DELETE FROM product WHERE id = %s"
            cursor.execute(sql, (npm,))
            mydb.commit()
            QMessageBox.information(None, "Success", "Data mahasiswa berhasil dihapus")
            self.loadproduct()
        except mc.Error as e:
            QMessageBox.critical(None, "Error", f"Gagal menghapus data: {e}")

    def ubahproduct(self):
        try:
            selected_row = self.tableWidget.currentRow()
            if selected_row == -1:
                QMessageBox.warning(None, "Warning", "Pilih baris yang ingin diubah")
                return
            npm = self.tableWidget.item(selected_row, 0).text()
            mydb = self.koneksi_db()
            if not mydb:
                return
            cursor = mydb.cursor()
            sql = "UPDATE product SET barkode = %s, name = %s, kategori = %s, qty = %s, harga = %s WHERE id = %s"
            val = (
                self.lineEditBarkode.text(),
                self.lineEditNama.text(),
                self.lineEditKategori.text(),
                self.lineEditQty.text(),
                self.lineEditHarga.text(),
                npm
            )
            cursor.execute(sql, val)
            mydb.commit()
            QMessageBox.information(None, "Success", "Data product berhasil diubah")
            self.clear_form()
            self.loadproduct()
        except mc.Error as e:
            QMessageBox.critical(None, "Error", f"Gagal mengubah data: {e}")

    def searchproduct(self):
        try:
            keyword = self.lineEditSearch.text()
            mydb = self.koneksi_db()
            if not mydb:
                return
            cursor = mydb.cursor()
            sql = "SELECT * FROM product WHERE id LIKE %s"
            cursor.execute(sql, (f"%{keyword}%",))
            result = cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except mc.Error as e:
            QMessageBox.critical(None, "Error", f"Gagal mencari data: {e}")

    def on_table_item_clicked(self, row, column):
        try:
            # Ambil data dari tabel berdasarkan baris yang diklik
            id = self.tableWidget.item(row, 0).text()
            barkode = self.tableWidget.item(row, 1).text()
            nama = self.tableWidget.item(row, 2).text()
            kategori = self.tableWidget.item(row, 3).text()
            qty = self.tableWidget.item(row, 4).text()
            harga = self.tableWidget.item(row, 5).text()

            # Isi form input dengan data yang diambil
            self.lineEditID.setText(id)
            self.lineEditBarkode.setText(barkode)
            self.lineEditNama.setText(nama)
            self.lineEditKategori.setText(kategori)
            self.lineEditQty.setText(qty)
            self.lineEditHarga.setText(harga)
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Gagal memuat data ke form: {e}")


    def clear_form(self):
        self.lineEditID.clear()
        self.lineEditBarkode.clear()
        self.lineEditNama.clear()
        self.lineEditKategori.clear()
        self.lineEditQty.clear()
        self.lineEditHarga.clear()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelID.setText(_translate("Form", "ID"))
        self.labelBarkode.setText(_translate("Form", "Barkode"))
        self.labelNama.setText(_translate("Form", "Nama"))
        self.labelKategori.setText(_translate("Form", "Kategori"))
        self.labelQty.setText(_translate("Form", "Qty"))
        self.labelHarga.setText(_translate("Form", "Harga"))
        self.pushButtonTambahkan.setText(_translate("Form", "Tambahkan"))
        self.pushButtonHapus.setText(_translate("Form", "Hapus"))
        self.pushButtonUbah.setText(_translate("Form", "Ubah"))
        self.pushButtonLoad.setText(_translate("Form", "Load"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Barkode"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Nama"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Kategori"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Qty"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Harga"))
        self.pushButtonSearch.setText(_translate("Form", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
