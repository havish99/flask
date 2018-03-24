#!/usr/bin/env python
import os
from flask import Flask,redirect,url_for,request

k=os.popen("arp -n | grep C | sed 's/ .*//' > ip_add")
filename="ip_add"
d={}
l=[]
a=[]
file=open(filename,"r")
for line in file:
	line=line.split(".")
	l.append(int(line[3]))
k=os.popen("iw dev wlan0 station dump | grep avg > rssi").read().split(" ")
file=open("rssi","r")
for line in file:
	k=line.split(" ")
	a.append(k[2].strip("[]"))
a=a[::-1]
for i in range(0,len(a)):
	d['1'+str(l[i])]=int(a[i])


