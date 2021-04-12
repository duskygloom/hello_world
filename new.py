from PyQt5.QtWidgets import \
    QApplication as qapp, \
    QMainWindow  as qwin, \
    QLabel       as qlab

import sys


def resize():
    global window
    x = window.width()
    y = window.height()
    label.setGeometry(x - 100, y - 20, 100, 20)
    label.setText(f"geometry: {x}x{y}")
    label.adjustSize()


app = qapp(sys.argv)

window = qwin()
window.setGeometry(100, 100, 500, 500)
window.resizeEvent(resize)

label = qlab(window)

window.show()

sys.exit(app.exec_())
