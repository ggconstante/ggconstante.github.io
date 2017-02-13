# Name: Gingrefel G. Constante
# Date: 04/03/2016
# Class: ISTA 350, Hw7
import os
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









