# Name: Gingrefel G. Constante

# Date: 02/22/2016

# Class: ISTA 350, Hw4



from hw3 import Person



class SocialPerson:
    '''
    about the function/ functions purpose---------this initialize you instance variables         
    what the parameters do and what type are they-------self is there because it just has to be there and
    filename is the file we will open from which will be read through from the Person class 
    meaning of the function's return value-------- this function does not have a return value. however
    it returns a friend from the Person class and store them in friends with email as keys  
    '''

    def __init__(self, filename = None): 

        self.friends = {}

        if filename == None:

            self.me = Person()

            self.status = input("Enter my status: ")

            

        else:

            read_file_mode = open(filename, 'r')

            self.me = Person.read_person(read_file_mode)

            self.status = read_file_mode.readline().strip()

            friend_exist = True

            while friend_exist:

                friend = Person.read_person(read_file_mode)

                if friend:

                    self.friends[friend.email] = friend

                else:

                    friend_exist = False

            read_file_mode.close()







    def friends_str(self):
        '''
        this function has no parameter but self
        '''

        empty_str = "" # starts with an empty string

        if self.friends == {}: # if no friends in our dictionary

            return empty_str # simply return that empty string

        else:

            counter = 1 # this is the counter which will do 1) and 2) and 3) and such and such

            for key in sorted(self.friends): # iterate through your sorted friends using their keys

                empty_str += str(counter) + ')  ' + repr(self.friends[key]) + '\n'  # this gets the value of the whole dictionary

                counter += 1 # this increments our counter 

            return empty_str # this returns the format of the friend string

    





    def __repr__(self):
        '''
        this function has no parameter but self and returns the representation of our me and friends format 
        '''

        foobar =  "---------- me ----------" +'\n'

        foobar += repr(self.me)+ '\n' 

        foobar += "My status is: " + self.status + '\n\n'

        foobar += "------- friends --------\n"

        foobar += self.friends_str()

        return foobar





    def add_friend(self):
        '''
        no parameter but self
        '''

        watch_me_whip = Person() # initialize the Person class to a variable

        self.friends[watch_me_whip.email] = watch_me_whip # then that person from the Person class will be added to your list friends provided with keys 




    def get_key(self):
        '''
        this function has no parameter but self
        '''

        print ("------- friends --------")

        print (self.friends_str() + "-"*24)

        result = "" # starts with an empty string

        prompt = input("Enter friend number or 0 to cancel: ") # ask the user and prompt is a string variable 

        if not prompt.isdigit() or int(prompt) > len(self.friends):

            print ("Not a friend number: " + prompt)

            return result # return result which is an empty string if user does not follow the prompt format

        if int(prompt) == 0:

            return result

        return sorted(self.friends)[int(prompt)-1] 



    def unfriend(self):

        result = ""

        unfriend_email = self.get_key()

        if unfriend_email != result:

            self.friends.pop(unfriend_email)



    def write_sp(self, fname):

        file = open(fname, 'w')

        self.me.write_person(file)

        file.write(self.status + '\n')

        for key in self.friends:

            self.friends[key].write_person(file)

        file.close()



    @staticmethod

    def get_sp():

        print ("---------- SocialPerson Options ----------")

        print ("1) Create a new SocialPerson")

        print ("2) Load a SocialPerson from file")

        print ("3) Cancel")

        option_user = int(input("Enter option number: "))

        if option_user == 2:

            prompt_chosen_two = input("Enter filename: ")

            return SocialPerson(prompt_chosen_two)

        elif option_user == 1:

            return SocialPerson()

        else:

            return None



    @staticmethod

    def get_option():

        print ("---------- SocialPerson Options ----------") 

        print ("1) Add a friend") 

        print ("2) Unfriend someone") 

        print ("3) Print to screen") 

        print ("4) Save") 

        print ("5) Exit")

        while True:

            input_prompt = input("Enter option number: ")

            if input_prompt.isdigit():

                if int(input_prompt) > 5 or int(input_prompt) <= 0:

                    print ("Invalid option: " + input_prompt + ', try again')

                else:

                    return int(input_prompt)

            else:

                print ("Invalid option: " + input_prompt + ', try again')



def main():

    ''''''

    fosha = SocialPerson.get_sp()

    while True:

        menu_option = SocialPerson.get_option()

        if menu_option == 1:

            fosha.add_friend()

        elif menu_option == 2:

            fosha.unfriend()

        elif menu_option == 3:

            print(fosha)

        elif menu_option == 4:

            prompt_save = input("Enter save filename: ")

            fosha.write_sp(prompt_save)

        else:

            break



if __name__ == '__main__':

    main() 

















        













