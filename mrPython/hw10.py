# Name: Gingrefel G. Constante
# Date: 04/25/2016
# Class: ISTA 350, Hw10
from bs4 import BeautifulSoup
import functools

@functools.total_ordering 
class Person:

    def __init__(self, last, first,ptype,email,phone,unit,position,addr,bldg,rm):
        '''
        instance variables declaration
        init: init has parameters corresponding to the following instance variables: 
        last (name), first (name), ptype (student, staff, appointed personnel, etc.), 
        email, phone, unit, position, addr, bldg, and rm.
        '''
        self.last = last # last and etc... are variables that are being passed in 
        self.first = first
        self.ptype = ptype
        self.email = email
        self.phone = phone
        self.unit = unit
        self.position = position
        self.addr = addr
        self.bldg = bldg
        self.rm = rm

    '''
    from_soup: this class method takes a BeautifulSoup object representing an html 
    element with the name span and attribute class="field-content". rich_thompson.html is a 
    file containing the results of searching UA's phonebook on my first and last name. 
    You can use this file to see how the data for each person found is organized, once you find it 
    considerably far down in the file. Extract this data and use it to construct and return a Person object. 
    The BeautifulSoup link above will be helpful. For some reason, a Person's unit is in their 'degree' attribute
    and their 'position' is in their 'department' attribute. Finally, when people enter data manually, 
    screwy things happen. President Hart's department info was entered in different format from all of the other 
    department data I have seen. So after you get the data for the position instance variable, insert this line: 
    pos = pos.replace('\r', '') (of course, use whatever temporary variable name you choose). 
    Kill that ridiculous carriage return.
    '''
    @classmethod # this is a decorator needed for this class
    def from_soup(cls, soup_obj): # the second argument is the BeautifulSoup object
    
        '''el_nombre'''
        name_sopa = soup_obj.find('h3')
        if name_sopa == None:
            last = ''
            first = ''
        else:
            name_sopa = name_sopa.get_text().strip().split(', ')
            last_name = name_sopa[0]
            first_name = name_sopa[1]

        '''ptype'''
        ptype_soup = soup_obj.find('span', 'type')
        if ptype_soup == None:
            ptype_soup = ''
        else:
            ptype_soup = ptype_soup.get_text().strip()
    
        '''el_sobre'''
        usps = soup_obj.find('a', 'mailto')
        if usps == None:
            usps = ''
        else:
            usps = usps.get_text().strip()

        '''el_telefono'''
        el_numero = soup_obj.find('a', 'phoneto')
        if el_numero == None:
            el_numero = ''
        else:
            el_numero = el_numero.get_text().strip()

        '''el_unit'''
        el_unito = soup_obj.find('div', 'degree')
        if el_unito == None:
            el_unito = ''
        else:
            el_unito = el_unito.get_text().strip()

        '''el_position'''
        el_position = soup_obj.find('div', 'department')
        if el_position == None:
            el_position = ''
        else:
            el_position = el_position.get_text().strip().split('\n')[0]
            el_position = el_position.replace('\r', '')

        '''el_address, el_bldg, el_rm'''
        el_add_bl_rm = soup_obj.find_all('div')
        if el_add_bl_rm[-3].get_text().strip():
            el_address = el_add_bl_rm[-3].get_text().strip()
        else:
            el_address = ""

        if el_add_bl_rm[-2].get_text().strip():
            el_bldg = el_add_bl_rm[-2].get_text().split(':')[1].strip()
        else:
            el_bldg = ""
        
        if el_add_bl_rm[-1].get_text().strip():
            el_rm = el_add_bl_rm[-1].get_text().split(':')[1].strip()
        else:
            el_rm = ""

        return cls(last_name, first_name, ptype_soup, usps, el_numero, el_unito, el_position, el_address,el_bldg, el_rm) 
    
    '''
    generator: this instance method generates the information in self as 
    strings in the order given in init with two exceptions. last and first 
    are in a single string, the first string yielded, per this example: 
    'Thompson, Rocket'. bldg and rm are in a single string, the last string yielded, per 
    this example: 'Gould-Simpson rm 856'.
    '''
    def generator(self):
        yield(self.last + ', ' + self.first)
        yield(self.ptype)
        yield(self.email)
        yield(self.phone)
        yield(self.unit)
        yield(self.position)
        yield(self.addr)
        yield(self.bldg + ' rm ' + self.rm)

    '''
    repr: returns a string containing first, last, email, and 
    position per this example: 'Rocket Thompson, crazy_dog@gmail.com, Happy Dog'.
    '''
    def __repr__(self):
        return (str(self.first) + ' ' + str(self.last) + ', ' + str(self.email) + ', ' + str(self.position))
    
    '''
    eq: this method tests equality between two Person objects with 
    just one of their many instance variables. What datum uniquely identifies a Person?
    '''
    def __eq__(self, other):
        return self.email == other.email # self.email is an instance and other.email is another instance

    '''
    lt: if the objects are equal, return False. If not, base the result on last names. 
    If the last names are equal, base the result on first names. 
    We only need one more tie breaker. What is it?
    '''        
    def __lt__(self,other):
        if self == other: # self and other is the entire Person instance
            return False
        elif self.last != other.last:
            if self.last < other.last:
                return True
            else:
                return False
        elif self.first != other.first:
            if self.first < other.first:
                return True
            else:
                return False
        else:
            if self.email < other.email:
                return True
            else:
                return False

    '''
    hash: magic method hash calls built-in function hash on email and 
    returns the result. This method allows a collection of Person objects 
    to be used to construct a set of Person objects.
    '''
    
    def __hash__(self):
        return hash(self.email)

class People:

    def __init__(self, person_obj = None, filename = None):
        '''
        instance variables
        '''
        if not person_obj:
            self.people = [] # 
        else:
            self.people = person_obj
        self.missing = [] # this holds the names that were in the input file and not found in the phonebook
        fname_open = open(filename)
        for i in range(len(fname_open))
        



    
    if __name__ == '__main__':
        main() 

