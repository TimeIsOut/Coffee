import sys, sqlite3
from PyQt5 import uic, QtCore, QtGui, QtWidgets


class AddEdit(QtWidgets.QMainWindow):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.id = ""
        uic.loadUi("addEditCoffeeForm.ui", self)
        if self.num == 1:
            self.setWindowTitle("Добавить кофе")
            self.save.setText("Добавить")
        else:
            self.setWindowTitle("Изменить кофе")
            self.save.setText("Изменить")
        self.save.clicked.connect(self.close)

    def closeEvent(self, event):
        if self.num == 1:
            d = w.cur.execute("select * from coffee").fetchall()
            data = (len(d) + 1, self.name.text(), self.percent.text(), self.type.text(),
                    self.desc.text(), self.price.text(), self.volume.text())
            w.showing.insertRow(len(d))
            for i, j in enumerate(data):
                if type(j) == int or type(j) == float:
                    item = QtWidgets.QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, j)
                else:
                    item = QtWidgets.QTableWidgetItem(j)
                w.showing.setItem(len(d), i, item)
            w.cur.execute(f"insert into coffee (id, name, percent, beans, desc, price, volume) values {data}")
            w.base.commit()
        else:
            data = [self.name.text(), self.percent.text(), self.type.text(), self.desc.text(), self.price.text(),
                    self.volume.text()]
            for i, j in enumerate(data):
                if type(j) == int or type(j) == float:
                    item = QtWidgets.QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, j)
                else:
                    item = QtWidgets.QTableWidgetItem(j)
                w.showing.setItem(0, i + 1, item)
            w.cur.execute(f"update coffee set name='{self.name.text()}' where id={self.id}")
            w.cur.execute(f"update coffee set percent={self.percent.text()} where id={self.id}")
            w.cur.execute(f"update coffee set beans='{self.type.text()}' where id={self.id}")
            w.cur.execute(f"update coffee set desc='{self.desc.text()}' where id={self.id}")
            w.cur.execute(f"update coffee set price={self.price.text()} where id={self.id}")
            w.cur.execute(f"update coffee set volume={self.volume.text()} where id={self.id}")
            w.base.commit()


class Coffee(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.f1 = AddEdit(1)
        self.f2 = AddEdit(2)
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
        self.add.clicked.connect(self.go)
        self.edit.clicked.connect(self.go)

    def go(self):
        if self.sender() == self.add:
            self.f1.show()
        else:
            if self.showing.currentRow() == -1:
                self.error.setText("Не выбрано!")
            else:
                self.error.setText("")
                d = self.showing.currentRow()
                self.f2.id = d + 1
                self.f2.name.setText(self.showing.item(d, 1).text())
                self.f2.percent.setText(self.showing.item(d, 2).text())
                self.f2.type.setText(self.showing.item(d, 3).text())
                self.f2.desc.setText(self.showing.item(d, 4).text())
                self.f2.price.setText(self.showing.item(d, 5).text())
                self.f2.volume.setText(self.showing.item(d, 6).text())
                self.f2.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Coffee()
    w.show()
    sys.exit(app.exec())