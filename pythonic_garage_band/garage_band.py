band_list = []

class Band:
    def __init__(self, name, members = []):
        self.name = name
        self.members = members
        self.band_list.append(self)



    def play_solos(self):
        """
         Asks each member musician to play a solo, in the order they were added to band.
        """
        solo = ' '
        for i in band_list:
            solo += f'{i.play_solo()}'
        return solo[:-1]
    


    def __str__(self):
        return("This is the Band class")

    
    def __repr__(self):
        return self.name

    
    @classmethod
    def to_list(cls):
        return cls.band_list

    
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
        return self.musicians






