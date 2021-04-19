from PyQt5.QtWidgets import \
    QMainWindow as qwin, \
    QPushButton as qpbt, \
    QLabel as qlab, \
    QFrame as qfra

from PyQt5.QtGui import \
    QIcon as qico

from PyQt5.QtCore import \
    Qt as qt, \
    QSize as qsiz


# variables

hand = qt.PointingHandCursor
top  = qt.AlignTop


class body_button(qpbt):
	
	def __init__(self, window: qwin):
		super().__init__(window)
		self.setCursor(hand)
		self.setStyleSheet('''\
QPushButton::hover
{
	background-color: rgb(255, 255, 255);
}
QPushButton
{
	background-color: rgb(255, 100, 125);
	color: black;
	border-radius: 25;
	border-style: none;
	padding-top: 0;
	padding-left: 0;
	padding-right: 0;
}''')


class popup(qlab):

	def __init__(self, window: qwin):
		super().__init__(window)
		self.window = window
		self.setGeometry(300, 200, 600, 400)
		self.setWordWrap(True)
		self.setAlignment(top)
		self.setStyleSheet('''\
border-style: solid;
border-width: 5;
border-radius: 20;
border-color: rgb(255, 100, 125);
background-color: rgba(33, 33, 33, 200);
padding-top: 10;
padding-left: 10;
padding-right: 110;''')
		# yes button
		self.yes = body_button(self)
		self.yes.setGeometry(475, 150, 150, 50)
		self.yes.setText("yes  ")
		# no button
		self.no = body_button(self)
		self.no.setGeometry(475, 250, 150, 50)
		self.no.setText("no   ")
		self.setVisible(False)


class top_button(qpbt):

	def __init__(self, window: qwin):
		super().__init__(window)
		self.setCursor(hand)
		self.setStyleSheet('''\
QPushButton::hover
{
	font-weight: 700;
	color: rgb(255, 100, 125);
}
QPushButton
{
border-style: none;
background-color: rgba(33, 33, 33, 0);
}''')


class panel(qfra):

	def __init__(self, window: qwin):
		super().__init__(window)
		self.setStyleSheet('''\
background-color: rgba(200, 100, 100, 200);
border-radius: 20;''')

		# icons
		self.up   = qico("resources/up.svg")
		self.down = qico("resources/down.svg")

		# title
		self.label = qlab(self)
		self.label.setGeometry(20, 15, 300, 50)
		self.label.setStyleSheet('''\
border-radius: 0;
background-color: rgba(0, 0, 0, 0);
font: 40pt;
font-weight: 700;''')

		# button
		self.button = qpbt(self)
		self.button.setGeometry(1040, 15, 100, 50)
		self.button.setIcon(self.up)
		self.button.setIconSize(qsiz(50, 50))
		self.button.setCursor(hand)
		self.button.clicked.connect(self.pull_up)
		self.button.setStyleSheet('''\
QPushButton::hover
{
	color: white;
}
QPushButton
{
	background-color: rgba(0, 0, 0, 0);
	color: black;
}''')

	# pull up function
	def pull_up(self):
		self.setGeometry(25, 80, 1150, 700)
		self.button.setIcon(self.down)
		self.button.setIconSize(qsiz(50, 50))
		self.button.clicked.connect(self.pull_down)


class message_panel(panel):

	def __init__(self, window: qwin):
		super().__init__(window)
		self.setGeometry(25, 600, 1150, 700)
		self.label.setText("message")

	# pull down function
	def pull_down(self):
		self.setGeometry(25, 600, 1150, 700)
		self.button.setIcon(self.up)
		self.button.setIconSize(qsiz(50, 50))
		self.button.clicked.connect(self.pull_up)


class updates_panel(panel):

	def __init__(self, window: qwin):
		super().__init__(window)
		self.setGeometry(25, 700, 1150, 750)
		self.label.setText("updates")

	# pull down function
	def pull_down(self):
		self.setGeometry(25, 700, 1150, 750)
		self.button.setIcon(self.up)
		self.button.setIconSize(qsiz(50, 50))
		self.button.clicked.connect(self.pull_up)


class card(qfra):

    def __init__(self, window: qwin):
        super().__init__(window)
        self.setGeometry(20, 120, 800, 640)
        self.setStyleSheet('''\
background-color: rgba(220, 163, 163, 100);
border-radius: 20;''')
        self.bottom_panel = qfra(self)
        self.bottom_panel.setGeometry(10, 580, 780, 50)
        self.bottom_panel.setStyleSheet('''
border-radius: 20;
border-style: solid;
border-color: rgb(33, 33, 33);
border-width: 2;
background-color: rgba(33, 33, 33, 50);''')
