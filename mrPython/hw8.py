# Name: Gingrefel G. Constante
# Date: 04/05/2016
# Class: ISTA 350, Hw8
import os
import json 
import requests, gzip
from bs4 import BeautifulSoup

def get_soup(str_url= None, fname = None, gzipped = False): # contains three parameters
    if fname: # if the filename is not None 
        open_file = open(fname) # open the file 
        file_obj = BeautifulSoup(open_file) # pass the resulting file-pointer to the BeautifulSoup constructor
        return file_obj # return the resulting object 
    if not str_url: # if the url is None
        raise RuntimeError('Either url or filename must be specified.')
    if str_url: # if it is not None--this is opposite logic
        r_server_request = requests.get(str_url) # send a request to the server 
    if gzipped: # if the response content is gzipped 
        info = gzip.decompress(r_server_request.content) # unzip it
        soup = BeautifulSoup(info) # pass the content to the BeautifulSoup
        return soup # return the resulting object
    else:
        return BeautifulSoup(r_server_request.content) 


def save_soup(fname, soup_obj): # takes two arguments 
    open_file = open(fname, 'w') # we are going to open the file and then write into that filename
    str_rep = str(soup_obj) # we are going to write a textual representation of the soup object in the file
    open_file.write(str_rep) # writing our str_rep into open_file
    open_file.close() # closing the file


def scrape_and_save():
    
    '''scraping the following addresses'''
    pcp ='http://www.wrcc.dri.edu/WRCCWrappers.py?sodxtrmts+028815+por+por+pcpn+none+msum+5+01+F'
    mint ='http://www.wrcc.dri.edu/WRCCWrappers.py?sodxtrmts+028815+por+por+mint+none+mave+5+01+F'
    maxt ='http://www.wrcc.dri.edu/WRCCWrappers.py?sodxtrmts+028815+por+por+maxt+none+mave+5+01+F'
    
    '''soup objects/ soupifying contents'''
    foo = get_soup(pcp) # you do this "foo" because the get_soup is returning something  
    bar = get_soup(mint)
    nuevo = get_soup(maxt)

    '''writing the soup objects to files'''
    save_soup('wrcc_pcpn.html', foo)
    save_soup('wrcc_mint.html', bar)
    save_soup('wrcc_maxt.html', nuevo)

# this is where homework8 starts 

def is_num(str_bool): # this is a string and can represent anything 
    try:
        foo = float(str_bool)
        return True
    except:
        try:
            bar = int(str_bool)
            return True
        except:
            return False 


'''
this function returns a list of lists containing the
useful data in the soup object
'''
def load_lists(soup_obj, flag): # soup_obj contains an html parsed tree and flag represents -999

    outer_list = [] # this is the outer list
    for tr in soup_obj.find_all('tr'): # this will find all the tr tags in your html file. all the lists in your entire tr
        inner_list = [] # this is the inner list
        for td in tr.find_all('td'): # this is extracting and iterating the td  
            td_contents = td.get_text()
            if is_num(td_contents): # this checks is it is a number from the data
                try:
                    inner_list.append(int(td_contents))
                except:
                    inner_list.append(float(td_contents))
            elif td_contents == '-----':
                inner_list.append(flag)
        outer_list.append(inner_list)
        '''this is transposing the table data'''
    outer_list_transposed = outer_list[1:-7] # this is overriding the original outer list which is a list of list and cutting it from bottom    
    transposed = []
    for i in range(len(outer_list_transposed[0])):
        transposed.append([])
    for lst in outer_list_transposed:
        for i in range(len(outer_list_transposed[0])):
            transposed[i].append(lst[i])
    return transposed

def replace_na(lol, row, col, flag, precision = 5):
    empty_list = []
    counter = col - 1 # this will reverse the order of column
    i = 0
    while i < 5 and counter >=0: # the purpose of i is to make sure we are only at most 5 times 
        if lol[row][counter] != flag:
            empty_list.append(lol[row][counter])
        i+=1
        counter -=1
    second_i = 0 
    second_counter = col + 1
    while second_i < 5 and second_counter <= len(lol[row])-1:
        if lol[row][second_counter] != flag:
            empty_list.append(lol[row][second_counter])
        second_i +=1
        second_counter +=1
    return round((round(sum(empty_list),precision)/len(empty_list)),precision)

def clean_data(clean_list, clean_flag, clean_precision = 5):
    for i in range(len(clean_list)):
        for j in range(len(clean_list[i])): 
            if clean_list[i][j] == clean_flag:
                foobar = replace_na(clean_list,i,j,clean_flag,clean_precision)
                clean_list[i][j] = foobar

def recalculate_annual_data(rec_lol, annual_bool = False, annual_precision = 5):
    '''this is transposing our original list and putting it back to the way it was
    [[2001,10,10,10,0
    [ 2002, 1, 2, 3,0]
    [ 2003,-1, 0, 1,11]]

    '''
    transposed = []
    for i in range(len(rec_lol[0])):
        transposed.append([])
    for lst in rec_lol:
        for i in range(len(rec_lol[0])):
            transposed[i].append(lst[i])
    for row in range(len(transposed)):
        foobar = round(sum(transposed[row][1:-1]),annual_precision)
        if annual_bool == True:
            nuevo = round(foobar/len(transposed[row][1:-1]), annual_precision)
            transposed[row][-1] = nuevo
        else:
            transposed[row][-1] = foobar
    '''altering the original list and populating the data'''
    rec_lol.clear() # start with an empty list and populate the datum
    for i in range(len(transposed[0])):
        rec_lol.append([])
    for lst in transposed:
        for i in range(len(transposed[0])):
            rec_lol[i].append(lst[i])


def clean_and_jsonify(listo_fnames, los_flagos, precision_toyota = 5):
    
    for i in range(len(listo_fnames)): # iterate through our list
        foobar = get_soup(None, listo_fnames[i], False) # call the get_soup
        nuevo = load_lists(foobar,los_flagos) # transform it into a list of lists by calling load_list 
        clean_data(nuevo, los_flagos, precision_toyota) # clean the list by calling clean_data
        if listo_fnames[i] == 'wrcc_pcpn.html': # if precipitation totals should be recalculated
            recalculate_annual_data(nuevo, False, precision_toyota)
        else:
            recalculate_annual_data(nuevo, True, precision_toyota) # else just recalculate averages
        banana = open(listo_fnames[i][:-5]+ ".json" ,'w') # dealing with one file at a time and slicing the .html extension
        json_obj = json.dump(nuevo,banana) # dump is like saving and takes a python obj and dumps it into a text file 
        banana.close()

def main():
    if not os.path.isfile('wrcc_pcpn.html'): # this is checking if a file exists in the current working directory using isfile
        print ('---- scraping and saving ----')
        scrape_and_save()
    if not os.path.isfile('wrcc_mint.html'):
        print ('---- scraping and saving ----')
        scrape_and_save()
    if not os.path.isfile('wrcc_maxt.html'):
        print ('---- scraping and saving ----')
        scrape_and_save()
    fnames = ['wrcc_pcpn.html', 'wrcc_mint.html','wrcc_maxt.html']
    clean_and_jsonify(fnames, -999, 2)




    


        










