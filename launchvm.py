#!/usr/bin/python

#importing modules
import cgi,cgitb,commands,time
cgitb.enable()

#header
print "Content-type:text/html"
print ""

#getting value entered by the user
data=cgi.FieldStorage()
n=data.getvalue('c')
n1=int(n)
dn=data.getvalue('dn')
mr=data.getvalue('mr')
print "<h2>"
print "Starting namenode machine   "
print "</h2>"
#Starting namenode machine
out=commands.getoutput('sudo virsh start nn1')				
print out

#Starting datanode machines
for i in range(n1):
	print "<h2>"
	print "Starting vm   "+str(i)
	print "</h2>"
	out=commands.getoutput('sudo virsh start dn'+str(i))
	print out
	print "</br>"

print "</br>"
print "</br>"
time.sleep(30)
#Running playbook files
x=i+1
if dn=="y":
	print commands.getoutput('sudo ansible-playbook launchdno.yml --limit "'+str(x)+'dn,nn"')
if mr=="y":
	print commands.getoutput('sudo ansible-playbook launchmro.yml --limit "'+str(x)+'dn,nn"')
print "</br>"
print "</br>"
print "</br>"
print "</br>"

print "<a href='http://192.168.122.22:50070'>"
print "Click here to go to the portal"
print "</a>"

if dn=='y':
	print "<a href='http://127.0.0.1:/hadoop/upload.html'>"
	print "<h2>"
	print "Upload a file"
	print "</h2>"
	print "</a>"


if mr=='y':
	print "<a href='http://127.0.0.1:/hadoop/yarn.html'>"
	print "<h2>"
	print "YARN"
	print "</h2>"
	print "</a>"



