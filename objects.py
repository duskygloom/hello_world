from PyQt5.QtWidgets import \
    QMainWindow as qwin, \
    QPushButton as qpbt, \
    QLabel as qlab, \
    QFrame as qfra

from PyQt5.QtGui import \
    QIcon   as qico, \
	QPixmap as qpix

from PyQt5.QtCore import \
    Qt as qt, \
    QSize as qsiz


# variables

hand = qt.PointingHandCursor
top  = qt.AlignTop
keepratio = qt.KeepAspectRatio


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
		self.qss_sheet = '''\
QPushButton::hover
{
	font-weight: 700;
	color: rgb(255, 100, 125);
}
QPushButton
{
border-style: none;
background-color: rgba(33, 33, 33, 0);
border-radius: 20;
}'''
		self.setStyleSheet(self.qss_sheet)

	def isselected(self, status: bool):
		if status:
			self.setStyleSheet('''\
QPushButton::hover
{
	font-weight: 700;
	color: rgb(255, 100, 125);
}
QPushButton
{
border-style: none;
background-color: rgba(127, 33, 128, 100);
border-radius: 20;
}''')
		else:
			self.setStyleSheet(self.qss_sheet)


class panel(qfra):

	def __init__(self, window: qwin):
		super().__init__(window)
		self.main_qss = '''\
background-color: rgba(200, 100, 100, 200);
border-radius: 20;'''
		self.setStyleSheet(self.main_qss)

		# new title
		self.message_image = qpix("resources/message.png")
		self.updates_image = qpix("resources/updates.png")

		# title
		self.label = qlab(self)
		self.label.setStyleSheet('''\
border-radius: 0;
background-color: rgba(0, 0, 0, 0);
font: 40pt;
font-weight: 700;''')

		# button
		self.button = qpbt(self)
		self.button.setGeometry(15, 15, 50, 50)
		self.button.setText("???")
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
	background-color: transparent;
	color: black;
	font: 40px;
}''')

	# pull up function
	def pull_up(self):
		self.setGeometry(25, 80, 1150, 700)
		self.button.setText("???")
		self.button.setIconSize(qsiz(50, 50))
		self.button.clicked.connect(self.pull_down)


class message_panel(panel):

	def __init__(self, window: qwin):
		super().__init__(window)
		self.setGeometry(1000, 80, 1150, 700)
		self.label.setGeometry(25, 75, 36, 214)
		self.label.setPixmap(self.message_image)

	# pull down function
	def pull_down(self):
		self.setGeometry(1000, 80, 1150, 700)
		self.button.setText("???")
		self.button.setIconSize(qsiz(50, 50))
		self.button.clicked.connect(self.pull_up)


class updates_panel(panel):

	def __init__(self, window: qwin):
		super().__init__(window)
		self.setGeometry(1100, 80, 1150, 700)
		self.label.setGeometry(15, 80, 53, 199)
		self.label.setPixmap(self.updates_image)

	# pull down function
	def pull_down(self):
		self.setGeometry(1100, 80, 1150, 700)
		# self.button.setIcon(self.up)
		self.button.setText("???")
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
        self.woah = minibutton(self.bottom_panel)
        self.woah.setGeometry(15, 5, 40, 40)
        self.shock = minibutton(self.bottom_panel)
        self.shock.setGeometry(60, 5, 40, 40)
        self.haha = minibutton(self.bottom_panel)
        self.haha.setGeometry(105, 5, 40, 40)
        self.angry = minibutton(self.bottom_panel)
        self.angry.setGeometry(150, 5, 40, 40)
        self.sad = minibutton(self.bottom_panel)
        self.sad.setGeometry(195, 5, 40, 40)


class minibutton(qpbt):

	def __init__(self, frame: qfra):
		super().__init__(frame)
		self.setFixedSize(40, 40)
		self.setCursor(hand)
		self.setStyleSheet('''\
