# fileReader for .txt
# this demonstrates how to read a file and 
# parse it using python
<<<<<<< HEAD
import webbrowser

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

# create a subclass and override the handlers
class MyHTMLParser(HTMLParser):

    def __init__(self):
        # this is in progress
        self.reset()
        self.newTags = []
        self.newAttrs = []
        self.htmlData = []
        # this is in progress

    def for_comments(self, comment): # this is gonna the data inside that comment section 
        print "Encountered comment", comment
        pos_comment = self.getpos() # getpos comes back with a line number and a character number position in the data
        print "At line: ", pos_comment[0], "position ", pos_comment[1]

    def for_startTags(self, start_tag):
        print "Encountered an end tag: ", start_tag
        pos_startTag = self.getpos()
        print "At line: ", pos_startTag[0], "position ", pos_startTag[1]

    def for_endtags(self, end_tag):
        print "Encountered an end tag: ", end_tag
        pos_endTag = self.getpos()
        print "At line: ", pos_endTag[0], "position ", pos_endTag[1]

    def for_data(self, data):
        print "Encountered an end tag: ", data
        pos_data = self.getpos()
        print "At line: ", pos_data[0], "position ", pos_data[1]

    # instantiate parser and feed it some HTML
    parserHTML = MyHTMLParser()
    # open test.html and write to it
    html_file = open("test.html", "w")
    if html_file.mode == "w":
        HTMLcontents = html_file.write()
        parserHTML.feed('<html><head><title>This is just a Test</title></head>'
                        '<body><h1>Parse me Darling!</h1><body></html>')

    """html_message = 
    
    <html>
    <head></head>
    <title><h1>Needs a Title Here Senior</h1></title>
    <h2></h2>
    <h3></h3>
    <body>
        <p>"Hello Capstone 2016"</p>
    </body>
    </html>
    
    html_file.write(html_message)
    html_file.close()
    """

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

if __name__ == "__main__":
    main();