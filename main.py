import time
import glob
import wget
import os
import requests
import shutil



# Starts a while loop to look for file updates within the upload folder
#
# Saves the old len of of the directory to get a base number
#
# Within the while loop it sleeps then looks for a any new files in the directory
#
# Once theres a change between oldNumber and newNumber then it runs the newest file
#
# #
def lookForFile():
    emptyFolder()
    localFiles = getLocalFiles()
    while len(localFiles) == 0:
        os.system('python led_waiting.py')
        print("Init Loop")
        toDownload = compareNewFile()
        localFiles = getLocalFiles()
        downloadFiles(toDownload)
        localFiles = getLocalFiles()

    localFiles = getLocalFiles()
    updater(0)
    while True:
        print("RunLoop")
        os.system('python led_waiting.py')
        localFiles = getLocalFiles()
        if not len(compareNewFile(localFiles))==0:
            downloadFiles(compareNewFile(localFiles))
            localFiles = getLocalFiles()
        if updateRobot():
            num = getCurrentNumber()
            updater(num)
            runScript(num)
#Emptys the folder besides those starter files to start a new session
def emptyFolder():
    files = glob.glob('upload/*')
    Restricted = ['upload/PCA9685.py','upload/Motor.py','upload/__pycache__']
    for f in files:
        print(f)
        if not f in Restricted:
            os.remove(f)
    url = "http://pleasework.csh.rit.edu/empty.php"
    requests.get(url)

#Downloads all the scripts withing the download List
def downloadFiles(downloadList=[]):
    for i in downloadList:
        downloadScript(int(i.replace('.py', '')))
    time.sleep(5)

#Checks for all the files in the upload excluding any needed files
def getLocalFiles():
    localFiles = glob.glob('./upload/*')
    localFiles = [s[9:] for s in localFiles]
    if "Motor.py" in localFiles:
        localFiles.remove('Motor.py')
    if "PCA9685.py" in localFiles:
        localFiles.remove('PCA9685.py')
    if "__pycache__" in localFiles:
        localFiles.remove('__pycache__')
    return localFiles

#
#def getSubmittedAmount():
#    url = "http://pleasework.csh.rit.edu/data.json"
 #   response = requests.get(url)
 #   json = response.json()
 #   return json["amountSubmitted"]

#Gets the current number of the 
def getCurrentNumber():
    url = "http://pleasework.csh.rit.edu/data.json"
    response = requests.get(url)
    json = response.json()
    return json["currentlyRunning"]


##
# Goes to the robot.php file which checks to see if its on the current running file.
#
# If page contains only "CurrentlyRunning" return none
#
# If page has json return the number for the file
# #

def updateRobot():
    url = "http://pleasework.csh.rit.edu/robot.php"

    response = requests.get(url)
    num = response.text
    if not response.text == "Running current":
        return True
    return False


def updater(fileNum):
    url = "http://pleasework.csh.rit.edu/justRan.php?id="+str(fileNum)
    requests.get(url)



#Compares a all the local files with all the uploaded files to see what the local folder is missing
def compareNewFile(locals=[]):
    uploadedFile = set(getKeys())
    localFiles = set(locals)

    return (uploadedFile - localFiles).union(localFiles - uploadedFile)

#Gets keys from the files in the data json
def getKeys():
    url = 'http://pleasework.csh.rit.edu/data.json'
    a = requests.get(url)
    a = a.json()
    a = a["files"]
    if len(a) ==0:
        return []
    myString = ".py"
    b = [s + myString for s in a.keys()]
    return b


def execfile(scriptName):
    pass


def runScript(scriptName):
    os.system('python ./upload/'+(str(scriptName)+'.py'))
##
# Connects to url of the correct file
#
# Downloads it to upload
#
def downloadScript(fileNum):

    url = "http://pleasework.csh.rit.edu/uploads/{}.py".format(fileNum)

    #time.sleep(5)

    wget.download(url, './upload/')
    time.sleep(5)


def main():
    lookForFile()


if __name__ == "__main__":
    main()
