import pickle

from PyQt5.QtWidgets import \
	QMainWindow    as qwin, \
	QFrame         as qfra, \
	QPushButton    as qpbt, \
	QLabel         as qlab, \
	QLineEdit      as qlin, \
	QShortcut      as qsho

from PyQt5.QtGui     import \
	QIcon          as qico, \
	QKeySequence   as qkes

from PyQt5.QtCore import \
	Qt as qt

from objects import *
from database import database


# variables

center = qt.AlignCenter
top    = qt.AlignTop
left   = qt.AlignLeft
hand   = qt.PointingHandCursor
enter  = qkes("Return")
escape = qkes("Escape")
data   = "data/users.bat"
try:
	with open(data, "rb") as file:
		users = pickle.load(file)
except:
	users = []


class interface:
    
	def __init__(self, window: qwin):
		self.main_window     = window
		self.top_box         = qfra(window)
		self.icon            = qico("resources/icon.svg")
		self.home_button     = qpbt(window)
		self.cards_button    = top_button(window)
		self.people_button   = top_button(window)
		self.groups_button   = top_button(window)
		self.posts_button    = top_button(window)
		self.settings_button = top_button(window)
		self.accounts_button = top_button(window)
		self.label_01        = qlab(window)
		self.label_02        = qlab(window)
		self.lineedit_01     = qlin(window)
		self.lineedit_02     = qlin(window)
		self.button_01       = body_button(window)
		self.button_02       = body_button(window)
		self.database        = database()
		self.popupbox_01     = popup(window)
		self.popupbox_02     = popup(window)
		self.popupbox_03     = popup(window)
		self.card            = card(window)
		self.panel_message   = message_panel(window)
		self.panel_updates   = updates_panel(window)
		self.shortcut_01     = qsho(self.lineedit_02)
		self.shortcut_02     = qsho(self.popupbox_01)
		self.shortcut_03     = qsho(self.popupbox_02)
		self.shortcut_04     = qsho(self.popupbox_01)
		self.shortcut_05     = qsho(self.popupbox_02)
		self.shortcut_06     = qsho(self.popupbox_03)


		# window
		window = self.main_window
		window.setGeometry(100, 100, 1200, 800)
		window.setFixedSize(1200, 800)
		window.setWindowTitle("hello_world")
		window.setWindowIcon(self.icon)
		window.setStyleSheet('''\
background-color: rgb(33, 33, 33);
color: white;
font: 20pt "Josefin Sans"''')

		# top box
		box = self.top_box
		box.setGeometry(17, 10, 1170, 60)
		box.setStyleSheet('''\
border-style: none;
background-color: rgba(33, 33, 33, 0);
border-radius: 30;
border-style: solid;
border-width: 3;
border-color: rgb(255, 100, 125);''')

		# home button
		button = self.home_button
		button.setGeometry(10, 10, 130, 60)
		button.setText("home")
		button.clicked.connect(self.setup_start)
		button.setCursor(hand)
		button.setStyleSheet('''\
background-color: rgb(255, 100, 125);
font-size: 20pt;
color: black;
border-radius: 30;''')

		# cards button
		button = self.cards_button
		button.setGeometry(160, 20, 140, 40)
		button.setText("cards")
		button.clicked.connect(self.setup_cards)

		# people button
		button = self.people_button
		button.setGeometry(320, 20, 140, 40)
		button.setText("people")
		button.clicked.connect(self.setup_people)

		# groups button
		button = self.groups_button
		button.setGeometry(480, 20, 140, 40)
		button.setText("groups")
		button.clicked.connect(self.setup_groups)

		# posts button
		button = self.posts_button
		button.setGeometry(640, 20, 140, 40)
		button.setText("posts")
		button.clicked.connect(self.setup_posts)

		# settings button
		button = self.settings_button
		button.setGeometry(880, 20, 140, 40)
		button.setText("settings")
		button.clicked.connect(self.setup_settings)

		# accounts button
		button = self.accounts_button
		button.setGeometry(1040, 20, 140, 40)
		button.setText("accounts")
		button.clicked.connect(self.accounts_click)
		

	def setup_start(self):

		# remove unncessary widgets
		self.button_02.setVisible(False)
		self.panel_message.setVisible(False)
		self.panel_updates.setVisible(False)
		self.card.setVisible(False)

		# name label
		label = self.label_01
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
		linedit = self.lineedit_01
		linedit.setGeometry(430, 520, 340, 40)
		linedit.setPlaceholderText("username")
		linedit.setStyleSheet('''\
background-color: rgba(211, 215, 207, 50);
padding-left: 10;
padding-right: 10;
border-radius: 15;''')
		linedit.setVisible(True)

		# password field
		linedit = self.lineedit_02
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
		button = self.button_01
		button.setGeometry(540, 670, 130, 50)
		button.setText("proceed")
		button.clicked.connect(self.proceed_click)
		button.setVisible(True)

		# status label
		label = self.label_02
		label.setGeometry(0, 770, 130, 50)
		label.adjustSize()
		label.setStyleSheet('''\
color: gray;
padding-left: 5''')
		label.setVisible(True)

		# enroll box
		popbox = self.popupbox_01
		popbox.yes.clicked.connect(self.enroll_yes)
		popbox.no.clicked.connect(self.enroll_no)

		# login box
		popbox = self.popupbox_02
		popbox.yes.clicked.connect(self.login_yes)
		popbox.no.clicked.connect(self.login_no)

		# accounts box
		popbox = self.popupbox_03
		popbox.setGeometry(570, 100, 600, 400)
		popbox.no.clicked.connect(self.accounts_close)

		# proceed shortcut
		shortcut = self.shortcut_01
		shortcut.setKey(enter)
		shortcut.activated.connect(self.proceed_click)
		shortcut.setEnabled(True)

		# enroll yes shortcut
		shortcut = self.shortcut_02
		shortcut.setKey(enter)
		shortcut.activated.connect(self.enroll_yes)
		shortcut.setEnabled(False)

		# enroll no shortcut
		shortcut = self.shortcut_04
		shortcut.setKey(escape)
		shortcut.activated.connect(self.enroll_no)
		shortcut.setEnabled(False)

		# login yes shortcut
		shortcut = self.shortcut_03
		shortcut.setKey(enter)
		shortcut.activated.connect(self.login_yes)
		shortcut.setEnabled(False)

		# login no shortcut
		shortcut = self.shortcut_05
		shortcut.setKey(escape)
		shortcut.activated.connect(self.login_no)
		shortcut.setEnabled(False)

		# accounts close shortcut
		shortcut = self.shortcut_06
		shortcut.setKey(escape)
		shortcut.activated.connect(self.accounts_close)
		shortcut.setEnabled(False)

		# accounts box
		popbox = self.popupbox_03
		popbox.yes.setVisible(False)


	# home window
	def setup_home(self):
		self.label_01.setText("home")
		self.lineedit_01.setVisible(False)
		self.lineedit_02.setVisible(False)
		self.button_01.setVisible(False)
		self.button_02.setVisible(False)
		self.card.setVisible(False)

		# updates panel
		panel = self.panel_updates
		panel.setVisible(True)

		# messages panel
		panel = self.panel_message
		panel.setVisible(True)


	# cards window
	def setup_cards(self):

		# hiding unnecessary widgets
		self.label_01.setVisible(False)
		self.lineedit_01.setVisible(False)
		self.lineedit_02.setVisible(False)
		self.button_01.setVisible(False)
		self.button_02.setVisible(False)

		# card
		card = self.card
		card.setVisible(True)
		
		# updates panel
		panel = self.panel_updates
		panel.setVisible(False)

		# messages panel
		panel = self.panel_message
		panel.setVisible(False)


	# people window
	def setup_people(self):
		self.label_01.setText("people")
		self.lineedit_01.setVisible(False)
		self.lineedit_02.setVisible(False)
		self.button_01.setVisible(False)
		self.button_02.setVisible(False)
		self.card.setVisible(False)

		# updates panel
		panel = self.panel_updates
		panel.setVisible(True)

		# messages panel
		panel = self.panel_message
		panel.setVisible(True)


	# groups window
	def setup_groups(self):
		self.label_01.setText("groups")
		self.lineedit_01.setVisible(False)
		self.lineedit_02.setVisible(False)
		self.button_01.setVisible(False)
		self.button_02.setVisible(False)
		self.card.setVisible(False)

		# updates panel
		panel = self.panel_updates
		panel.setVisible(True)

		# messages panel
		panel = self.panel_message
		panel.setVisible(True)


	# posts window
	def setup_posts(self):
		self.label_01.setText("posts")
		self.lineedit_01.setVisible(False)
		self.lineedit_02.setVisible(False)
		self.button_01.setVisible(False)
		self.button_02.setVisible(False)
		self.card.setVisible(False)

		# updates panel
		panel = self.panel_updates
		panel.setVisible(True)

		# messages panel
		panel = self.panel_message
		panel.setVisible(True)


	# settings window
	def setup_settings(self):
		self.label_01.setText("settings")
		self.lineedit_01.setVisible(False)
		self.lineedit_02.setVisible(False)
		self.button_01.setVisible(False)
		self.button_02.setVisible(False)
		self.card.setVisible(False)


	# accounts click function
	def accounts_click(self):
		self.popupbox_03.no.setText("close  ")
		text = "logged in users: \n\n"
		for i in users:
			text += " > " + i + "\n"
		self.popupbox_03.setText(text)
		self.popupbox_03.setVisible(True)
		self.shortcut_06.setEnabled(True)

	# proceed click function
	def proceed_click(self):
		stat = self.label_02
		name = self.lineedit_01.text()
		password = self.lineedit_02.text()
		value = self.database.authentication(name, password)
		if value == 0:
			stat.setText("username is not registered")
			stat.adjustSize()
			self.popupbox_01.setText(f'''\
Confirm enrollment!


username: {self.lineedit_01.text()}
password: {self.lineedit_02.text()}

rules for username and password:
• username and password must not be empty or whitespace
• username and password must be longer than 5 characters
• username and password cannot contain " and \\''')
			self.popupbox_01.setVisible(True)
			self.shortcut_01.setEnabled(False)
			self.shortcut_02.setEnabled(True)
			self.shortcut_04.setEnabled(True)
		elif value == 2:
			stat.setText("logging in...")
			stat.adjustSize()
			self.popupbox_02.setText(f'''\
Confirm login!


username: {self.lineedit_01.text()}
password: {self.lineedit_02.text()}''')
			self.popupbox_02.setVisible(True)
			self.shortcut_01.setEnabled(False)
			self.shortcut_03.setEnabled(True)
			self.shortcut_05.setEnabled(True)
		elif value == 1:
			stat.setText("incorrect password")
			stat.adjustSize()

	# enroll box yes function
	def enroll_yes(self):
		name = self.lineedit_01.text()
		password = self.lineedit_02.text()
		signal = self.database.enrollment(name, password)
		if signal == 0:
			self.label_02.setText("invalid username")
			self.popupbox_01.setVisible(False)
			self.shortcut_01.setEnabled(True)
			self.shortcut_02.setEnabled(False)
		elif signal == 1:
			self.label_02.setText("invalid password")
			self.popupbox_01.setVisible(False)
			self.shortcut_01.setEnabled(True)
			self.shortcut_02.setEnabled(False)
		elif signal == 2:
			self.label_02.setText("account created")
			self.popupbox_01.setVisible(False)
			self.shortcut_01.setEnabled(True)
			self.shortcut_02.setEnabled(False)

	# login box yes function
	def login_yes(self):
		global users
		user = self.lineedit_01.text()
		if user not in users:
			users.append(self.lineedit_01.text())
		with open(data, "wb") as user_bin:
			pickle.dump(users, user_bin)
		self.popupbox_02.setVisible(False)
		self.shortcut_01.setEnabled(True)
		self.shortcut_03.setEnabled(False)

	# enroll box no function
	def enroll_no(self):
		self.popupbox_01.setVisible(False)
		self.shortcut_01.setEnabled(True)
		self.shortcut_02.setEnabled(False)
		self.shortcut_04.setEnabled(False)

	# login box no function
	def login_no(self):
		self.popupbox_02.setVisible(False)
		self.shortcut_01.setEnabled(True)
		self.shortcut_03.setEnabled(False)
		self.shortcut_05.setEnabled(False)

	# account box close function
	def accounts_close(self):
		self.popupbox_03.setVisible(False)
		self.shortcut_06.setEnabled(False)

	# reset password function
	def reset_password(self):
		button = self.button_02
		button.setGeometry(430, 700, 50, 50)		
		button.setText("reset password")
		button.adjustSize()
		button.setVisible(True)
		


