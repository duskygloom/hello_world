from PyQt5.QtWidgets import \
	QMainWindow    as qwin, \
	QFrame         as qfra, \
	QPushButton    as qpbt, \
	QLabel         as qlab, \
	QLineEdit      as qlin, \
	QShortcut      as qsho

from PyQt5.QtGui     import \
	QIcon          as qico, \
	QKeySequence   as qkes, \
	QFontDatabase  as qfdb

from PyQt5.QtCore import \
	Qt as qt

from objects import *
from database import *


# variables

center = qt.AlignCenter
top    = qt.AlignTop
left   = qt.AlignLeft
hand   = qt.PointingHandCursor
enter  = qkes("Return")
escape = qkes("Escape")
userdata = getuserdata()
settings = getconfdata()


class interface:
    
	def __init__(self, window: qwin):
		self.mainwindow     = window
		self.icon  = qico("resources/icon.svg")
		self.topbox         = qfra(window)
		self.homebutton     = qpbt(window)
		self.cardsbutton    = top_button(window)
		self.peoplebutton   = top_button(window)
		self.groupsbutton   = top_button(window)
		self.postsbutton    = top_button(window)
		self.settingsbutton = top_button(window)
		self.accountsbutton = top_button(window)
		self.label01        = qlab(window)
		self.label02        = qlab(window)
		self.linedit01      = qlin(window)
		self.linedit02      = qlin(window)
		self.button01       = body_button(window)
		self.button02       = body_button(window)
		self.database       = database()
		self.popupbox01     = popup(window)
		self.popupbox02     = popup(window)
		self.card           = card(window)
		self.resizelem      = resizelement(window)
		self.zoomelem       = zoomelement(window)
		self.themelem       = themelement(window)
		self.profheader     = profile_header(window)
		self.cardsgroup     = cardslayout(window)
		self.person01       = persontab(window)
		self.person02       = persontab(window)
		self.person03       = persontab(window)
		self.person04       = persontab(window)
		self.person05       = persontab(window)
		self.group01        = persontab(window)
		self.group02        = persontab(window)
		self.group03        = persontab(window)
		self.group04        = persontab(window)
		self.group05        = persontab(window)
		self.panelmessage   = message_panel(window)
		self.panelupdates   = updates_panel(window)
		self.accountbox     = popup(window)
		self.shortcut01     = qsho(self.linedit02)
		self.shortcut02     = qsho(self.popupbox01)
		self.shortcut03     = qsho(self.popupbox02)
		self.shortcut04     = qsho(self.popupbox01)
		self.shortcut05     = qsho(self.popupbox02)
		self.shortcut06     = qsho(self.accountbox)


		# window
		window = self.mainwindow
		window.setGeometry(100, 100, 1200, 800)
		window.setFixedSize(1200, 800)
		window.setWindowTitle("hello_world")
		window.setWindowIcon(self.icon)
		window.setStyleSheet('''\
background-color: rgb(33, 33, 33);
color: white;
font: 20pt "Josefin Sans"''')

		# top box
		box = self.topbox
		box.setGeometry(17, 10, 1170, 60)
		box.setStyleSheet('''\
border-style: none;
background-color: rgba(33, 33, 33, 0);
border-radius: 30;
border-style: solid;
border-width: 3;
border-color: rgb(255, 100, 125);''')

		# home button
		button = self.homebutton
		button.setGeometry(10, 10, 130, 60)
		button.setText("home")
		button.clicked.connect(self.setup_home)
		button.setCursor(hand)
		button.setStyleSheet('''\
background-color: rgb(255, 100, 125);
font-size: 20pt;
color: black;
border-radius: 30;''')

		# cards button
		button = self.cardsbutton
		button.setGeometry(160, 20, 140, 40)
		button.setText("cards")
		button.clicked.connect(self.setup_cards)

		# people button
		button = self.peoplebutton
		button.setGeometry(320, 20, 140, 40)
		button.setText("people")
		button.clicked.connect(self.setup_people)

		# groups button
		button = self.groupsbutton
		button.setGeometry(480, 20, 140, 40)
		button.setText("groups")
		button.clicked.connect(self.setup_groups)

		# posts button
		button = self.postsbutton
		button.setGeometry(640, 20, 140, 40)
		button.setText("posts")
		button.clicked.connect(self.setup_posts)

		# settings button
		button = self.settingsbutton
		button.setGeometry(880, 20, 140, 40)
		button.setText("settings")
		button.clicked.connect(self.setup_settings)

		# accounts button
		button = self.accountsbutton
		button.setGeometry(1040, 20, 140, 40)
		button.setText("accounts")
		button.clicked.connect(self.accounts_click)

		# settings options

		self.resizelem.otheroptions = [self.zoomelem, self.themelem]
		self.zoomelem.otheroptions = [self.resizelem, self.themelem]
		self.themelem.otheroptions = [self.resizelem, self.zoomelem]

		

	def setup_start(self):

		# show widgets
		showwidgets(
			self.label01,
			self.label02,
			self.linedit01,
			self.linedit02,
			self.button01
		)

		# hide widgets
		hidewidgets(
			self.group01,
			self.group02,
			self.group03,
			self.group04,
			self.group05,
			self.button02,
			self.card,
			self.resizelem,
			self.themelem,
			self.zoomelem,
			self.profheader,
			self.cardsgroup,
			self.panelmessage,
			self.panelupdates,
			self.accountbox,
			self.person01,
			self.person02,
			self.person03,
			self.person04,
			self.person05
		)

		# fixing top buttons
		self.cardsbutton.isselected(False)
		self.peoplebutton.isselected(False)
		self.groupsbutton.isselected(False)
		self.postsbutton.isselected(False)
		self.settingsbutton.isselected(False)

		# name label
		label = self.label01
		label.setGeometry(170, 130, 860, 280)
		label.setText("hello_world")
		label.setAlignment(center)
		label.setStyleSheet('''\
background-color: rgba(33, 33, 33, 0);
border-style: solid;
border-width: 5;
border-color: rgb(255, 100, 125);
border-radius: 140;
font: 100pt;
padding-top: 40;''')
		label.setVisible(True)

		# name field
		linedit = self.linedit01
		linedit.setGeometry(430, 520, 340, 40)
		linedit.setPlaceholderText("username")
		linedit.setStyleSheet('''\
background-color: rgba(211, 215, 207, 50);
padding-left: 10;
padding-right: 10;
border-radius: 15;''')
		linedit.setVisible(True)

		# password field
		linedit = self.linedit02
		linedit.setGeometry(430, 580, 340, 40)
		linedit.setEchoMode(qlin.Password)
		linedit.setPlaceholderText("password")
		linedit.setStyleSheet('''\
background-color: rgba(211, 215, 207, 50);
padding-left: 10;
padding-right: 10;
border-radius: 15;''')
		linedit.setVisible(True)

		# proceed button
		button = self.button01
		button.setGeometry(540, 670, 130, 50)
		button.setText("proceed")
		button.clicked.connect(self.proceed_click)
		button.setVisible(True)

		# status label
		label = self.label02
		label.setGeometry(0, 770, 130, 50)
		label.adjustSize()
		label.setStyleSheet('''\
color: gray;
padding-left: 5''')
		label.setVisible(True)

		# enroll box
		popbox = self.popupbox01
		popbox.yes.clicked.connect(self.enroll_yes)
		popbox.no.clicked.connect(self.enroll_no)

		# login box
		popbox = self.popupbox02
		popbox.yes.clicked.connect(self.login_yes)
		popbox.no.clicked.connect(self.login_no)

		# accounts box
		popbox = self.accountbox
		popbox.setGeometry(570, 100, 600, 400)
		popbox.no.clicked.connect(self.accounts_close)

		# proceed shortcut
		shortcut = self.shortcut01
		shortcut.setKey(enter)
		shortcut.activated.connect(self.proceed_click)
		shortcut.setEnabled(True)

		# enroll yes shortcut
		shortcut = self.shortcut02
		shortcut.setKey(enter)
		shortcut.activated.connect(self.enroll_yes)
		shortcut.setEnabled(False)

		# enroll no shortcut
		shortcut = self.shortcut04
		shortcut.setKey(escape)
		shortcut.activated.connect(self.enroll_no)
		shortcut.setEnabled(False)

		# login yes shortcut
		shortcut = self.shortcut03
		shortcut.setKey(enter)
		shortcut.activated.connect(self.login_yes)
		shortcut.setEnabled(False)

		# login no shortcut
		shortcut = self.shortcut05
		shortcut.setKey(escape)
		shortcut.activated.connect(self.login_no)
		shortcut.setEnabled(False)

		# accounts close shortcut
		shortcut = self.shortcut06
		shortcut.setKey(escape)
		shortcut.activated.connect(self.accounts_close)
		shortcut.setEnabled(False)

		# accounts box
		popbox = self.accountbox
		popbox.yes.setVisible(False)


	# home window
	def setup_home(self):

		# show widgets
		showwidgets(
			self.profheader,
			self.panelmessage,
			self.panelupdates
		)

		# hiding widgets
		hidewidgets(
			self.group01,
			self.group02,
			self.group03,
			self.group04,
			self.group05,
			self.label01,
			self.linedit01,
			self.linedit02,
			self.button01,
			self.button02,
			self.card,
			self.resizelem,
			self.zoomelem,
			self.themelem,
			self.cardsgroup,
			self.person01,
			self.person02,
			self.person03,
			self.person04,
			self.person05
		)

		# fixing top buttons
		self.cardsbutton.isselected(False)
		self.peoplebutton.isselected(False)
		self.groupsbutton.isselected(False)
		self.postsbutton.isselected(False)
		self.settingsbutton.isselected(False)

		# profile header
		user = userdata["logged"]
		self.profheader.about.setText(user)


	# cards window
	def setup_cards(self):

		# show widgets
		showwidgets(
			self.cardsgroup,
			self.panelmessage,
			self.panelupdates
		)

		# hiding widgets
		hidewidgets(
			self.group01,
			self.group02,
			self.group03,
			self.group04,
			self.group05,
			self.label01,
			self.linedit01,
			self.linedit02,
			self.button01,
			self.button02,
			self.profheader,
			self.themelem,
			self.zoomelem,
			self.resizelem,
			self.person01,
			self.person02,
			self.person03,
			self.person04,
			self.person05
		)

		# fixing top buttons
		self.cardsbutton.isselected(True)
		self.peoplebutton.isselected(False)
		self.groupsbutton.isselected(False)
		self.postsbutton.isselected(False)
		self.settingsbutton.isselected(False)


	# people window
	def setup_people(self):

		# showing widgets
		showwidgets(
			self.person01,
			self.person02,
			self.person03,
			self.person04,
			self.person05,
			self.panelmessage,
			self.panelupdates
		)

		# hiding widgets
		hidewidgets(
			self.group01,
			self.group02,
			self.group03,
			self.group04,
			self.group05,
			self.linedit01,
			self.linedit02,
			self.button01,
			self.button02,
			self.card,
			self.profheader,
			self.resizelem,
			self.zoomelem,
			self.themelem
		)

		# fixing top buttons
		self.cardsbutton.isselected(False)
		self.peoplebutton.isselected(True)
		self.groupsbutton.isselected(False)
		self.postsbutton.isselected(False)
		self.settingsbutton.isselected(False)
		self.cardsgroup.setvisible(False)

		# person tabs
		tab = self.person01
		tab.place(0)
		tab.setname("duskygloom")
		tab.setbackground("resources/me/background.svg")
		tab.setforeground("resources/me/foreground.svg")
		tab = self.person02
		tab.place(1)
		tab.setname("hello")
		tab = self.person03
		tab.place(2)
		tab.setname("shiro")
		tab = self.person04
		tab.place(3)
		tab.setname("world")
		tab = self.person05
		tab.place(4)
		tab.setname("endorsi")


	# groups window
	def setup_groups(self):

		# show widgets
		showwidgets(
			self.group01,
			self.group02,
			self.group03,
			self.group04,
			self.group05,
			self.panelmessage,
			self.panelupdates
		)

		# hiding widgets
		hidewidgets(
			self.linedit01,
			self.linedit02,
			self.button01,
			self.button02,
			self.card,
			self.profheader,
			self.resizelem,
			self.zoomelem,
			self.themelem,
			self.cardsgroup,
			self.person01,
			self.person02,
			self.person03,
			self.person04,
			self.person05
		)
		
		# fixing top buttons
		self.cardsbutton.isselected(False)
		self.peoplebutton.isselected(False)
		self.groupsbutton.isselected(True)
		self.postsbutton.isselected(False)
		self.settingsbutton.isselected(False)

		# group tabs
		tab = self.group01
		tab.setname("tower of god memes")
		tab.place(0)
		tab = self.group02
		tab.setname("webtoon memes")
		tab.place(1)
		tab = self.group03
		tab.setname("unOrdinary")
		tab.place(2)
		tab = self.group04
		tab.setname("god of high school")
		tab.place(3)
		tab = self.group05
		tab.setname("tower of god")
		tab.place(4)


	# posts window
	def setup_posts(self):

		# showing widgets
		showwidgets(
			self.panelmessage,
			self.panelupdates
		)

		# hiding widgets
		hidewidgets(
			self.group01,
			self.group02,
			self.group03,
			self.group04,
			self.group05,
			self.linedit01,
			self.linedit02,
			self.button01,
			self.button02,
			self.card,
			self.profheader,
			self.resizelem,
			self.zoomelem,
			self.themelem,
			self.cardsgroup,
			self.person01,
			self.person02,
			self.person03,
			self.person04,
			self.person05
		)
		
		# fixing top buttons
		self.cardsbutton.isselected(False)
		self.peoplebutton.isselected(False)
		self.groupsbutton.isselected(False)
		self.postsbutton.isselected(True)
		self.settingsbutton.isselected(False)


	# settings window
	def setup_settings(self):

		# showing elements
		showwidgets(
			self.panelmessage,
			self.panelupdates,
			self.resizelem,
			self.zoomelem,
			self.themelem
		)

		# hiding elements
		hidewidgets(
			self.group01,
			self.group02,
			self.group03,
			self.group04,
			self.group05,
			self.label01,
			self.linedit01,
			self.linedit02,
			self.button01,
			self.button02,
			self.card,
			self.profheader,
			self.cardsgroup,
			self.person01,
			self.person02,
			self.person03,
			self.person04,
			self.person05
		)

		# fixing top buttons
		self.cardsbutton.isselected(False)
		self.peoplebutton.isselected(False)
		self.groupsbutton.isselected(False)
		self.postsbutton.isselected(False)
		self.settingsbutton.isselected(True)


	# accounts click function
	def accounts_click(self):
		self.accountbox.no.setText("close  ")
		text = "current user: \n\t"
		logged = userdata["logged"]
		if logged is not None:
			text += logged
		text += "\n\nall users: \n"
		for i in userdata["others"][:9]:
			text += "\t" + i + "\n"
		self.accountbox.setText(text)
		self.accountbox.setVisible(True)
		self.shortcut06.setEnabled(True)

	# proceed click function
	def proceed_click(self):
		stat = self.label02
		name = self.linedit01.text()
		password = self.linedit02.text()
		value = self.database.authentication(name, password)
		if value == 0:
			stat.setText("username is not registered")
			stat.adjustSize()
			self.popupbox01.setText(f'''\
Confirm enrollment!


username: {self.linedit01.text()}
password: {self.linedit02.text()}

rules for username and password:
??? username and password must not be empty or whitespace
??? username and password must be longer than 5 characters
??? username and password cannot contain " and \\''')
			self.popupbox01.setVisible(True)
			self.shortcut01.setEnabled(False)
			self.shortcut02.setEnabled(True)
			self.shortcut04.setEnabled(True)
		elif value == 2:
			stat.setText("logged in")
			stat.adjustSize()
			self.popupbox02.setText(f'''\
Confirm login!


username: {self.linedit01.text()}
password: {self.linedit02.text()}''')
			self.popupbox02.setVisible(True)
			self.shortcut01.setEnabled(False)
			self.shortcut03.setEnabled(True)
			self.shortcut05.setEnabled(True)
		elif value == 1:
			stat.setText("incorrect password")
			stat.adjustSize()

	# enroll box yes function
	def enroll_yes(self):
		name = self.linedit01.text()
		password = self.linedit02.text()
		signal = self.database.enrollment(name, password)
		if signal == 0:
			self.label02.setText("invalid username")
			self.popupbox01.setVisible(False)
			self.shortcut01.setEnabled(True)
			self.shortcut02.setEnabled(False)
		elif signal == 1:
			self.label02.setText("invalid password")
			self.popupbox01.setVisible(False)
			self.shortcut01.setEnabled(True)
			self.shortcut02.setEnabled(False)
		elif signal == 2:
			self.label02.setText("account created")
			setupuser(name)
			self.popupbox01.setVisible(False)
			self.shortcut01.setEnabled(True)
			self.shortcut02.setEnabled(False)

	# login box yes function
	def login_yes(self):
		global userdata
		user = self.linedit01.text()
		if user != userdata["logged"]:
			userdata["logged"] = user
		_list = userdata["others"]
		if user != _list:
			if user in _list:
				_list.remove(user)
			_list.insert(0, user)
		setuserdata(userdata)
		self.popupbox02.setVisible(False)
		self.shortcut01.setEnabled(True)
		self.shortcut03.setEnabled(False)

	# enroll box no function
	def enroll_no(self):
		self.popupbox01.setVisible(False)
		self.shortcut01.setEnabled(True)
		self.shortcut02.setEnabled(False)
		self.shortcut04.setEnabled(False)

	# login box no function
	def login_no(self):
		self.popupbox02.setVisible(False)
		self.shortcut01.setEnabled(True)
		self.shortcut03.setEnabled(False)
		self.shortcut05.setEnabled(False)

	# account box close function
	def accounts_close(self):
		self.accountbox.setVisible(False)
		self.shortcut06.setEnabled(False)
