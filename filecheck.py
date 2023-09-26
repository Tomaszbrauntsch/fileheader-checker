# Created By: Tomasz Brauntsch

from hexdump import hexdump
import io # allows for text manipulation of bytes
import json # used to look at the magicnumbers
import re # used for comparsion of file headers in json file
import sys # used to read arguments
def byteExtraction(fileName):
    photoBytes = [] #used later for extracting bytes from data
    bytesString = ""
    
    photo = open(fileName, "rb")
    photoRaw = io.StringIO(str(hexdump(photo.read()))) # reads the file, hexdumps it, converts it into a StringIO buffer
    for x in range(0,2): # maybe increase the end value of range if it the range is too small for specific file headers
        dataParsed = (photoRaw.readline()).split(" ")
        dataParsed = dataParsed[1:len(dataParsed)-1]
        for byte in dataParsed:
            if(byte != ''):
                photoBytes.append(byte)

    for x in range(0, len(photoBytes)):
        if(x%2 == 0 and x != 0):
            bytesString += " "
        bytesString += str(photoBytes[x]) 

    # print(bytesString) # uncomment this to see what the first two strings of file headers from your file are 
    photo.close()
    return bytesString

def byteChecker(fileName):
    extractedBytes = byteExtraction(fileName)
    fileExt = fileName.split(".")[-1]
    with open("magicnums.json") as magicFile:
        magicNumbers = json.loads(magicFile.read())
    found = 0 # if the file header is found (default file header is not found)
    fileHeadersReference = magicNumbers["magicNumbers"][0][str(fileExt)]
    if (type(fileHeadersReference) == list): # checks if the file header in the reference has more than one file header since it needs a different process
        for fileHeader in fileHeadersReference:
            if(re.search(fileHeader, extractedBytes)):
                found = 1
                break

    elif (type(fileHeadersReference) == str):
        if(re.search(fileHeadersReference, extractedBytes)):
            found = 1
    else:
        print("This file extension is either not in our database or doesn't exist!")
    
    if (found == 1):
        print("This file is correct :: " + str(fileExt))
    elif(found == 0):
        print("The file is either corrupted or the wrong file extension")

def main():
    try:
        fileName = sys.argv[1]
        byteChecker(fileName)
    except IndexError:
        print("MISSING ARG ERROR: Please include a file as an argument!")
        exit(2) #missing arg error
    except FileNotFoundError:
        print("INVALID FILE ERROR: Please include a valid file!")
        exit(3) #invalid file error
    

main()