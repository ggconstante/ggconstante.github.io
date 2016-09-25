# fileReader for .txt
# this demonstrates how to read a file and 
# parse it using python
<<<<<<< HEAD

# import the HTMLParser module
from HTMLParser import HTMLParser
=======
# from HTMLParser import html.parser
>>>>>>> b74d7e8fac200e4c9ff28d7a4e6057b9ea214b6d
##################### comment each line please ########################
def main():
    # this will read the file
    file = open("sample.txt", "r") # r means to read the file
    # readlines will also process each line separately 
    lines = file.readlines() # this will read all the lines in the document not just a single line
    file.close() # make sure to always close the file

    html_file = open("test.html", "w")
    html_message = 
    """
    <html>
    <head></head>
    <title>"Needs a Title Here Senior"</title>
    <body>
        <p>"Hello Capstone 2016"</p>
    </body>
    </html>
    
    """
    html_file.write(html_message)
    html_file.close()

    # to look for patterns
    for everyline in lines:
<<<<<<< HEAD
        everyline = everyline.strip().split() # this will remove the extra spaces between lines
        print (everyline)
=======
        everyline = everyline.strip() # this will remove the extra spaces between lines
        # print(everyline)

        if everyline.startswith("##"):
            everyline = everyline[3:]
            taglist = everyline.split(",")
            htmlitem = taglist[0]
            print(htmlitem)


            


>>>>>>> b74d7e8fac200e4c9ff28d7a4e6057b9ea214b6d
    # display result 
main()
