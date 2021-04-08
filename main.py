from time import sleep

from PyQt5.QtWidgets import \
	QMainWindow    as qwin, \
	QApplication   as qapp, \
	QFrame         as qfra, \
	QPushButton    as qpbt, \
	QLabel         as qlab, \
	QLineEdit      as qlin

from PyQt5.QtCore    import \
	Qt as qt

from PyQt5.QtGui     import \
	QIcon          as qico


# variables

center = qt.AlignCenter


class interface:
    
	def __init__(self, window: qwin):
		self.main_window     = window
		self.top_box         = qfra(window)
		self.you_button      = qpbt(window)
		self.cards_button    = qpbt(window)
		self.people_button   = qpbt(window)
		self.groups_button   = qpbt(window)
		self.posts_button    = qpbt(window)
		self.settings_button = qpbt(window)
		self.accounts_button = qpbt(window)
		self.name_label      = qlab(window)
		self.email_field     = qlin(window)
		self.password_field  = qlin(window)
		self.proceed_button  = qpbt(window)

	def setup_win(self):

		# window
		win = self.main_window
		win.setGeometry(100, 100, 1200, 800)
		win.setWindowTitle("hello_world")
		win.setWindowIcon(qico("icon.svg"))
		win.setStyleSheet('''\
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

		# you button
		you = self.you_button
		you.setGeometry(10, 10, 130, 60)
		you.setText("h_w")
		you.clicked.connect(self.you_click)
		you.setStyleSheet('''\
background-color: rgb(255, 100, 125);
font-size: 25pt;
font-weight: 700;
color: black;
border-radius: 30;''')

		# cards button
		car = self.cards_button
		car.setGeometry(160, 20, 140, 40)
		car.setText("cards")
		car.clicked.connect(self.car_click)
		car.setStyleSheet('''\
border-style: none;
background-color: rgba(33, 33, 33, 0);''')

		# people button
		peo = self.people_button
		peo.setGeometry(320, 20, 140, 40)
		peo.setText("people")
		peo.clicked.connect(self.peo_click)
		peo.setStyleSheet('''\
border-style: none;
background-color: rgba(33, 33, 33, 0);''')

		# groups button
		gro = self.groups_button
		gro.setGeometry(480, 20, 140, 40)
		gro.setText("groups")
		gro.clicked.connect(self.gro_click)
		gro.setStyleSheet('''\
border-style: none;
background-color: rgba(33, 33, 33, 0);''')

		# posts button
		pos = self.posts_button
		pos.setGeometry(640, 20, 140, 40)
		pos.setText("posts")
		pos.clicked.connect(self.pos_click)
		pos.setStyleSheet('''\
border-style: none;
background-color: rgba(33, 33, 33, 0);''')

		# settings button
		sett = self.settings_button
		sett.setGeometry(880, 20, 140, 40)
		sett.setText("settings")
		sett.clicked.connect(self.set_click)
		sett.setStyleSheet('''\
border-style: none;
background-color: rgba(33, 33, 33, 0);''')

		# accounts button
		acc = self.accounts_button
		acc.setGeometry(1040, 20, 140, 40)
		acc.setText("accounts")
		acc.clicked.connect(self.acc_click)
		acc.setStyleSheet('''\
border-style: none;
background-color: rgba(33, 33, 33, 0);''')

		# name label
		nam = self.name_label
		nam.setGeometry(170, 130, 860, 280)
		nam.setText("hello_world")
		nam.setAlignment(center)
		nam.setStyleSheet('''\
background-color: rgba(33, 33, 33, 0);
border-style: solid;
border-width: 5;
border-color: rgb(255, 100, 125);
border-radius: 140;
font: 100pt;
padding-top: 40;''')

		# email field
		mai = self.email_field
		mai.setGeometry(430, 520, 340, 40)
		mai.setPlaceholderText("email_id")
		mai.setStyleSheet('''\
background-color: rgba(211, 215, 207, 50);
padding-left: 10;
border-radius: 15;''')

		# password field
		pas = self.password_field
		pas.setGeometry(430, 580, 340, 40)
		pas.setEchoMode(qlin.Password)
		pas.setPlaceholderText("password")
		pas.setStyleSheet('''\
background-color: rgba(211, 215, 207, 50);
padding-left: 10;
border-radius: 15;''')

		# proceed button
		pro = self.proceed_button
		pro.setGeometry(540, 670, 130, 50)
		pro.setText("proceed")
		pro.clicked.connect(self.pro_click)
		pro.setStyleSheet('''\
background-color: rgb(255, 100, 125);
color: black;
border-radius: 25;''')


	# you button function
	def you_click(self):
		btext = self.you_button.text()
		if btext == "h_w":
			self.you_button.setText("you")
		else:
			self.you_button.setText("h_w")

	# cards button function
	def car_click(self):
		print("cards")

	# people click function
	def peo_click(self):
		print("people")

	# groups click function
	def gro_click(self):
		print("groups")

	# posts click function
	def pos_click(self):
		print("posts")

	# settings click function
	def set_click(self):
		print("settings")

	# accounts click function
	def acc_click(self):
		print("accounts")

	# proceed click function
	def pro_click(self):
		email = self.email_field.text()
		password = self.password_field.text()
		print(f"email: {email}, password: {password}")



if __name__ == "__main__":
    import sys
    app = qapp(sys.argv)
    window = qwin()
    ui = interface(window)
    ui.setup_win()
    window.show()
    sys.exit(app.exec_())