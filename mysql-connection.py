import pandas as pd
import mysql.connector
con = mysql.connector.connect(host ='localhost',port = 3306,user = 'root',password = '********')

# viewing all databases
try:

	mycursor = con.cursor()
	mycursor.execute('SHOW DATABASES')
	print('These are the available databases ')
	for i in mycursor:
		print(i)

except Exception as e:
	print('Could not show all databases')
	print(e)

#connecting to a existing database
try:
	con1 = mysql.connector.connect(host ='localhost',port = 3306,user = 'root',password = 'poruthur',database = 'studentdb')
	print("Connected to studentdb database")

except Exception as e:
	print("Could not connect to studentdb database")
	print(e)


