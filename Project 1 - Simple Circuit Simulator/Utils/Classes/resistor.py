'''
Class Implementation:
Resistor:
    Attributes:
        name (str): The user should provide this as an argument when defining the object
        bus1 (str): The user should provide this as an argument when defining the object
        bus2 (str): The user should provide this as an argument when defining the object
        r (float): The user should provide this as an argument when defining the object
        g (float): The user should provide this as an argument when defining the object
    Methods:
        set_bus_v(bus_v: float): Sets the voltage at the bus
'''

from Utils.Classes.bus import Bus
class Resistor:
    def __init__(self, name: str, bus1: Bus, bus2: Bus, r: float):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r
        self._g = self.calc_g()

    @property
    def g(self) -> float:
        return self._g

    def calc_g(self) -> float:
        """Calculates the conductance value (g = 1/r)"""
        if self.r == 0:
            raise ValueError(f"Resistor {self.name}: Resistance cannot be zero")
        return 1.0 / self.r

if __name__ == "__main__":
    resistor = Resistor("resistor1", "bus1", "bus2", 5)
    print(resistor.g)