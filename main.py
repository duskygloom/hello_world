from PyQt5.QtWidgets import \
	QApplication as qapp, \
	QMainWindow  as qwin

from interface import interface

if __name__ == "__main__":
    import sys
    app = qapp(sys.argv)
    window = qwin()
    ui = interface(window)
    ui.setup_win()
    window.show()
    sys.exit(app.exec_())
