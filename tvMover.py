import os
import sys
import shutil

curDir = os.getcwd()
print(curDir)
folders = os.listdir(curDir)

for fd in folders:
    if os.path.isdir(fd):
        print(fd)
        files = os.listdir(fd) # get file list
        os.chdir(os.path.join(curDir, fd)) # change into subdirectory
        for f in files:
            print(f)
            #fp, fn = os.path.split(f)
            try:
                shutil.move(f, curDir)
            except:
                pass # just skip if already exists in curDir
            
        os.chdir(curDir) # return to parent directory

