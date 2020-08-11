#!/usr/bin/python

#importing modules
import cgi,cgitb,commands
cgitb.enable()

#header
print "Content-type:text/html"
print ""

#getting value entered by the user
data=cgi.FieldStorage()
n=data.getvalue('fn')
r=data.getvalue('r')
bs=data.getvalue('bs')
fbs=int(bs)*1024*1024

#uploading file
print commands.getoutput("sudo ssh nn1 '/hadoop2/bin/hdfs dfs -Ddfs.replication="+r+" -Ddfs.block.size="+str(fbs)+" -put "+n+" /project'")
print "<h2>"
print "File uploaded"
print "</h2>"
	

