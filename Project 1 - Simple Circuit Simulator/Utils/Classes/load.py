'''
Class Implementation:
Load:
    Attributes:
        name (str): The user should provide this as an argument when defining the object
        bus1 (str): The user should provide this as an argument when defining the object
        p (float): The user should provide this as an argument when defining the object
        v (float): The user should provide this as an argument when defining the object
        q (float): The user should provide this as an argument when defining the object
        r (float): The user should provide this as an argument when defining the object
        g (float): It should be calculated internally using the calc_g method
    Methods:
        calc_g(): Calculates the conductance value
'''
from Utils.Classes.bus import Bus
class Load:
    def __init__(self,name: str,bus1: Bus,p: float, v: float ):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.v = v
        self._g = self.calc_g()

    @property
    def g(self)->float:
        return self._g
    def calc_g(self)->float:
        return self.p / self.v**2

if __name__ == "__main__":

    load = Load("load1", "bus1", 2000, 100)
    print(load.g)
