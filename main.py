import sys, sqlite3
from PyQt5 import uic, QtCore, QtGui, QtWidgets


class Coffee(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.base = sqlite3.connect("coffee.sqlite")
        self.cur = self.base.cursor()
        data = self.cur.execute("select * from coffee").fetchall()
        self.showing.setColumnCount(7)
        self.showing.setRowCount(len(data))
        for i, k in enumerate(["ID", "Сорт", "Степень обжарки(%)", "Вид", "Описание", "Цена", "Объём"]):
            self.showing.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(k))
        for i, j in enumerate(data):
            for k, l in enumerate(j):
                if type(l) == int or type(l) == float:
                    item = QtWidgets.QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, l)
                else:
                    item = QtWidgets.QTableWidgetItem(l)
                self.showing.setItem(i, k, item)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Coffee()
    w.show()
    sys.exit(app.exec())