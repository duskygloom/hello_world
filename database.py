import os, pickle
import mysql.connector as sql

from dotenv import load_dotenv as load
load()

datadir = os.getenv("datadir")


class database:

	def __init__(self):
		self.host = os.getenv("host")
		self.user = os.getenv("user")
		self.password = os.getenv("password")
		self.database = os.getenv("database")
		self.client = sql.connect(
			host = self.host,
			user = self.user,
			password = self.password,
			database = self.database
        )
		self.cursor = self.client.cursor()


	def authentication(self, name: str, password: str) -> int:
		'''\
0 : username and password not found
1 : username found, password not
2 : username and password found'''
		cur = self.cursor
		com = f"select * from user_credentials where username = '{name}'"
		cur.execute(com)
		result = cur.fetchone()
		is_name = is_pass = 0
		if result != None:
			is_name = 1
		if is_name == 1:
			com = f"select password from user_credentials where username = '{name}'"
			cur.execute(com)
			result = cur.fetchone()
			if result[0] == password:
				is_pass = 1
		value = is_name * 10 + is_pass
		if value == 0:
			return 0
		elif value == 10:
			return 1
		elif value == 11:
			return 2

	def enrollment(self, name: str, password: str) -> int:
		'''\
0 : invalid username
1 : invalid password
2 : enrolled'''
		cur = self.cursor
		if name == "" or name.isspace() or len(name) < 5 or "\"" in name or "\\" in name:
			return 0
		elif password == "" or password.isspace() or len(password) < 5 or "\"" in password or "\\" in password:
			return 1
		com = f'''insert into user_credentials values ("{name}", "{password}")'''
		cur.execute(com)
		self.client.commit()
		return 2

# data related functions

def setuserdata(data: dict):
	with open("data/userdata.bat", "wb") as file:
		pickle.dump(data, file)

def getuserdata() -> dict:
	if "userdata.bat" in os.listdir("data"):
		with open("data/userdata.bat", "rb") as file:
			userdata = pickle.load(file)
			return userdata
	else:
		datadict = {"logged": None, "others": []}
		setuserdata(datadict)
		getuserdata()

def islogged() -> bool:
	if getuserdata()["logged"] is None:
		return False
	return True

def setconfdata(confdata: dict):
	with open("data/settings.bat", "wb") as file:
		pickle.dump(confdata, file)

def getconfdata() -> dict:
	if "settings.bat" in os.listdir("data"):
		with open("data/settings.bat", "rb") as file:
			confdata = pickle.load(file)
			return confdata
	else:
		confdict = {"resolution": "1200x800", "zoom": "1x", "theme": "duskydark"}
		setconfdata(confdict)
		getuserdata()

def copy(original_file: str, new_file: str):
	with open(original_file, "rb") as file1:
		with open(new_file, "wb") as file2:
			file2.write(file1.read())

def setupuser(name: str):
	basedir = f"{datadir}/{name}"
	try:
		os.mkdir(basedir)
		os.mkdir(f"{basedir}/images")
		copy("resoures/background.svg", f"{basedir}/images/background.svg")
		copy("resoures/foreground.svg", f"{basedir}/images/foreground.svg")
		os.mkdir(f"{basedir}/audio")
		os.mkdir(f"{basedir}/video")
		os.mkdir(f"{basedir}/docs")
		os.mkdir(f"{basedir}/misc")
	except FileExistsError:
		pass
