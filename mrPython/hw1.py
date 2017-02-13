# Name: Gingrefel G. Constante
# Date: 01/19/2016
# Class: ISTA 350, Hw1
# Brief Summary: The intention of this homework is to review strings and lists and how to go back and forth between them.

def sort_int_string(int_str): # one string parameter
        if int_str == "":
            return "" # return an empty string
        num_str = int_str.split() # splitting the string 
        num_str.sort(key=int) # sorting the string and 
        sorted_str = " ".join(num_str) # combining and sorting the entire string 
        return sorted_str # return the sorted string


def dash_reverse(rev_str): # takes one string argument
    result = rev_str[::-1] # this will reverse the string 
    new_str = "" # start with an empty string
    for i in range(len(result)): # going through the reversed string
        new_str += result[i] # adding at specific index and adding it to our new_str
        if i< len(result)-1: # this is checking if your index is less than your the length of your string 
            new_str += '-'
    return new_str

'''
This function was given in class.  
'''   
def xslice_replace(string, start, end, step, replacement):
    str_list = list(string)
    rep_list = list(replacement)
    str_list[start:end:step] = rep_list
    return "".join(str_list)
    
                       #list_alt  #item_search
def element_ip_replace(search_lst, found_match, replacement=None): 
    i = 0
    for i in range(len(search_lst)):
        if search_lst[i] == found_match:
            search_lst[i] = replacement
            i += 1


def element_nl_replace(original_list, searched_item, replacement = None):
    return_this_list = [] 
    i = 0
    foobar = list(original_list) # make sure to turn into a list first because Damaris said that 
    for i in range(len(foobar)): # this is our original list that we need to iterate
        if foobar[i] == searched_item:
            return_this_list.append(replacement)
            i += 1
        else:
            return_this_list.append(foobar[i])
            i += 1
    return return_this_list


def lreplace(search_lst, sublist, third_lst=[]): 
    result = [] # starting with an empty list
    i = 0 # counter start at 0
    if len(search_lst) == 0 and len(sublist) == 0: # making sure they are the same type
        result += third_lst
    if len(sublist) == 0 and len(search_lst) > len(sublist):
        for i in range(len(search_lst)):  
                result.extend(third_lst)
                result.append(search_lst[i])
        result.extend(third_lst)
    else:
        while i < len(search_lst):
       
            if search_lst[i:i + len(sublist)] == sublist: # this is moving you counter + key value
                result +=third_lst
                i +=len(sublist)
            else:
                result.append(search_lst[i])
                i += 1
    search_lst.clear()
    search_lst.extend(result)


def list_lt(list_one, list_two):
    return_list = []
    x = list(list_one)
    y = list(list_two)
    if len(x) != len(y):
        return None
    flag = False
    for i in range(len(x)):
        if x[i] < y[i]:
            return_list.append(True)
        else:
            return_list.append(flag)
    return return_list

def sum_of_powers(first_list_base, second_list_exponents):
    new_list_powers = []
    exp = 0
    first = list(first_list_base)
    second = list(second_list_exponents)
    while exp < len(second):
        index_first_base = 0
        num_sum = 0
        while index_first_base < len(first):
            num_sum += first[index_first_base] ** second[exp]
            index_first_base +=1
        new_list_powers.append(num_sum)
        exp += 1

    return new_list_powers

def trace(matrix):
    lol_matrix = list(matrix)
    counter = 0
    for i in range(0, len(lol_matrix)):
        counter = counter + float(lol_matrix[i][i])
    return counter

def str_by_twos(string_okay):# "abcd" -> "ab" "bc" "cd"
    result = []
    i = 0
    while i < len(string_okay):
        if i+1<len(string_okay): # 0+1<4
           s = string_okay[i] + string_okay[i+1]
           result.append(s)
        i+= 1
        
    return result

if __name__ == '__main__':
    main()  
           

    
