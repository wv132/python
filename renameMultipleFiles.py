# Pythono3 code to rename multiple 
# files in a directory or folder 

# importing os module 
import os

# Function to rename multiple files
def main():
    StartText = """This program will rename files which are in reverse
    Once you entered the right path the program will collect all the files in that path, reverse the filename and rename it."""
    print(StartText)

    #Ask for the filepath input from the user and change directory to the given file path
    os.chdir(input("what is the path of the files you want to rename: "))
    
    #Loop over every file in the directory
    for file in os.listdir():
        #split the filename from the file extention
        fileName, fileExt = os.path.splitext(file)
        #Take only the filename without the fileextention
        my_source = str(fileName)
        #Reverse the sourcefilename withouut thew extention and set it as the destination filename
        my_dest = my_source[::-1]+fileExt

        os.rename(file, my_dest)

        print('{} --> {}'.format(file,my_dest))


if __name__ == '__main__':
   # Calling main() function
   main()
