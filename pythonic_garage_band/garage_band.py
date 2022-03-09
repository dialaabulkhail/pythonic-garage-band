from abc import abstractmethod



class Band:
    members = []

    def __init__(self, name, members = []):
        self.name = name
        self.members = members
        self.__class__.all.append(self)

    all = []




    def play_solos(self):
        """
         Asks each member musician to play a solo, in the order they were added to band.
        """
        solos = ''
        for i in self.members:
            solos += f'{i.play_solo()}\n'
        return solos[:-1]
    

    def __str__(self):
        return("This is the Band class")


    @abstractmethod
    def __repr__(self):
        return self.name

    
    @classmethod
    def to_list(cls):
        return cls.all

    
# here goes the staticmethod
class Musician:

    # members = []

    def __init__(self, musicians, instrument):
        self.musicians = musicians
        self.instrument = instrument
        # self.__class__.members.append(self)
    
    

    def __str__(self):
        return self.musicians


    
    def __repr__(self):
        return("This is the base class")


    @abstractmethod
    def get_instrument(self):
        return self.instrument


    @abstractmethod
    def play_solo(self):
        return ''


###### Musicians classes inheriting name attribute from Band class 

class Guitarist(Band):

    def __str__(self):
        return f'My name is {self.name} and I play guitar'


    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'


    def get_instrument(self):
        return "guitar" 
    

    def play_solo(self):
        return "face melting guitar solo"




class Drummer(Band):

    def __str__(self):
        return f'My name is {self.name} and I play drums'


    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'


    def get_instrument(self):
        return "drums"


    def play_solo(self):
        return "rattle boom crash"
    



class Bassist(Band):

    def __str__(self):
        return f'My name is {self.name} and I play bass'


    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'


    def get_instrument(self):
        return "bass"


    def play_solo(self):
        return "bom bom buh bom"


    


# if __name__ == "__main__":
