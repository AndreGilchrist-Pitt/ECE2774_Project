'''
Circuit (Manages all components of the circuit)
    Attributes:
        name (str): The user should provide this as an argument when defining
                    the object.
        buses (Dict[str, Bus]): A dictionary where each item has a bus name as
                                the key and its corresponding Bus object as the value. The Bus object is
                                created using the add_bus method of the Circuit class.
        resistors (Dict[str, Resistor]): A dictionary where each item has a resistor
                                        name as the key and its corresponding Resistor object as the value. The
                                        Resistor object is created using the add_resistor method of the Circuit class.
        loads (Dict[str, Load]): A dictionary where each item has a load name as
                                the key and its corresponding Load object as the value. The Load object
                                is created using the add_load method of the Circuit class.
        vsource (Vsource): A VSource object. The Vsource object is created
                        using the add_vsource method of the Circuit class.
        i (float): Current flowing through the circuit. It should be updated during
                   the power flow calculation.
    Methods:
        add_bus(bus: str): Adds a bus to the circuit.
        add_resistor_element(name: str, bus1: str, bus2: str, r: float): Adds a resistor to the circuit.
        add_load_element(name: str, bus1: str, p: float, v: float): Adds a load to the circuit.
        add_vsource_element(name: str, bus1: str, v: float): Adds a voltage source to the circuit.
        set_i(i: float): Updates the i attribute.
        print_nodal_voltage(): Prints voltages at all buses.
        print_circuit_current(): Prints circuit current.
'''
from Utils.Classes.bus import Bus
from Utils.Classes.resistor import Resistor
from Utils.Classes.load import Load
from Utils.Classes.vsource import VSource

from typing import Dict

class Circuit:
    def __init__(self, name: str):
        self.name = name
        self.buses: Dict[str, Bus] = dict()
        self.resistors: Dict[str, Resistor] = {}
        self.loads: Dict[str, Load] = {}
        self.vsource = None
        self.i = 0.0

    def add_bus(self, bus: str):
        '''Adds a bus to the circuit'''
        self.buses[bus] = Bus(bus)

    def add_resistor_element(self, name: str, bus1: Bus, bus2: Bus, r: float):
        '''Adds a resistor to the circuit'''
        self.resistors[name] = Resistor(name, bus1, bus2, r)

    def add_load_element(self, name: str, bus1: Bus, p: float, v: float):
        '''Adds a load to the circuit'''
        self.loads[name] = Load(name, bus1, p, v)

    def add_vsource_element(self, name: str, bus1: Bus, v: float):
        '''Adds a voltage source to the circuit'''
        self.vsource = VSource(name, bus1, v)
        bus1.set_bus_v(v)

    def set_i(self, i: float):
        '''Updates the i attribute'''
        if i < 0:
            raise ValueError("Current cannot be negative")
        self.i = i

    def print_nodal_voltage(self):
        '''Prints voltages at all buses'''
        for bus in self.buses.values():
            print(f"Bus {bus.name}: {bus.v} V")

    def print_circuit_current(self):
        '''Prints circuit current'''
        print(f"Circuit Current: {self.i} A")


if __name__ == "__main__":
    circuit = Circuit("circuit1")
    circuit.add_bus("bus1")
    circuit.add_bus("bus2")
    circuit.add_resistor_element("resistor1", circuit.buses["bus1"], circuit.buses["bus2"], 5)
    circuit.add_load_element("load1", circuit.buses["bus1"], 2000, 100)
    circuit.add_vsource_element("vsource1", circuit.buses["bus1"], 100)
    circuit.set_i(10)
    circuit.print_nodal_voltage()
    circuit.print_circuit_current()
