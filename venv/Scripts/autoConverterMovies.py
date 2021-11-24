import os, time, subprocess, sys

fileList = []
rootdir = input("root Dir: ")
for root, subFolders, files in os.walk(rootdir):
    for file in files:
        theFile = os.path.join(root, file)
        fileName, fileExtension = os.path.splitext(theFile)
        if fileExtension.lower() in ('.avi', '.mkv'):
            print('Adding', theFile)
            fileList.append(theFile)

runstr = '"C:\\Program Files\\HandBrake\\HandBrakeCLI.exe" -i "{0}" -o "{1}" -e "x264" -q 24.0 --audio-lang-list eng,und --first-audio'

print('============--------============')

while fileList:
    inFile = fileList.pop()
    fileName, fileExtension = os.path.splitext(inFile)
    outFile = fileName + '.mp4'

    print('Processing', inFile)
    returncode = subprocess.call(runstr.format(inFile, outFile))
    time.sleep(5)
    print('Removing', inFile)
    os.remove(inFile)