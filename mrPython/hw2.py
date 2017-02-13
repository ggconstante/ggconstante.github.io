# Name: Gingrefel G. Constante
# Date: 02/07/2016
# Class: ISTA 350, Hw2



def ltranslate (this_list, general_dict):
    '''
    about the function/ functions purpose
    what the parameters do and what type are they
    meaning of the function's return value
    '''
    for i in range(len(this_list)):
        if this_list[i] in general_dict: 
            this_list[i] = general_dict[this_list[i]]

              
def word_count(file_name, general_dict = None):

    if general_dict == None:
        general_dict = {}
    input_file = open(file_name, 'r') # read the file 
    for line in input_file.readlines(): # read all the lines of a file
        line = line.strip().split() 
        
        for word in line: 
            word = word.lower() # lowering that word
            if word not in general_dict: 
                general_dict[word] = 1 # add that word from your text file to your dictionary 
            else:
                general_dict[word] +=1  
                
    input_file.close() # closing the file
    return general_dict # returning the original dictionary 
    
def average_wc(el_numero):
        if el_numero == {}:
            return 0
        return sum(el_numero.values())/(len(el_numero))
        
        
def max_wc(max_count):
   
    max_word = 0
    for foobar in max_count.values(): # this is a dictionary
        if foobar > max_word:
            max_word = foobar
      
    return max_word
    
# (short for dictionary reverse) This function takes a forward dictionary as its sole argument
# and creates and returns a reverse dictionary. You may assume that all values in the forward dictionary
# are immutable. Each value in the forward dictionary will bne a key in the reverse dictionary. Since values
# may appear more than once in the forward dictionary, the values in the reverse dictionary will be lists. 
def dreverse (forward_dict): 

    reverse_dict = {} # creating an empty dictionary 

    for key in forward_dict:
        if forward_dict[key] not in reverse_dict:
            reverse_dict[forward_dict[key]] = [key]
        else:
            reverse_dict[forward_dict[key]].append(key) # this maps and represents a list
            
    return reverse_dict
    
'''def bird_weights(file_name):
    fname = open(file_name, 'r')
    counter_list = []
    
    for line in fname.readlines():
        if line[0] in fname:
            counter_list += fname.values()'''
'''

'''            
def median(median_list):
    if median_list == []: 
        return None
    this_median_list = sorted(median_list) # this will order the list
    median_length = len(this_median_list) # getting the length of the list
    if median_length % 2 == 0:
        even_index_number =(median_length/2)
        odd_index_number = (median_length/2)-1
        return (this_median_list[int(even_index_number)] + this_median_list[int(odd_index_number)])/ 2
    else:
        middle_num = int(median_length // 2)
    return this_median_list[middle_num]
    
            
        
            
if __name__ == '__main__':
    main()        