# Name: Gingrefel G. Constante
# Date: 02/14/2016
# Class: ISTA 350, Hw3
import os
import sqlite3
import sys

class Person:

    def __init__(self, first = "", last = "", bday = "", email = ""): 

        '''
        this function is initializing your variables and creates your instances

        about the function/ functions purpose
        what the parameters do and what type are they
        the parameters are all strings and they are supposed to be global an declared in the Person class
        meaning of the function's return value

        this function does not return anything
        '''
        if first:
            self.first = first
        else:
            self.first = input("Enter person's first name: ")
        if last:
            self.last = last
        else:
            self.last = input("Enter person's last name: ")
        if bday:
            self.bday = bday
        else:
            self.bday = input("Enter person's birthday: ")
        if email:
            self.email = email
        else:
            self.email = input("Enter person's e-mail: ")

    def __repr__(self):
        # this function is used on how we present our data in the database

        return self.first + ' ' + self.last +  ': ' + self.bday + ', '+ self.email

    @classmethod    
    def read_person(cls, file):
        # this function is an instant class and is not global in our Person class
        first = file.readline().strip()
        if not first:
            return False
        last = file.readline().strip()
        bday = file.readline().strip()
        email = file.readline().strip()
        return cls(first, last, bday, email)

    def write_person(self, file_object): # this is the file object we are writing into 
        file_object.write(self.first + '\n' + self.last + '\n' + self.bday + '\n' + self.email + '\n')

def open_persons_db():
    # this function is used to connect to our database for friends and colleagues using 
    # we are using the sqlite3 to connect to our database.

    file_path = os.path.exists('persons.db') # this checks if the database exist
    db = sqlite3.connect('persons.db')
    db.row_factory = sqlite3.Row # use to gain easy access to the fields of a row
    if not file_path: # this gives you true or false
        db.execute('CREATE TABLE friends' + '(first TEXT, last TEXT, bday TEXT, email TEXT PRIMARY KEY)')
        db.execute('CREATE TABLE colleagues' + '(first TEXT, last TEXT, bday TEXT, email TEXT PRIMARY KEY)')
        db.commit() # make the changes persistent
    return db

def add_person(p_db, p_obj,friend = True, colleague = False):
    if friend == False and colleague == False:
        print ("Warning: " + p_obj.email +  " not added - must be friend or colleague", file = sys.stderr)
        return False
    if friend == True:
        p_db.execute('INSERT INTO friends' + '(first, last, bday, email )'+'VALUES(?,?,?,?);',(p_obj.first, p_obj.last, p_obj.bday,p_obj.email))
    if colleague == True:
        p_db.execute('INSERT INTO colleagues' + '(first, last, bday, email )'+'VALUES(?,?,?,?);',(p_obj.first, p_obj.last, p_obj.bday,p_obj.email))
    p_db.commit()
    return True

def delete_person(person_db, person):

    person_db.execute('DELETE FROM friends WHERE email = ?;',(person.email,)) # comma is specifying a tuple and email is our Primary Key
    person_db.execute('DELETE FROM colleagues WHERE email = ?;',(person.email,))
    person_db.commit()

def to_Person_list(cur_obj):
                             
    return_list = []                                                                                                         
    rows = cur_obj.fetchall() # multiple rows
    for r in rows:
        return_list.append(Person(r['first'],r['last'],r['bday'],r['email']))
    return return_list

def get_friends(person_get_friends):
    cursor = person_get_friends.execute('SELECT * FROM friends; ')
    return to_Person_list(cursor)
def get_colleagues(person_get_colleagues):
    cursor = person_get_colleagues.execute('SELECT * FROM colleagues; ')
    return to_Person_list(cursor)

def get_all(person_get_all):
    cursor = person_get_all.execute('SELECT * FROM friends UNION SELECT * FROM colleagues;')
    return to_Person_list(cursor)

def get_and(person_get_and):
    cursor = person_get_and.execute('SELECT friends.first, friends.last, friends.bday, friends.email FROM friends JOIN colleagues ON colleagues.email = friends.email;')
    return to_Person_list(cursor)

    














