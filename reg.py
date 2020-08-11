#!/usr/bin/python
import cgi,cgitb		
import mysql.connector as mysql			#importing modules

print "Content-type:text/html"
print ""					#header

data=cgi.FieldStorage()
u=data.getvalue('u')
p=data.getvalue('p')
c=data.getvalue('c')
e=data.getvalue('e')				#getting data entered by user
u1="a"
p1="a"
c1=23
e1="a"
flag=0
conn=mysql.connect(user='root',database='hadoop',host='localhost')
if conn.is_connected:
	print "Connection successful"
else:
	print "Something went wrong"		#connecting to database
cur=conn.cursor()
cur.execute("select * from reg")			#getting data from table
out =cur.fetchall()
for i in out:
	if str(i[0])==u:			#checking if uname already exists
		flag =1				
		print "<h3>"
		print "Username already in use"
		print "</h3>"
		print "<a href =http://127.0.0.1/hadoop/reg.html>"
		print "Click here to try again"
		print "<a/>"
		

if flag==0:						#inserting into table				
	cur.execute("insert into reg values('"+str(u)+"','"+str(p)+"',"+str(c)+",'"+str(e)+"')")
	conn.commit()
	print "<a href =http://127.0.0.1/hadoop/login.html>"
	print "Click here to go to login page"
	print "<a/>"


