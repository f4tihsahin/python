import os
os.chdir("C:\\PentestBox\\base\\python")
if (os.path.isfile('python.exe')):
    os.rename('python.exe','python27.exe')
    print("1. İŞLEM TAMAM")
else:
    pass
    print ("OLMADI")

os.chdir("C:\\Users\\root\\Anaconda3")
if (os.path.isfile('python37.exe')):
    os.rename('python37.exe','python.exe')
    print("2. İŞLEM TAMAM")
else:
    pass
    print ("OLMADI")
