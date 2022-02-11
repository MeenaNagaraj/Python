#OS Module
#to perform OS-based tasks and get related information about operating system.

import os


#1. os.name() - provides name of the OS module that it imports.
# it registers 'posix', 'nt', 'os2', 'ce', 'java' and 'riscos'
print(os.name)      #o/p: nt

#2. os.mkdir() - to create new directory
#os.mkdir("F:\\New Dir")     #F:\New Dir - new dir created to the path in the string arg of function

#3. os.makedirs() - creates a directory recursivel -subdirectory
#os.makedirs("F:/Python Program/OS/new")

#4. os.getcwd() - returns Current Working Directory of the file
print(os.getcwd())  #o/p:F:\Python Program\Task

#5. os.chdir() - to change CWD
'''
os.chdir("F:\Python Program\OS")
print(os.getcwd())              #o/p:F:\Python Program\OS
'''

#6.os.listdir() - returns a list of all files and folders present inside the specified directory
print(os.listdir("F:\Python Program")) #o/p:['hellow.py', 'IfElse-HackerRankTask.py', 'Interview', 'OS', 'Project','Task']

#7.os.rename() - file or directory can be renamed
#os.rename("test.txt","myfile.txt")  #file name "test" is changed into "myfile"

#8.os.rmdir()- used to remove or delete an empty directory.
#can't remove CWD. To remove it, should change the cwd.
'''
os.chdir("..")
os.rmdir("F:\Python Program\OS")    # Directory OS deleted
'''

#9. os.removedirs() - remove directories recursively
#os.removedirs("F:/Python Program/OS/new")   #removed

#10. os.stat() -  used to get status of the specified path
print(os.stat("myfile.txt"))
'''
o/p: os.stat_result(st_mode=33206, st_ino=1125899906903626, st_dev=43076344,
st_nlink=1, st_uid=0, st_gid=0,st_size=0, st_atime=1644561926,
st_mtime=1644558990, st_ctime=1644558990)
'''

#11. os.walk()-a generator that creates a tuple of values (dirpath, dirnames, filenames)
for dirpath,dirname,filename in os.walk("F:\Python Program\Project"):
    print("DirPath:",dirpath)
    print("DirName:",dirname)
    print("FileName:",filename)
'''
o/p:
DirPath: F:\Python Program\Project
DirName: []
FileName: ['mini.py', 'Miniproject1-RockPaperScissor.py']
'''

