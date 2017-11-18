#!/usr/bin/env python
import urllib
import os
import platform
import shutil

#get html content
r = urllib.urlopen('http://zeus.softweek.net/item-slt-1.html')

for line in r:
    if line.find('GOOGLE HOSTS') >= 0:
        url = line[line.find('http://'):][:line[line.find('http://'):].find('"')]

#set hosts path
if platform.system() == 'Windows':
    sysdir = os.getenv('SystemDrive')
    hostspath = sysdir + '/windows/system32/drivers/etc/hosts'
if platform.system() == 'Linux':
    hostspath = '/etc/hosts'

#backup hosts file
if os.path.isfile(hostspath+'_bak') == False:
    shutil.copyfile(hostspath,hostspath+'_bak')
shutil.copyfile(hostspath+'_bak',hostspath)

#start add
host = open(hostspath,'r')
content = host.read()
host.close()
r = urllib.urlopen(url)

#add file
for line in r:
    line=line.strip('\n')
    content = content + line
    
host = open(hostspath,'w')
host.write(content)
host.close()
