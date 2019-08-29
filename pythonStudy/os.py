import os

path = input("请输入文件路径:")

filelist = os.listdir(path)

n = 0
for i in filelist:
    oldname = path + os.sep + filelist[n]
    newname = path + os.sep +'a' + str(n+1)

    os.rename(oldname, newname)
    print(oldname, '====>', newname)

    n+=1
print(filelist)