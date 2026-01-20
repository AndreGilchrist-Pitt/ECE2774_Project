'''
Students must develop a Python program that models and solves a DC circuit with a voltage
source, a series resistor, and a load resistor connected between buses A and B. The program
should calculate and display the voltage at each bus and the current flowing through the circuit.

Class implementation:
    Solution
        Attributes:
            circuit (Circuit): When creating a solution object, you must pass a Circuit
                                object as an argument.
        Methods:
            do_power_flow(): Solves the circuit by finding bus voltages and circuit
                            current. First calculate the current using element conductance values,
                            then determine the voltage at bus B. This algorithm is designed
                            specifically for this circuit, as the main goal is to understand the coding
                            implementation.
'''
from Utils.Classes.Circuit import Circuit


class Solution:
    def __init__(self, circuit: Circuit):
        self.circuit = circuit

    def do_power_flow(self):
        # Get the resistor and load from dictionaries
        resistor = list(self.circuit.resistors.values())[0]
        load = list(self.circuit.loads.values())[0]

        # Calculate circuit conductance
        total_g = 1/(1/resistor.g + 1/load.g)

        # Calculate circuit current (I = V * G)
        current = self.circuit.vsource.v * total_g
        self.circuit.set_i(current)

        # Calculate voltage drop across the series resistor
        v_drop = current / resistor.g

        # Calculate voltage at bus B
        v_bus_b = self.circuit.vsource.v - v_drop

        # Set voltage at bus A
        bus_a = self.circuit.buses[self.circuit.vsource.bus1]
        bus_a.set_bus_v(self.circuit.vsource.v)

        # Set voltage at bus B
        bus_b = self.circuit.buses[load.bus1]
        bus_b.set_bus_v(v_bus_b)

        #move to circuit class
        #self.circuit.print_nodal_voltage()
        #self.circuit.print_circuit_current()

if __name__ == "__main__":
    circuit = Circuit("circuit1")
    circuit.add_bus("bus1")
    circuit.add_bus("bus2")
    circuit.add_resistor_element("resistor1", "bus1", "bus2", 5)
    circuit.add_load_element("load1", "bus2", 2000, 100)
    circuit.add_vsource_element("vsource1", "bus1", 100)
    solution = Solution(circuit)
    solution.do_power_flow()