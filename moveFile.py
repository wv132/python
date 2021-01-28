import os
import shutil

startText = """
This program will move content from one folder to another folder.
-   Enter a sourcepath. This is the path where all the content are that you want to move.
-   Enter a targetpath. This is the path that you want your content to move to.
        NOTE - if you enter a targetpathname that doesnt exist, the program will create that path for you.

"""
print(startText)

sourcePath = input("Enter - the sourcePath: ")#r"C:\Users\WV\Desktop\testingPython\new folder"
targetPath = input("Enter - the targetPath: ")#r"C:\Users\WV\Desktop\testingPython\new"

pathSeparator = "\\"

os.chdir(sourcePath)
count = 0

for file in os.listdir():
       
    f_sourcePath = sourcePath+pathSeparator+file
    f_targetPath = targetPath+pathSeparator+file
    shutil.move(f_sourcePath,f_targetPath)
    print("Moving file succesfull. "+file)
    count += 1

print("total files moved: "+str(count))

