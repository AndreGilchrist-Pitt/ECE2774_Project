'''
Class Implementation:
Bus:
    Attributes:
        name (str): The user should provide this as an argument when defining the object
        v (float): Represents the voltage at the bus. For buses connected to a voltage source,
                    the voltage updates when the source is created.
                    For all other buses, the voltage updates during the power flow calculation.
    Methods:
        set_bus_v(bus_v: float): Sets the voltage at the bus
'''


class Bus:
    def __init__(self, name: str):
        self.name = name
        self.v = 0.0
    def set_bus_v(self, bus_v: float):
        self.v = bus_v



if __name__ == "__main__":
    bus = Bus("bus1")
    print(bus.v)
    bus.set_bus_v(100)
    print(bus.v)
    print(bus)