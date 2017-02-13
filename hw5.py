# Name: Gingrefel G. Constante

# Date: 02/28/2016

# Class: ISTA 350, Hw5

class Binary:

    '''
    init has one string parameter with a default argument of '0'. This string can be the empty
    string (treat the same as '0'). Otherwise, it should consist only of 0’s and 1’s and should be 16 or less
    characters long. If the argument does not meet these requirements, raise a RuntimeError. Each
    Binary object has one instance variable, a list called num_list. num_list has integers 0 or 1 in
    the same order as the corresponding characters in the argument. If the string is less than 16 characters
    long, num_list should be padded by repeating the leftmost digit until the list has 16 elements. This is
    to be done by calling the next method.
    '''

    def __init__(self, string_zero = '0'): # string_zero is a string of zeroes and ones
        if string_zero == '': # if string is empty
            string_zero = '0' # return a string of zeroes and ones 
        self.num_list = list(string_zero) # lets turn a string_zero into a list since a list is mutable

        if string_zero:
            for number in string_zero:
                if number not in ['0','1', 0 , 1]: # if the user put in not one of these
                    raise RuntimeError() # raise this
        if len(string_zero) > 16: # if the len which is an int is greater than 16
            raise RuntimeError() # raise this 
        
        for i in range(len(self.num_list)): # iterate through self.num_list
            self.num_list[i] = int(self.num_list[i]) # this is converting self.num_list into int
        
        if len(string_zero) < 16: # if length is less than 16
            self.pad() # call the function pad() and 0's to the left
    '''
    Pad num_list by repeating the leftmost digit until the list has 16 elements
    '''

    def pad(self):  
        while len(self.num_list) < 16:
            self.num_list.insert(0, self.num_list[0])

    '''
    repr: Return a 16-character string representing the fixed-width binary number, such as:
    '00000000000000000'.
    '''

    def __repr__(self):
        return "".join(str(item) for item in self.num_list)
    
    '''
    eq: Takes a Binary object as an argument. Return True if self == the argument, False
    otherwise.
    '''
    def __eq__(self, other):
        if self.num_list == other.num_list:
            return True
        else:
            return False
    '''
    add: Takes a Binary object as an argument. Return a new Binary instance that represents the sum
    of self and the argument. If the sum requires more than 16 digits, raise a RuntimeError.
    '''

    def __add__(self, other_binary):
        result = []
        carry = 0
        for i in range(15, -1, -1):
            bit_sum = self.num_list[i] + other_binary.num_list[i] + carry
            result.insert(0, bit_sum % 2)
            carry = int(bit_sum > 1)
        if self.num_list[0] == other_binary.num_list[0] != result[0]:
            raise RuntimeError()
        return Binary(result) 
    '''
    neg: Return a new Binary instance that equals -self.
    '''

    def __neg__(self):
        new_list = [] # make an empty list
        counter = ''
        for i in range(len(self.num_list)): #
            if self.num_list[i] == 1: # if the index [i] is an integer 1
                new_list.append('0') # then we flip that 1 and append 0 to it or change 1 to 0. this is a string 0
            else:
                new_list.append(str(1)) # append str 1 
        counter = ''.join(new_list)
        return Binary(counter) + Binary('01') # Binary() = 0, we do this to not change the Binary(counter)
    
    '''
    sub: Takes a Binary object as an argument. Return a new Binary instance that represents self –
    the argument.
    ''' 

    def __sub__(self, other):
        return self + (-other)

    '''
    int: Return the decimal value of the Binary object. This method should never raise a
    RuntimeError due to overflow. Do not use int on Binary objects in any other method. You may
    use it to convert strings to integers, but not on Binary objects.
    '''

    def __int__(self):
        dec_total = 0 # this is an int starting fresh cola at 0
        subscript = 0
        if self.num_list == [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]: # 2^15 = -32768, now we put negative because the leading binary digit is 1  
            return (-32768)
        if self.num_list[0] == 1:
            foobar = (-self) # this is like calling the neg() function
            for pos in foobar.num_list[::-1]: # let's go reverse fellas
                if pos == 1: # in this location is a string
                    dec_total += 2** subscript
                subscript += 1 # incrementing subscript
            return (-dec_total)
        for pos in self.num_list[::-1]: # let's go reverse fellas
            if pos == 1: # in this location is a string
                dec_total += 2** subscript
            subscript += 1
        return dec_total

    '''
    lt: Takes a Binary object as an argument. Return True if self < the argument, False
    otherwise. This method should never raise a RuntimeError due to overflow.
    '''
    def __lt__(self, other):
        if self.num_list[0] == 0 and other.num_list[0] == 1:
            return False
        elif self.num_list[0] == 1 and other.num_list[0] == 0:
            return True
        else:
            winnie = self + (-other)
            if winnie.num_list[0] == 1: # you are checking if it is negative means self is smaller 10-100 = -90
                return True
            else:
                return False

    '''
    abs: Return a new instance that is the absolute value of self.
    '''
    def __abs__(self):
        if self.num_list[0] == 1:
            return (-self) 
        else:
            return self + Binary()





