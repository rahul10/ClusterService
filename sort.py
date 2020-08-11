#!/usr/bin/python

#importing modules
import cgi,cgitb,commands,time
cgitb.enable()

#header
print "Content-type:text/html"
print ""

#getting value entered by the user
data=cgi.FieldStorage()
n=data.getvalue('fn')
slash="/"
#checking if file exists
flag =0
out=commands.getoutput("sudo ssh dn  'hdfs dfs -ls /project | grep "+n+" | cut -d "+slash+" -f3'")
print out
print n
if out==n:
	flag=1
if flag==0:
	print "<h2>"
	print "File not present"
	print "</h2>"

#Running process
if flag==1:
	print commands.getoutput("sudo ssh dn 'yarn jar /hadoop2/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar sort /project/"+n+" /output1'")
	print "<h2>"
	print "You can check the output in the output folder"
	print "</h2>"
	
