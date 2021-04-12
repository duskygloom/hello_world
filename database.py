import mysql.connector as sql

from dotenv import load_dotenv as load
from os import getenv
load()


class database:

	def __init__(self):
		self.host = getenv("host")
		self.user = getenv("user")
		self.password = getenv("pass")
		self.database = getenv("data")
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
		return 2
