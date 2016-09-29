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
    dict_tag = {'Title':'title', 'Header': 'h1','Header-medium':'h2','Header-small':'h3',
                'Header-center':['h1', 'style="text-align:center;"'], 'Header-medium-center':['h2', 'style="text-align:center;"'],
                'Header-small-center':['h3', 'style="text-align:center;"'], 'PP':'p', 'PP-center':['p', 'style="text-align:center;"'],
                'PP-right':['p', 'style="text-align:right;"'], 'List':['ul', 'style="list-style-type:none;"', 'li'],
                'List-dotted':['ul', 'li'],'List-number':['ol', 'li'], 'Quote': 'blockquote', 'Quote-person': ['blockquote', 'footer'],
                'Link':'a'}

    # save hard_tags list for later
    hard_tags = ['Header-center','Header-medium-center','Header-small-center','PP-center','PP-right','List','List-dotted','List-number'
                'Quote-person']   


    # def tag_maker():


    # open test.html and write to it
    html_file = open("test.html", "w")

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

        if everyline.startswith("##"): # finds tags in sample.txt
            tag = everyline[3:]

        elif everyline: #finds content that is not a tag
            content = everyline.strip()
                
        else: # puts things together on empty lines
            if tag in dict_tag: 
                new_tag = dict_tag[tag] #finds HTML value from sample.text key

                if isinstance(new_tag, list):  #if value is a list, make html_tag first list item
                    html_tag = new_tag[0]
                else:
                    html_tag = new_tag  #if value is just a str

                # hard tags - CENTERS
                if (tag == 'Header-center') or (tag == 'Header-medium-center') or (tag == 'Header-small-center') or (tag == 'PP-center'):
                    print("<" + html_tag + " " + new_tag[1] + ">" + content + "</" + html_tag + ">\n")

                # hard tags - RIGHTS
                elif tag == 'PP-right':
                    print("<" + html_tag + " " + new_tag[1] + ">" + content + "</" + html_tag + ">\n")    

                # hard tags - LISTS
                # elif (tag == 'List') or (tag == 'List-number') or (tag == 'List-dotted'):
                    # FIX THIS print("<" + html_tag + " " + new_tag[1] + ">" + content + "</" + html_tag + ">\n")

                # hard tags - QUOTES
                # elif tag == 'Quote-person':
                    # FIX THIS print("<" + html_tag + " " + new_tag[1] + ">" + content + "</" + html_tag + ">\n")

                # print only works for easy tags
                else:
                    print("<" + html_tag + ">" + content + "</" + html_tag + ">\n")


     
    # end HTML
    html_file.close()






if __name__ == "__main__":
    main();
