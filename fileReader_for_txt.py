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

    dict_tag = {'Title':'title', 'Header': 'h1','Header-medium':'h2','Header-small':'h3',
                'Header-center':['h1', 'style="text-align:center;"'], 'Header-medium-center':['h2', 'style="text-align:center;"'],
                'Header-small-center':['h3', 'style="text-align:center;"'], 'PP':'p', 'PP-center':['p', 'style="text-align:center;"'],
                'PP-right':['p', 'style="text-align:right;"'], 'List':['ul', 'style="list-style-type:none;"', 'li'],
                'List-dotted':['ul', 'li'],'List-number':['ol', 'li'], 'Quote': 'blockquote', 'Quote-person': ['blockquote', 'footer'],
                'Link':'a'}

    # open test.html and write to it
    html_file = open("test.html", "w")



    #### this is where the dictionary starts########
    # def tag_Maker():

    # instantiate parser and feed it some HTML
    # parserHTML = MyHTMLParser()
    # open test.html and write to it
    html_file = open("test.html", "w")
    # if html_file.mode == "w":
    #     HTMLcontents = html_file.write()
    #     parserHTML.feed('<html><head><title>This is just a Test</title></head>'o
    #                     '<body><h1>Parse me Darling!</h1><body></html>')

    html_message = ('<!DOCTYPE html>'
                    '<html>'
                    '<head>'
                    '<title>Needs a Title Here Senior</title>'
                    '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />'
                    '<link rel="stylesheet" type="text/css" href="style.css"></head>'
                    '<script src ="capstone.js"></script>'
                    '<body>'
                    '<p><center><strong>Hello Capstone 2016</strong></center></p>'
                    '<center><a href= "http://www.cnn.com/2016/09/26/politics/live-updates-trump-clinton-debate/">'
                    'Useless people</a></center>'
                    '<div>'
                    '<div id ="fontIncrease"><p>Make me Bigger!!!</p></div>'
                    '<!-- this is to increase the font size-->' 
                    '<button onclick="increaseButton();">Embiggen</button>'
                    '</div>'
                    '</body>'
                    '</html>')
 
    html_file.write(html_message)
    html_file.close()
    

    # to look for tag identifiers
    for everyline in lines:
        everyline = everyline.strip('\n') # this will remove the extra spaces between lines

        if everyline.startswith("##"):
            tag = everyline[3:]

        elif everyline:
            content = everyline.strip()
                
<<<<<<< HEAD
        # else:
        #     html_file.write("<" + taglist[0] + ">" + taglist[-1] + "</" + taglist[0] + ">\n")
=======
        else:
            if tag in dict_tag:
                new_tag = dict_tag[tag]
                
                if isinstance(new_tag, list):
                    html_tag = new_tag[0]
                else:
                    html_tag = new_tag

                # print(html_tag)
            html_file.write("<" + html_tag + ">" + content + "</" + html_tag + ">\n")
>>>>>>> c6f195c33d6ffdcd89c5fd19578dc7371446c47e

    # display result 







if __name__ == "__main__":
    main();
