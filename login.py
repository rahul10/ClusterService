#!/usr/bin/python
#importing modules
import cgi,cgitb
import mysql.connector as mysql

#header
print "Content-type:text/html"
print ""

#getting values entered by user
data=cgi.FieldStorage()
u=data.getvalue('u')
p=data.getvalue('p')

#connecting to database
conn=mysql.connect(user='root',database='hadoop',host='localhost')
if conn.is_connected:
	print "Connection successful"
else:
	print "Something went wrong"
f=0
cur=conn.cursor()
cur.execute("select * from reg")
out=cur.fetchall()
#checking loggin details
for i in out:
	if (u==str(i[0]) and str(p)==i[1]):
		print "Logged in"
		f=1
		print "<a href =http://127.0.0.1/hadoop/clusterserv.html>"
		print "Click here to go ClusterService"
		print "<a/>"
		break
if f==0:
	print "<h2>"
	print "Invalid details"
	print "</h2>"
	print "<a href =http://127.0.0.1/hadoop/login.html>"
	print "Click here to try again"
	print "<a/>"
