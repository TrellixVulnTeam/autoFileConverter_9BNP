import os, time, subprocess, sys


# This initializes an empty list that as the script walks through the directory, it adds the file name to the list to feed into handbrake
fileList = []

# This asks for you to input a directory that you want the script to walk through
rootdir = input("root Dir: ")

# For each root directory, subfolder, and file in the specified directory, it will look for files that end in your desired file type
for root, subFolders, files in os.walk(rootdir):
    for file in files:
        # Creates the variable that joins the root directory to the file name so the full file name is added to the fileList
        theFile = os.path.join(root,file)
        # Splits the Extension from the fileName to see if the Extension matches the search
        fileName, fileExtension = os.path.splitext(theFile)
        # Compares extensions to the ones that you're looking for to convert
        if fileExtension.lower() in ('.avi', '.mkv'):
            # If the fileExtension is in this list, it will add the file to the list
            print('Adding',theFile)
            fileList.append(theFile)


# This is the string that feeds into the Handbrake Program with all of the options that you would normally tweak in the GUI version
# -i is input, and takes the first file name that the list feeds to it, the variable is inFile
# -o is output and takes the outputted video file, the variable is outFile
# -e Encoder options are x264, x265, mpeg4, mpeg2, VP8, VP9, theora
# -q This is the adjustment for the quality slider
# --audio-lang-list is a little tricky as sometimes a file will download with an english audio track, but it will show up as "unknown language"
# by putting eng,und in the list it will check to see if any of the audio tracks match those and will use the first one that matches in the final file
runstr = '"C:\\Program Files\\HandBrake\\HandBrakeCLI.exe" -i "{0}" -o "{1}" -e "x264" -q 27.0 --audio-lang-list eng,und --first-audio'

# This is just to make the whole deal look a little cleaner when it runs
print('============--------============')

# While there are still items in fileList, it will take the next file and run the file through handbrake, remove the item from the list
# and then delete the original file before moving on to the next item
while fileList:
    # Pops the next file off the top of the list and makes it the input file for handbrake
    inFile = fileList.pop()
    # Splits the original file extension off of the file name
    fileName, fileExtension = os.path.splitext(inFile)
    # Adds the desired file extension to the end of the file name
    # Since you can't have two files with the same name in a folder, I've found it easier to just make all new files .mp4 so there's no fuss
    # about same file names and it lets you know when files have already been converted
    outFile = fileName+'.mp4'

    print('Processing',inFile)
    # Runs the Handbrake CLI function with the designated options in the runstr variable
    # inFile and outFile replace the {0} and {1} in the runstr variable
    returncode = subprocess.call(runstr.format(inFile,outFile))
    # When the file is done the program sleeps for a moment before moving on
    time.sleep(5)
    # Removes inFile from the working list
    print('Removing',inFile)
    # Deletes the inFile from storage leaving the converted item in its place.
    os.remove(inFile)