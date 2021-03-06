# fileReader for .txt
# this demonstrates how to read a file and 
# parse it using python
import os

##################### comment each line please ########################

dict_tag = {'Title':['<title>', '</title>'],
            'Header': ['<h1>','</h1>'],
            'Header-medium':['<h2>','</h2>'],
            'Header-small':['<h3>','</h3>'],
            'Header-center':['<h1 class="centered">', '</h1>'], 
            'Header-medium-center':['<h2 class="centered">', '</h2>'],
            'Header-small-center':['<h3 class="centered">', '</h3>'],
            'Link':['<a href="', '">', '</a>'],
            'PP':['<p class="pp_one">','</p>'], 
            'PP-center':['<p class="centered pp_two">', '</p>'],
            'PP-right':['<p class="pp_right">', '</p>'], 
            'List':['<ul>', '<li>','</li>','</ul>'],
            'List-dotted':['<ul class="list_dotted">', '<li>', '</li>','</ul>'],
            'List-number':['<ol>', '<li>','</li>','</ol>'], 
            'Quote': ['<blockquote>','</blockquote>'], 
            'Quote-person': ['<blockquote>', '<footer>- ', '</footer>', '</blockquote>'], 'Image':['<img src="', '"\>'],
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
        f.write(open_tag + c + close_tag + '\n</head>\n\n<body>\n<div id="wrapper">\n')

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

def tweets(f):
    askTwitter = input('Do you want to include your recent tweets? y/n ')
    if askTwitter.lower() == 'y':
        account = input('If your twitter account name is @Bob124, enter Bob124\nPlease enter a public twitter account name:')
        # if account not valid....
        f.write('<a class="twitter-timeline" data-height="500" href="https://twitter.com/' + account + '">'
            'Tweets by ' + account + '</a> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>')
    else:
        return

def git(*args):
    return subprocess.check_call(['git'] + list(args))        

########################################


def main():
    file = open("sample.txt", "r") # this will read the file
    lines = file.readlines() # readlines will process each line separately 
    file.close() # close file

    html_file = open("capstone.html", "w") # open capstone.html and write to it

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

    tweets(html_file)            

    # Extras
    html_file.write('<p class="center"><strong>Hello Capstone 2016</strong></p>\n'
                '<a href="http://www.arizona.edu/" class="center">'
                'Randomness</a>\n<div>\n<div id="fontIncrease">\n<p>Make this string bigger/larger</p>\n</div>\n'
                '<!-- this is to increase the font size-->\n<button onclick="increaseButton();" id = "capstone" >Capstoned!!</button>\n'
                )

    html_file.write('<div>\n'
                '<div id ="hideMe"> <p>Simple Javascript<strong>manipulation!</strong></p></div>\n'
                '<input  onclick = "showButton();"  id = "click" type ="Button" value = "Hide"/>'
                )


    footer = '\n</div>\n<footer id="footer">\n&copy; 2016 | Design by Gingrefel Constante &amp; Albert Reiber\n</footer>'
    html_file.write(footer)

    # JS files
    html_file.write('\n\n<!-- JS files -->\n<script src ="capstone.js"></script>\n')


    # end HTML

    html_file.write('\n</body>\n</html>')
    html_file.close()    

    # Adds files and uploads to GitHub for live hosting FOR MAC OS ONLY
    if os.name == 'posix':
        os.system("git add -A")
        os.system("git commit -m 'test'")
        os.system("git push")
    else:
        return


if __name__ == "__main__":
    main();
