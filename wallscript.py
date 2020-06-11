#!usr/bin/python3
#coding:utf 8 

import os,datetime,sys

username = sys.argv[1]
date = datetime.datetime.now()
hour = date.hour
rem = hour%2
hour-=rem
path = "./assets"+str(hour)+".png"
os.system("DISPLAY=:1 GSETTINGS_BACKEND=dconf gsettings set org.gnome.desktop.background picture-uri  'file://%s'" %(path))