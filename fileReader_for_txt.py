# fileReader for .txt
# this demonstrates how to read a file and 
# parse it using python

##################### comment each line please ########################
def main():
    # this will read the file
    file = open("sample.txt", "r") # r means to read the file
    # readlines will also process each line separately 
    lines = file.readlines() # this will read all the lines in the document not just a single line
    file.close() # make sure to always close the file

    # to look for patterns
    for everyline in lines:
        everyline = everyline.strip() # this will remove the extra spaces between lines
        print (everyline)
    # display result 
main()
