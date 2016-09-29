# fileReader for .txt
# this demonstrates how to read a file and 
# parse it using python
# from html.parser import HTMLParser
# import webbrowser

##################### comment each line please ########################
def main():
    # this will read the file
    file = open("sample.txt", "r") # r means to read the file
    # readlines will also process each line separately 
    lines = file.readlines() # this will read all the lines in the document not just a single line
    file.close() # make sure to always close the file


    #### this is where the dictionary starts########
    def tag_Maker():

    # instantiate parser and feed it some HTML
    # parserHTML = MyHTMLParser()
    # open test.html and write to it
    html_file = open("test.html", "w")
    # if html_file.mode == "w":
    #     HTMLcontents = html_file.write()
    #     parserHTML.feed('<html><head><title>This is just a Test</title></head>'o
    #                     '<body><h1>Parse me Darling!</h1><body></html>')
    html_message = ('<!DOCTYPE html><html>'
    				'<head>'
    				'<title>Needs a Title Here Senior</title>'
    				'<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />'
    				'<script src ="capstone.js"></script>'
    				'</head>')

    html_message = ('<!DOCTYPE html><html><head><title>Needs a Title Here Senior</title>'
                    '<link rel="stylesheet" type="text/css" href="style.css"></head>'
                    '<body>'
                    '<p><center><strong>Hello Capstone 2016</strong></center></p>'
                    '<center><a href= "http://www.cnn.com/2016/09/26/politics/live-updates-trump-clinton-debate/">'
                    'Useless people</a></center>'
                    '<div>'
					'<div id ="fontIncrease"><p><center><strong>Capstone Bigger Options!!!</strong></center></p></div>'
					'<!-- this is to increase the font size-->' 
					'<center><button onclick="increaseButton();">Enlarge me Darling!!!</button></center>'
					'</div>'
                    '</body></html>')
    
    html_file.write(html_message)
    

    # to look for tag identifiers
    for everyline in lines:
        everyline = everyline.strip('\n') # this will remove the extra spaces between lines

        if everyline.startswith("##"):
            tagline = everyline[3:]
            taglist = tagline.split(',')

        elif everyline:
            content = everyline.strip()
            taglist.append(content)
            # print(taglist)
            
            if taglist[0] == "Title":
                parsedTitle = taglist[1]
                print(parsedTitle)
                
        else:
            html_file.write("<" + taglist[0] + ">" + taglist[-1] + "</" + taglist[0] + ">\n")

    # display result 

    html_file.close()






if __name__ == "__main__":
    main();