QPushButton::hover
{
	background-color: rgba(33, 33, 33, 100);
}
QPushButton
{
	border-style: none;
	background-color: rgba(0, 0, 0, 0);
}''')
		self.setIconSize(qsiz(30, 30))


class profile_header:

	def __init__(self, window: qwin):

		# background
		self.bgimage = qpix("resources/me/background.svg")
		self.background = qlab(window)
		self.background.setGeometry(-100, 100, 1080, 200)
		self.background.setPixmap(self.bgimage)
		self.background.setStyleSheet('''\
border-radius: 100;
background-color: transparent;
padding-left: 100;''')

		# foreground
		self.fgimage = qpix("resources/me/foreground.svg")
		self.foreground = qlab(window)
		self.foreground.setGeometry(100, 170, 200, 200)
		self.foreground.setPixmap(self.fgimage)
		self.foreground.setStyleSheet('''\
border-radius: 50;
background-color: transparent;''')

		# about
		self.about = qpbt(window)
		self.about.setGeometry(320, 320, 140, 40)
		self.about.setStyleSheet('''\
QPushButton::hover
{
	color: white;
}
QPushButton
{
	background-color: transparent;
	border-style: none;
	color: rgb(147, 224, 227);
}''')
		self.about.setText("none")

	def setvisible(self, status: bool):
		self.background.setVisible(status)
		self.foreground.setVisible(status)
		self.about.setVisible(status)


class settingsoption:

	def __init__(self, window: qwin):

		# button
		self.button = qpbt(window)
		self.button.setCursor(hand)
		self.button.clicked.connect(self.buttonclicked)
		self.button.setStyleSheet('''\
QPushButton::hover
{
	background-color: rgba(240, 223, 175, 200);
}
QPushButton
{
	border-radius: 20;
	background-color: rgba(240, 223, 175, 150);
	color: black;
	padding-left: 30;
	text-align: left;
	font: 30px;
}''')
		self.button.setVisible(False)

		# frame
		self.frame = qfra(window)
		self.frame.setGeometry(350, 140, 600, 600)
		self.frame.setStyleSheet('''\
background-color: transparent;
border-radius: 20;
border-style: solid;
border-width: 5;
border-color: rgb(240, 223, 175);''')
		self.frame.setVisible(False)

		self.label = qlab(self.frame)
		self.label.setGeometry(50, 50, 50, 50)
		self.label.setStyleSheet('''\
border-style: none;
font: 40px;''')

		self.otheroptions = []

	def buttonposition(self, y: int):
		self.button.setGeometry(-20, y, 300, 40)

	def setvisible(self, status: bool):
		if status:
			self.button.setVisible(True)
			return
		self.button.setVisible(False)
		self.frame.setVisible(False)

	def buttonclicked(self):
		if self.frame.isVisible():
			self.frame.setVisible(False)
			return
		for i in self.otheroptions:
			i.frame.setVisible(False)
		self.frame.setVisible(True)

	def createhead(self):
		self.label.setText(self.button.text())
		self.label.adjustSize()


class resizelement(settingsoption):

	def __init__(self, window: qwin):
		super().__init__(window)

		# button
		self.buttonposition(200)
		self.button.setText("resize window")
		
		# frame
		self.createhead()
		

class zoomelement(settingsoption):

	def __init__(self, window: qwin):
		super().__init__(window)

		# button
		self.buttonposition(300)
		self.button.setText("relative size")

		# frame
		self.createhead()


class themelement(settingsoption):

	def __init__(self, window: qwin):
		super().__init__(window)

		# button
		self.buttonposition(400)
		self.button.setText("change theme")

		# frame
		self.createhead()


class cardsbutton(qpbt):

	def __init__(self,window: qwin):
		super().__init__(window)
		self.setCursor(hand)
		self.setStyleSheet('''\
QPushButton::hover
{
	background-color: #595a5e;
}
QPushButton
{
	border-style: none;
	background-color: #303135;
	border-radius: 30;
}''')


class cardslayout:

	def __init__(self, window: qwin):

		# frame
		self.frame = qfra(window)
		self.frame.setGeometry(30, 90, 940, 680)
		self.frame.setStyleSheet('''\
