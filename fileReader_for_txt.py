# fileReader for .txt
# this demonstrates how to read a file and 
# parse it using python
# from html.parser import HTMLParser
# import webbrowser

##################### comment each line please ########################

#### this is where the dictionary starts########
dict_tag = {'Title':['<title>', '</title>'],'Header': ['<h1>','</h1>'],'Header-medium':['<h2>','</h2>'],
            'Header-small':['<h3','</h3>'],'Header-center':['<h1 class="center">', '</h1>'], 
            'Header-medium-center':['<h2 class="center">', '</h2>'],
            'Header-small-center':['<h3 class="center">', '</h3>'],'Link':['<a href="', '">', '</a>'],
            'PP':['<p>','</p>'], 'PP-center':['<p class="center">', '</p>'],
            'PP-right':['<p class="right">', '</p>'], 
            'List':['<ul style="list-style-type:none;">', '<li>', '</li>','</ul>'],
            'List-dotted':['<ul>', '<li>', '</li>','</ul>'],'List-number':['<ol>', '<li>', '</li>','</ol>'], 
            'Quote': ['<blockquote>','</blockquote>'], 
            'Quote-person': ['<blockquote>', '<footer>', '</footer>', '</blockquote>']
            }

# hard_tags list 
hard_tags = ['List','List-dotted','List-number','Quote-person', 'Link']  


def reader(line):
    if line.startswith("##"): # finds tags in sample.txt
        tag = line[3:]

    elif line: #finds content that is not a tag
        content = line.strip()
        
    else: # puts things together on empty lines           

        if tag in dict_tag: # checks for valid tags
            new_tag = dict_tag[tag] #finds HTML value 
            print(new_tag)
                
            open_tag = new_tag[0]
            close_tag = new_tag[-1]

            if tag in hard_tags: # if a hard tag use hard_tag()
                hard_tag(tag)

            else:    
                print(open_tag + content + close_tag + '\n')


def hard_tag(t):
    # link tags
    if t == 'Link':
        content = content.split(',')
        url, txt = content[0], content[1]
        print(open_tag + url + new_tag[1] + txt + close_tag + '\n')

    # list tags
    elif (t == 'List') or (t == 'List-dotted') or (t == 'List-number'):
        print(open_tag + '\n')
        content = content.split('\n')
        for i in content:
            print(new_tag[1] + i + new_tag[2] + '\n')
        print(close_tag)

    # quote tags
    elif t == 'Quote-person':
        content = content.split('\n')
        person, words = content[0], content[1]
        print(open_tag + words + new_tag[1] + person + new_tag[2] + close_tag)



def main():
    file = open("sample.txt", "r") # this will read the file
    # readlines will also process each line separately 
    lines = file.readlines() # this will read all the lines in the document not just a single line
    file.close() # make sure to always close the file 

    # open test.html and write to it
    html_file = open("test.html", "w")

    html_message = ('<!DOCTYPE html>\n'
                    '<html>\n'
                    '<head>\n'
                    '<title>Needs a Title Here Senior</title>\n'
                    '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n'
                    '<link rel="stylesheet" type="text/css" href="style.css">\n</head>\n'
                    '<script src ="capstone.js"></script>\n'
                    '<body>\n'
                    '<p class="center"><strong>Hello Capstone 2016</strong></center></p>'
                    '<center><a href= "http://www.cnn.com/2016/09/26/politics/live-updates-trump-clinton-debate/">'
                    'Useless people</a></center>'
                    '<div>'
                    '<div id ="fontIncrease"><p>Make me Bigger!!!</p></div>'
                    '<!-- this is to increase the font size-->' 
                    '<button onclick="increaseButton();">Embiggen</button>'
                    '</div>')
 
    html_file.write(html_message)
    

    # to look for tag identifiers
    for everyline in lines:
        everyline = everyline.strip('\n') # this will remove the extra spaces between lines
        reader(everyline) # calls reader() to write html 

    # end HTML

    html_file.write('\n</body>\n</html>')
    html_file.close()






if __name__ == "__main__":
    main();
