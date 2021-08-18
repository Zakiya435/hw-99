import time,os,shutil
path = "C:/Users/HAKPILOT/Desktop/Trash"
days = 1
c = 0
seconds = time.time()- (days * 24 * 60 * 60)
isExist = os.path.exists(path)
if isExist == True:
    allList = os.listdir(path)
    allFiles = os.walk(path)
    for i in allList:
        joined = os.path.join(path,"/"+allList[c])
        c=c+1
        status = os.stat(path).st_ctime
        if status > seconds:
            if os.path.isfile(joined):
                os.remove(joined)
            elif os.path.isdir(joined):
                shutil.rmtree()
elif isExist == False:
    print("Path not found")