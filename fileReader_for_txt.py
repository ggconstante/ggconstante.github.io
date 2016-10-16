# fileReader for .txt
# this demonstrates how to read a file and 
# parse it using python
import os

##################### comment each line please ########################

######## tag id dictionary and list ########
dict_tag = {'Title':['<title>', '</title>'],'Header': ['<h1>','</h1>'],'Header-medium':['<h2>','</h2>'],
            'Header-small':['<h3>','</h3>'],'Header-center':['<h1 class="center">', '</h1>'], 
            'Header-medium-center':['<h2 class="center">', '</h2>'],
            'Header-small-center':['<h3 class="center">', '</h3>'],'Link':['<a href="', '">', '</a>'],
            'PP':['<p>','</p>'], 'PP-center':['<p class="center">', '</p>'],
            'PP-right':['<p class="right">', '</p>'], 
            'List':['<ul style="list-style-type:none;">', '<li>', '</li>','</ul>'],
            'List-dotted':['<ul>', '<li>', '</li>','</ul>'],'List-number':['<ol>', '<li>', '</li>','</ol>'], 
            'Quote': ['<blockquote>','</blockquote>'], 
            'Quote-person': ['<blockquote>', '<footer>', '</footer>', '</blockquote>'], 'Image':['<img src="', '"\>'],
            'Image':['<img src="', '"/>']
            }

hard_tags = ['List','List-dotted','List-number','Quote-person', 'Link']  


######## read/write functions ########
def header(t, c, f):
    if t in dict_tag and t == 'Title': # checks for valid tags
        new_tag = dict_tag[t] #finds HTML value  
        open_tag = new_tag[0]
        close_tag = new_tag[-1]

        f.write('<!DOCTYPE html>\n<html>\n<head>\n'
                '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n'
                '<link rel="stylesheet" type="text/css" href="style.css">\n')
        f.write(open_tag + c + close_tag + '\n</head>\n\n<body>\n')

    else:
        reader(t, c, f)


def reader(t, c, f):
    if t in dict_tag and t != 'Title': # checks for valid tags
        new_tag = dict_tag[t] #finds HTML value  
        open_tag = new_tag[0]
        close_tag = new_tag[-1]

        if t in hard_tags: # if a hard tag use hard_tag()
            hard_tag(t, c, f)

        else:    
            f.write(open_tag + c + close_tag + '\n')

    else: #invalid tag
        print('Error: ' + t + ' is an invalid tag\nView elements.txt for reference')


def hard_tag(t, c, f):
    if t in dict_tag: # checks for valid tags
        new_tag = dict_tag[t] #finds HTML value  
        open_tag = new_tag[0]
        close_tag = new_tag[-1]

    # link tags
    if t == 'Link':
        c = c.split(',')
        url, txt = c[0], c[1]
        f.write(open_tag + url + new_tag[1] + txt + close_tag + '\n')

    # list tags
    elif t.startswith('List'):
        f.write(open_tag)
        list_content = c.split(',')
        for i in list_content:
            f.write(new_tag[1] + i.strip() + new_tag[2])
        f.write(close_tag + '\n')

    # quote tags
    elif t == 'Quote-person':
        c = c.split('--')
        person, words = c[0], c[1]
        if not person:
            print('Error, you forgot to credit your quote to somebody')
        elif not words:
            print('Error, you forgot your quote')
        else:
            f.write(open_tag + words.strip() + new_tag[1] + person.strip() + new_tag[2] + close_tag + '\n')


########################################


def main():
    file = open("sample.txt", "r") # this will read the file
    lines = file.readlines() # readlines will process each line separately 
    file.close() # close file

    html_file = open("test.html", "w") # open test.html and write to it

    # look for tag identifiers
    for everyline in lines:
        everyline = everyline.strip('\n') # this will remove the extra spaces between lines
        # reader(everyline, tag) # calls reader() to write html 

        if everyline.startswith("##"): # finds tags in sample.txt
            tag = everyline[3:]

        elif everyline: #finds content that is not a tag
            content = everyline.strip()
        
        else: # puts things together on empty lines
            header(tag, content, html_file)


    # Extras
    html_file.write('<p class="center"><strong>Hello Capstone 2016</strong></p>\n'
                '<a href="http://www.cnn.com/2016/09/26/politics/live-updates-trump-clinton-debate/" class="center">'
                'Useless people</a>\n<div>\n<div id="fontIncrease">\n<p><center>Enlarge me Darling!!!</center></p>\n</div>\n'
                '<!-- this is to increase the font size-->\n<button onclick="increaseButton();"><center>Capstoned!!</center></button>\n'
                '</div>')

    html_file.write('\n<a class="twitter-timeline" href="https://twitter.com/albertreiber">Tweets by albertreiber</a> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>')


    # JS files
    html_file.write('\n\n<!-- JS files -->\n<script src ="capstone.js"></script>\n')

    # end HTML

    html_file.write('\n</body>\n</html>')
    html_file.close()


    # Adds files and uploads to GitHub for live hosting
    os.system("git add -A")
    os.system("git commit -m 'test'")
    os.system("git push")


if __name__ == "__main__":
    main();
