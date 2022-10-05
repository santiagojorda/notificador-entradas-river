import os 

def getFileLines(nameFile):
    file = open(nameFile, 'r')
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    file.close()
    return lines

def writeAtTheEnd(nameFile, message):
    file = open(nameFile, 'r+')
    file.seek(0, 2)
    file.write(message)
    file.close()

def fileFirstLinesRemover(nameFile, lines, numberOfLines):
    os.remove(nameFile)
    file = open(nameFile, 'w')
    for i in range(len(lines)):
        if(i >= numberOfLines):
            file.write(lines[i]+'\n')
    file.close()