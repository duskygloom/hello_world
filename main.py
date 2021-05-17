#! /usr/bin/python3


from PyQt5.QtWidgets import \
	QApplication as qapp, \
	QMainWindow  as qwin, \
    QShortcut    as qsho

from PyQt5.QtGui     import \
    QKeySequence  as qkes, \
    QFontDatabase as qfdb

from interface import interface
from database  import islogged


if __name__ == "__main__":
    import sys
    app = qapp(sys.argv)
    qfdb.addApplicationFont("resources/josefinfont.ttf")
    window = qwin()    
    ui = interface(window)

    if islogged():
        ui.setup_home()
    else:
        ui.setup_start()

    # quit shortcut
    quit_shortcut = qsho(qkes("Ctrl+Q"), window)
    quit_shortcut.activated.connect(lambda: app.exit())
    
    window.show()
    sys.exit(app.exec_())
