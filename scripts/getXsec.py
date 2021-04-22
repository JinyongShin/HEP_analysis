#!/usr/bin/python
import re

f = open("crossx.html",'r+')

read = f.read()

split = read.split('<tr>')


decayed = "rowspan=2" ##################### To Find Decayed Event Check the html file 

Dlist = list()

for i in split:
	if decayed in i:
		Dlist.append(i)

str2 = '\n'.join(Dlist)

list2 = str2.split('<td rowspan=2>') 	### If you want change number here to corresponding number for your event!

run = "run"

xsec = " <font face=symbol>&#177"

runlist = list()
xseclist = list()

for j in list2:
	if run in j:
		runlist.append(j)
	elif xsec in j:
		xseclist.append(j)

td = "<td>"
center = "<center>"

for k in runlist:
	if td in k:
		runlist.remove(k)
	elif center in k:
		runlist.remove(k)

href = "href"

for l in runlist:
	if href in l:
		runlist.remove(l)


runt = '\n'.join(runlist)

runlist = runt.split('<')

runt = '\n'.join(runlist)

runlist = runt.split()

t = "td"

for i in runlist:
	if t in i:
		runlist.remove(i)


runt = '\n'.join(runlist)

xsect = '\n'.join(xseclist)

xseclist = xsect.split('\n')

xsect = ';\n'.join(xseclist)

xseclist = xsect.split(';')

fuck="<center><a>"

for i in xseclist:
	if fuck in i:
		pass
	else:
		xseclist.remove(i)

xsect = '\n'.join(xseclist)

xseclist = xsect.split()

a = "a"
t = "t"
for i in xseclist:
	if a in i:
		xseclist.remove(i)
for j in xseclist:
	if t in j:
		xseclist.remove(j)
ent="ent"
for k in xseclist:
	if ent in k:
		xseclist.remove(k)

xsect = '\n'.join(xseclist)
	
Fr=open("Xsection.csv",'w+')
Fr.write("Num_run , cross section\n")
for x in range(0,len(runlist)):
	Fr.write(runlist[x]+","+xseclist[x]+"\n" )
Fr.close()
