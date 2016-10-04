# fileReader for .txt
# this demonstrates how to read a file and 
# parse it using python
# from html.parser import HTMLParser
# import webbrowser

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
            'Quote-person': ['<blockquote>', '<footer>', '</footer>', '</blockquote>']
            }

hard_tags = ['List','List-dotted','List-number','Quote-person', 'Link']  



######## read/write functions ########
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

        else: #invalid tag
            print('Error: invalid tag\nView elements.txt for reference')


def hard_tag(t):
    # link tags
    if t == 'Link':
        content = content.split(',')
        url, txt = content[0], content[1]
        print(open_tag + url + new_tag[1] + txt + close_tag + '\n')

    # list tags
    elif t.startswith('List'):
        print(open_tag)
        list_content = content.split(',')
        for i in list_content:
            print(new_tag[1] + i.strip() + new_tag[2])
        print(close_tag + '\n')

    # quote tags
    elif t == 'Quote-person':
        content = content.split('--')
        person, words = content[0], content[1]
        print(open_tag + words.strip() + new_tag[1] + person.strip() + new_tag[2] + close_tag + '\n')


########################################


def main():
    file = open("sample.txt", "r") # this will read the file
    lines = file.readlines() # readlines will process each line separately 
    file.close() # close file

    html_file = open("test.html", "w") # open test.html and write to it

    # HTML file header
    html_file.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Needs a Title Here Senior</title>\n'
                    '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n'
                    '<link rel="stylesheet" type="text/css" href="style.css">\n</head>\n'
                    '<script src ="capstone.js"></script>\n<body>\n<p class="center"><strong>Hello Capstone 2016</strong></p>\n'
                    '<a href="http://www.cnn.com/2016/09/26/politics/live-updates-trump-clinton-debate/" class="center">'
                    'Useless people</a>\n<div>\n<div id="fontIncrease">\n<p>Make me Bigger!!!</p>\n</div>\n'
                    '<!-- this is to increase the font size-->\n<button onclick="increaseButton();">Embiggen</button>\n'
                    '</div>')

    # look for tag identifiers
    for everyline in lines:
        everyline = everyline.strip('\n') # this will remove the extra spaces between lines
        # reader(everyline) # calls reader() to write html 


        if everyline.startswith("##"): # finds tags in sample.txt
            tag = everyline[3:]

        elif everyline: #finds content that is not a tag
            content = everyline.strip()
        
        else: # puts things together on empty lines

            if tag in dict_tag:
                new_tag = dict_tag[tag] #finds HTML value from sample.text key
                
                open_tag = new_tag[0]
                close_tag = new_tag[-1]

                # link tags
                if tag == 'Link':
                    content = content.split(',')
                    url, txt = content[0], content[1]
                    html_file.write(open_tag + url + new_tag[1] + txt + close_tag + '\n')

                # list tags
                elif tag.startswith('List'):
                    html_file.write(open_tag)
                    list_content = content.split(',')
                    for i in list_content:
                        html_file.write(new_tag[1] + i.strip() + new_tag[2])
                    html_file.write(close_tag + '\n')

                # quote tags
                elif tag == 'Quote-person':
                    content = content.split('--')
                    person, words = content[0], content[1]
                    html_file.write(open_tag + words.strip() + new_tag[1] + person.strip() + new_tag[2] + close_tag + '\n')    

                # print easy tags
                else:
                    html_file.write(open_tag + content + close_tag + '\n')
                    


# def html_list():
#     list_of_elements = dict_tag[List] # this picks up all the values
#     for i in list_of_elements:

#         html_file.write(key_word[0])





#         if key
#     for i in list_of_elements:
#         if i.key

#     if (key_word == 'List') or (key_word == 'List_dotted') or (key_word == 'List-number'):
#             html_file.write(key_word)
#             print (dict_list)




# def html_list(key_word, items):
#     for key_word in dict_tags.values():
#         if (key_word == 'List') or (key_word == 'List_dotted') or (key_word == 'List-number'):
#             html_file.write(key_word)
#             print (dict_list)


    # end HTML

    html_file.write('\n</body>\n</html>')
    html_file.close()



if __name__ == "__main__":
    main();
