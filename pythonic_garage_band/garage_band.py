from abc import abstractmethod



class Band:
    def __init__(self, name, members = []):
        self.name = name
        self.members = members



    def play_solos(self):
        """
         Asks each member musician to play a solo, in the order they were added to band.
        """
        for i in self.members:
            solos += i.play_solo() 
        return solos
    


    def __str__(self):
        return("This is the Band class")


    @abstractmethod
    def __repr__(self):
        return self.name

    
    @classmethod
    def to_list(cls):
        return cls.members

    
# here goes the staticmethod






class Musician:

    members = []

    def __init__(self, musicians, instrument):
        self.musicians = musicians
        self.instrument = instrument
        self.members.append(self)

    

    def __str__(self):
        return self.musicians


    
    def __repr__(self):
        return("This is the base class")


    
    def get_instrument(self):
        return self.instrument


    def play_solo(self):
        if {self.instrument} == "guitar":
            return "face melting guitar solo"
        elif {self.instrument} == "bass":
            return "bom bom buh bom"
        else:
            return "rattle boom crash"


###### Musicians classes inheriting name attribute from Band class 
##passed
class Guitarist(Band):
    def __str__(self):
        return f'My name is {self.name} and I play guitar'


    def get_instrument(self):
        return "guitar"


    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'



#Passed
class Drummer(Band):
    def __str__(self):
        return f'My name is {self.name} and I play drums'


    def get_instrument(self):
        return "drums"


    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'
    

#passed
class Bassist(Band):
    def __str__(self):
        return f'My name is {self.name} and I play bass'


    def get_instrument(self):
        return "bass"


    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

