#!/usr/bin/python
1;4205;0cimport sys
import os
from time import clock
import time

from os import listdir
from os.path import isfile, join



import timelimitexecution

timeout=600 # timeout



def listAllDirectories(path):
    onlyDirectories = [join(path,f) for f in listdir(path) if not isfile(join(path, f))]

    return onlyDirectories


def runOneClassBenchMark(path, SLV):
    print path
    fileList=[]
    output=open(path+"/result.csv","w+")
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(".dat"):
                fileList.append(os.path.join(root, f))
                
    fileList.sort()
    for fullfilename in fileList:
        print fullfilename
        start=time.time()
        command=SLV+" -f  "+fullfilename
        fileNames=fullfilename.split('/')
        fileName=fileNames[len(fileNames)-1]
        baseName=fileName.split('.')[0]
        result=baseName+", >"+str(timeout)+"\n"
        if timelimitexecution.run_with_limited_time(os.system,(command, ),{}, timeout):
            result=baseName+","+str(time.time()-start)+"\n"
        else:
            
            os.system("killall "+SLV.split('/')[-1])
            print "timeout "
        output.write(result)

    output.close()       
    

if __name__ == '__main__':
    if  len(sys.argv)<3:
        exit()

    SLV=sys.argv[1]
    inputs=sys.argv[2]
    
    DirecList=listAllDirectories(inputs)
    
    for dirs in  DirecList:
        runOneClassBenchMark(dirs, SLV)

    