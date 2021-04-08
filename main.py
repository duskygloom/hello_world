from PyQt5.QtWidgets import \
	QApplication as qapp, \
	QMainWindow  as qwin, \
    QShortcut    as qsho

from PyQt5.QtGui     import \
    QKeySequence as qkes

from interface import interface


if __name__ == "__main__":
    import sys
    app = qapp(sys.argv)
    window = qwin()
    ui = interface(window)
    ui.setup_win()

    # quit shortcut
    quit_shortcut = qsho(qkes("Ctrl+Q"), window)
    quit_shortcut.activated.connect(lambda: app.exit())
    
    window.show()
    sys.exit(app.exec_())
