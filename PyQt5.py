import sys
from PyQt5.QtWidgets import QApplication, QWidget
a = input('Введите имя виджета: ')
b = int(input('Введите ширину: '))
c = int(input('Введите длину: '))
if __name__ == "__main__":
    app = QApplication(sys.argv)
w = QWidget()
w.resize(b, c)
w.setWindowTitle(a)
w.show()
sys.exit(app.exec_())
