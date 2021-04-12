from PyQt5.QtWidgets import \
    QPushButton as qpbt, \
    QMainWindow as qwin

from PyQt5.QtGui     import \
    QCursor as qcur

from PyQt5.QtCore    import \
    Qt as qt


# variables
button_pointer = qcur(qt.PointingHandCursor)


class button(qpbt):
    '''\
self.title : button title
self.function : button function'''
    
    def __init__(self, window: qwin):
        super().__init__()
        self.window   = window
        self.button   = qpbt(window)
        self.title    = "button"
        self.function = lambda: print("hello_world")

    def setup(self):
        self.button.setText(self.title)
        self.button.clicked.connect(self.function)
        self.button.setCursor(button_pointer)
        self.button.setStyleSheet('''\
background-color: rgb(255, 100, 125);
color: black;
border-radius: 25;''')