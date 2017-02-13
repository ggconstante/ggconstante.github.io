# Name: Gingrefel G. Constante
# Date: 04/17/2016
# Class: ISTA 350, Hw9
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
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

'''this is where homework8 starts''' 

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

'''Hw9 starts here'''

'''
this function takes "str_func_fname" as its sole argument. str_func_fname contains a json object
representating a list of lists. returns a DataFrame that is named frame with row labels
(index) that are three-letter abbreviations for the months and the year
'''

def get_panda(str_func_fname):
    infile = open(str_func_fname)
    json_pointer = json.load(infile) # list of lists
    index = ['Jan', 'Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Ann']
    columns = json_pointer[0]
    frame = DataFrame(json_pointer[1:],index,columns)
    return frame

'''
takes a data_frame as its sole argument and calculate the statistics and populate the
data_frame with them
'''

def get_stats(data_frame):
    index_dataframe = ['mean', 'sigma', 's','r']
    columns = list(data_frame.index)
    for_mean = []
    for_pop_sd = []
    sample_sd = []
    r_corr = []
    master_list = []
    col_years = Series(data_frame.columns)
    for i in range(len(data_frame)):
        for_mean.append(data_frame.iloc[i].mean())
        for_pop_sd.append(data_frame.iloc[i].std(ddof = 0))
        sample_sd.append(data_frame.iloc[i].std(ddof = 1))
        row = Series(data_frame.iloc[i].values) # this is changing
        r_corr.append(row.corr(col_years))
    master_list.append(for_mean)
    master_list.append(for_pop_sd)
    master_list.append(sample_sd)
    master_list.append(r_corr)
    return DataFrame(master_list, index_dataframe,columns)

'''
this function takes an fname as a filename. create a DataFrame from the data in the file.
print a DataFrame containing a statistical summary of that data.
'''

def print_stats(fname):
    print('----- Statistics for '+ str(fname) + ' -----\n')
    sushi_chan = get_panda(fname)
    print (get_stats(sushi_chan))
    print ('')

'''
this function takes a smooth_data_frame and datum_precision as its two arguments. 
it returns a DataFrame(derp,foo,bar) but each data point has been replaced with the 
11-year average of the surrounding data including the data point itself. datum_precision specifies
a precision for each datum. 
'''

def smooth_data(smooth_data_frame,datum_precision = 5):
    foo = smooth_data_frame.index
    bar = smooth_data_frame.columns
    derp = []
    for row in range(len(foo)):
        foobar = []
        for col in range(len(smooth_data_frame.values[row])):
            if col < 5: # this one checks the 5 values to the left
                first_left = sum(smooth_data_frame.values[row][:col]) # this will get the first list of numbers but not the actual index
                first_right = sum(smooth_data_frame.values[row][col:col+6])
                foobar.append(round((first_left + first_right) / (len(smooth_data_frame.values[row][:col])\
                + len(smooth_data_frame.values[row][col:col+6])), datum_precision))
            elif col >= len(smooth_data_frame.values[row])-5: # this checks if there are 5 values on the right
                second_left = sum(smooth_data_frame.values[row][col-5:col])
                second_right = sum(smooth_data_frame.values[row][col:])
                foobar.append(round((second_left + second_right) /(len(smooth_data_frame.values[row][col-5:col])\
                   + len(smooth_data_frame.values[row][col:])),datum_precision))
            else:
                left = sum(smooth_data_frame.values[row][col-5:col])
                right = sum(smooth_data_frame.values[row][col:col+6])
                foobar.append(round((left + right)/11,datum_precision)) # this is guaranteed you will have 11 values
        derp.append(foobar)
    return DataFrame(derp,foo,bar)
'''
this function has three arguments: fname_plot, month_plot and el_precisio
'''
def make_plot(fname_plot, month_plot = None, el_precisio = 5):
    data_frame_plot = get_panda(fname_plot) # make a dataframe from the file 
    data_frame_smooth = smooth_data(data_frame_plot,el_precisio) # use that to make a dataframe of smoothed data
    foo = data_frame_plot.T # transposed
    bar = data_frame_smooth.T # transposed
    if month_plot == None: # if no month was passed 
        sub_plot = foo.plot(subplots = True, legend = None, color = 'g', yticks = [], title = fname_plot) # plot all the data
        for i in range(len(sub_plot)): # setting up for the label
            sub_plot[i].set_ylabel(foo.columns[i]) # this will give you the label for the columns
            bar.ix[:,i].plot(ax = sub_plot[i], color = 'b', legend = None, yticks = [])
    else:
        foo.ix[:,0].plot(title = fname_plot + ": " + str(month_plot)) # plotting just the months data with the title being the filename followed by a colon and the month string 
        bar.ix[:,0].plot() # plotting the smoothed data

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

    for fname in fnames:
        json_fname = fname.split('.')[0] + '.json'
        print_stats(json_fname)
        make_plot(json_fname,el_precisio = 2)
    plt.figure()
    make_plot(fnames[0].split('.')[0] + '.json', 'Jan')
    input('Enter to end:')

if __name__ == '__main__':
    main()




    


        










