import os
from os import listdir
import datetime
import sys
import time

import subprocess

for f in listdir("cases"):

    cmd = 'AND.exe cases/'+f
    print( cmd)
    now=datetime.datetime.now()
    start=time.time()
    r=subprocess.check_output(cmd,shell=False)
    r=str(r)
    realrootnum=len([c for c in r if r=='['])
    if realrootnum <1 :
        realrootnum=0
    else:
        realrootnum-=1
    print("real root number is: "+str(realrootnum))

    print ("time(s): "+str(time.time()-start))

