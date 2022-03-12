from abc import abstractmethod


"""
    The Band class has the following methods:
    - the __init__ which takes name and members attributes.
    - play_solos which returns the order of musicians playing solos in order.
    - to_list which is a class method that returns a list of every instance.
    __str__ that returns a stirng.
    __repr__ that returns the names.
"""
class Band:

    all_instances = []
    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.all_instances.append(self)


    def play_solos(self):
        solo = []
        for i in self.members:
            solo.append(i.play_solo())
        return solo


    
    @classmethod
    def to_list(cls):
        return cls.all_instances



    def __str__(self):
        return("This is the Band class")



    def __repr__(self):
        return self.name

    ##########################################################################

    """
    Musician class is a base class that will be inherited from (Abstract).
    Methods:
    1. __str__()  --> string a string
    2. __repr__()  --> to print a string
    3. abstract methods:
       a- get_instrument() --> will be inherited in the musicians classes
       b-  play_solo() --> will be inherited form musicians classes
    """
class Musician():

    def __init__(self, name):
        self.name = name
    


    def __str__():
        return "This is the Muician class"


    
    def __repr__():
        return("This is the base class")


    @abstractmethod
    def get_instrument():
        pass


    def play_solo():
        pass

    ##########################################################################

"""
Musicians classes inheriting name attribute from Musician class.
each one has the folowing methods:
- get_instrument which is inherited from Musicians base class, and retuns a string of instrument name.
- play_solo which is inherited from Musicians base class, and retuns a string.
- __str__ which returns a string that contains the name inherited form Musicians.
- __repr__ which returns a string that contains the name inherited form Musicians.
""" 

class Guitarist(Musician):

    def get_instrument(self):
        return "guitar" 



    def play_solo(self):
        return "face melting guitar solo"



    def __str__(self):
        return f'My name is {self.name} and I play guitar'



    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'


"""
Drummer class
"""

class Drummer(Musician):

    def get_instrument(self):
        return "drums"



    def play_solo(self):
        return "rattle boom crash"



    def __str__(self):
        return f'My name is {self.name} and I play drums'



    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'


"""
Bassist class
"""
class Bassist(Musician):

    def get_instrument(self):
        return "bass"



    def play_solo(self):
        return "bom bom buh bom"



    def __str__(self):
        return f'My name is {self.name} and I play bass'



    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'