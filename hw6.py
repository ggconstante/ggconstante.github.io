# Name: Gingrefel G. Constante
# Date: 03/24/2016
# Class: ISTA 350, Hw6

import numpy as np

'''
takes an array "arg_array" and returns a new array "return_this_array"
elements in the same order
'''

def reverse(arg_array):
    return_this_array = list(arg_array[::-1]) # this will reverse the array
    return np.array(return_this_array) # return a new array

'''
this function takes "odd_even_array" as a sole argument and
return "new_even_odd". 
'''
def odd_even_mask(odd_even_array):
    new_even_odd = [] 
    for i in range(len(odd_even_array)):
        if odd_even_array[i] % 2 == 0: # if even 
            new_even_odd.append(0) # return this
        else:
            new_even_odd.append(1) # this is for odd
    return new_even_odd # return this new array
    
'''
this function takes a "cycle_arr" array and "int_num" as its second argument. 
returns a new array "new_arr" with the element shifts to the right end of the array
'''
def cycle(cycle_arr, int_num):
    foo = list(cycle_arr)
    new_arr = []
    foobar = int_num % len(foo) # for instance 1%4 = 1
    new_arr.extend(foo[-foobar:] + foo[:-foobar])
    return new_arr

'''
this function takes a "double_arr" array as an argument 
and returns "new_double" that has each element doubled.  
'''
def double(double_arr):
    new_double = []
    for i in range(len(double_arr)):
        new_double.append(double_arr[i] * 2)
    return new_double

'''
this function takes "double_ip_arr" as an array
and doubles each element in place.
'''

def double_ip(double_ip_arr):
    for i in range(len(double_ip_arr)):
        double_ip_arr[i] *= 2

'''
this function takes "sq_array" as an array and
replaces each even element with its square
'''
def square_evens(sq_array):
    for i in range(len(sq_array)):
        if sq_array[i] % 2  == 0: # this is to check if the element is even 
            sq_array[i] *= sq_array[i] # this will square the even elements

'''
this function takes a "key" and "binary_array" as the second
argument. check the position of "midway_index" between "low_index"
and "high_index". if key is found return "midway_index//2". if 
the item in the "binary_array" is larger than the key
change low_index and high_index approporiately.   
'''
def binary_search(key, binary_array):
    low_index = 0
    high_index = len(binary_array)-1
    while low_index <= high_index:
        midway_index = (high_index + low_index)//2
        if binary_array[midway_index] == key:
            return midway_index
        if binary_array[midway_index] > key:
            high_index = high_index-1
        else:
            low_index = low_index + 1
    return -1

'''
this function has four arguments namely: arr, index, value, overwrite. if the 
number to overwrite is not found shift all values from index and one spot higher. 
if overwrite "value" is found then arr[index] = value
'''
def insert(arr, index, value, overwrite):
    if index > len(arr): # if the index is too large 
        raise IndexError  # raise IndexError
    if overwrite == False: # this will decide to shift all values from index and higher one to the right
        clone_array = arr.copy() # making a copy of the arr
        for i in range(index, len(arr)-1): # this for loop starts where the index is and iterate through the len-1
            arr[i+1] = clone_array[i] # this is shifting all the values from index and one spot higher to the right
        arr[index] = value # replace the original array at a particular index with the value 
    else:
        arr[index] = value # if value is found just move it inside original array 

'''
this function takes three variables. a "boss_array", "index_one"
and "index_two". swap the values of indices of "index_one" with "index_two"
No need to do any error checking 
'''
def swap(boss_array, index_one, index_two):
    for i in range(len(boss_array)):
        first_int = boss_array[index_one]
        second_int = boss_array[index_two]
        boss_array[index_one] = second_int
        boss_array[index_two] = first_int

'''
this function takes two arrays namely: "array_one" and "array_two". 
it will return the "nuevo_array" that is the length of the longer 
of the two arguments. the "nuevo_array" will return the sum of the elements
in the corresponding positions in the two arguments.
array_one = [1,2,3,4]
array_two = [5,6,7,8,9]
nuevo_array = [6,8,10,12,9]  => this is the one you return  
'''        

def add_arrays(array_one, array_two):
    nuevo_array = [] # return this array
    if len(array_two) > len(array_one):
        for i in range(len(array_two)):
            if i < len(array_one):
                nuevo_array.append(array_one[i] + array_two[i])
            else:
                nuevo_array.append(array_two[i])
    else: 
        for i in range(len(array_one)):
            if i < len(array_two):
                nuevo_array.append(array_two[i] + array_one[i])
            else:
                nuevo_array.append(array_one[i])
    return np.array(nuevo_array)


if __name__ == '__main__':
    main()  