background-color: transparent;
border-radius: 30;
border-style: solid;
border-width: 3;
border-color: white;''')
		
		# prev button
		self.prevbutton = cardsbutton(window)
		self.prevbutton.setIcon(qico("resources/cards/prev.svg"))
		self.prevbutton.setIconSize(qsiz(60, 60))
		self.prevbutton.setGeometry(20, 400, 60, 60)

		# next button
		self.nextbutton = cardsbutton(window)
		self.nextbutton.setIcon(qico("resources/cards/next.svg"))
		self.nextbutton.setIconSize(qsiz(60, 60))
		self.nextbutton.setGeometry(920, 400, 60, 60)

		# like button
		self.likebutton = cardsbutton(window)
		self.likebutton.setIcon(qico("resources/cards/like.svg"))
		self.likebutton.setIconSize(qsiz(50, 50))
		self.likebutton.setGeometry(710, 720, 60, 60)

		# comment button
		self.commentbutton = cardsbutton(window)
		self.commentbutton.setIcon(qico("resources/cards/comment.svg"))
		self.commentbutton.setIconSize(qsiz(50, 50))
		self.commentbutton.setGeometry(780, 720, 60, 60)

		# share button
		self.sharebutton = cardsbutton(window)
		self.sharebutton.setIcon(qico("resources/cards/share.svg"))
		self.sharebutton.setIconSize(qsiz(50, 50))
		self.sharebutton.setGeometry(850, 720, 60, 60)

		# report button
		self.reportbutton = cardsbutton(window)
		self.reportbutton.setIcon(qico("resources/cards/report.svg"))
		self.reportbutton.setIconSize(qsiz(50, 50))
		self.reportbutton.setGeometry(920, 720, 60, 60)

	def setvisible(self, status: bool):
		self.prevbutton.setVisible(status)
		self.nextbutton.setVisible(status)
		self.likebutton.setVisible(status)
		self.commentbutton.setVisible(status)
		self.sharebutton.setVisible(status)
		self.reportbutton.setVisible(status)
		self.frame.setVisible(status)


def hidewidgets(*widgets):
	for i in widgets:
		try:
			i.setVisible(False)
		except:
			i.setvisible(False)

def showwidgets(*widgets):
	for i in widgets:
		try:
			i.setVisible(True)
		except:
			i.setvisible(True)


class persontab(qfra):

	def __init__(self, window: qwin):
		super().__init__(window)
		self.setStyleSheet('''\
background-color: transparent;''')

		# background
		self.background = qlab(self)
		self.background.setGeometry(-60, 0, 950, 120)
		self.background.setStyleSheet('''\
border-radius: 60;
padding-left: 60;
background-color: transparent;''')

		# foreground
		self.foreground = qlab(self)
		self.foreground.setGeometry(20, 10, 100, 100)
		self.foreground.setStyleSheet('''\
background-color: transparent;
border-radius: 20;''')

		# name
		self.name = qlab(self)
		self.name.setGeometry(140, 50, 120, 60)
		self.name.setStyleSheet('''\
color: black;
background-color: rgba(200, 100, 125, 200);
border-radius: 10;''')

	def place(self, position: int):
		'''places person tab in the given index'''
		if position == 0:
			self.setGeometry(0, 90, 950, 120)
		elif position == 1:
			self.setGeometry(0, 230, 950, 120)
		elif position == 2:
			self.setGeometry(0, 370, 950, 120)
		elif position == 3:
			self.setGeometry(0, 510, 950, 120)
		elif position == 4:
			self.setGeometry(0, 650, 950, 120)

	def setname(self, name: str):
		'''sets the name of the person'''
		self.name.setText("  " + name + "  ")
		self.name.adjustSize()

	def setbackground(self, path: str):
		'''sets background using the path'''
		image = qpix(path)
		self.background.setPixmap(image)

	def setforeground(self, path: str):
		'''sets foreground using the path'''
		image = qpix(path)
		image.scaled(100, 100, keepratio)
		self.foreground.setPixmap(image)
