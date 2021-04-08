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


	def authentication(self, email: str, password: str) -> int:
		'''\
0  : email and password not found
10 : email found, password not
11 : email and password found'''
		cur = self.cursor
		com = f"select * from user_credentials where email = '{email}'"
		cur.execute(com)
		result = cur.fetchone()
		is_mail = is_pass = 0
		if result != None:
			is_mail = 1
		if is_mail == 1:
			com = f"select password from user_credentials where email = '{email}'"
			cur.execute(com)
			result = cur.fetchone()
			if result[0] == password:
				is_pass = 1
		return is_mail * 10 + is_pass
		