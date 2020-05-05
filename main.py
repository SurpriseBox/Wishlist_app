import os
import sys

from PyQt5.QtWidgets import QApplication
from mysql.connector import MySQLConnection, ProgrammingError, errors

from UI_classes.main_window_class import MainWindow


def init_db(connector, doc_root, user, password):
	cursor = connector.cursor()
	try:
		cursor.execute("create database _wishes_local_db_")
	except errors.Error:
		print('Database already exists. Loading schema...')
	connector.commit()
	cursor.close()

	try:
		os.system("mysql -u{} -p{} _wishes_local_db_ < {}assets/db_schema/db_schema.sql".format(user, password, doc_root))
	except Exception as err:
		print(err)
		return 1

	return 0


def set_connection(doc_root):
	conn = MySQLConnection()
	try:
		conn.connect(host='127.0.0.1', user='_wishes_db_user_', database='_wishes_local_db_')

	except ProgrammingError:
		print('For the first connection you need to provide '
			  'your MySQL root access for creating Database and the required user')
		user = str(input('username:'))
		password = str(input('password:'))
		conn.connect(host='127.0.0.1', user=user, password=password, database='')

		if init_db(conn, doc_root, user, password) == 1:
			print('Database creation failed.')
			return MySQLConnection()

		print("Schema loaded. Creating user...")
		cursor = conn.cursor()
		try:
			cursor.execute('create user _wishes_db_user_@127.0.0.1;')
			cursor.execute('grant all privileges on _wishes_local_db_.wish to _wishes_db_user_@127.0.0.1;')
			print("User created. Starting the app...")
		except errors.Error as err:
			print(err.msg)
			print("User creation failed.")

		cursor.close()
		conn.close()
		conn = set_connection(doc_root)

	return conn


if __name__ == "__main__":

	dirs = sys.argv[0].split('/')
	doc_root = ''
	for i in range(len(dirs) - 1):
		doc_root += dirs[i] + '/'

	db_connector = set_connection(doc_root)

	application = QApplication(sys.argv)
	main_window = MainWindow(doc_root, db_connector)
	main_window.show()
	sys.exit(application.exec())