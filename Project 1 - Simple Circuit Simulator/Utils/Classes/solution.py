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
from Utils.Classes.circuit import Circuit


class Solution:
    def __init__(self, circuit: Circuit):
        self._circuit = circuit

    def do_power_flow(self):
        # Get the resistor and load from dictionaries
        resistors = list(self._circuit.resistors.values())
        loads = list(self._circuit.loads.values())
        elements = resistors + loads
        if not elements:
            raise ValueError("Circuit must contain at least one resistor or load")

        # Calculate circuit conductance
        total_g = 1 / sum(1 / element.g for element in elements)

        # Calculate circuit current (I = V * G)
        current = self._circuit.vsource.v * total_g
        self._circuit.set_i(current)

        # Calculate total voltage drop across series resistors
        v_drop = sum(current / resistor.g for resistor in resistors)

        # Calculate voltage at bus B
        v_bus_b = self._circuit.vsource.v - v_drop

        # Set voltage at bus B (connected to loads)
        for load in loads:
            load.bus1.set_bus_v(v_bus_b)

if __name__ == "__main__":
    circuit = Circuit("circuit1")
    circuit.add_bus("bus1")
    circuit.add_bus("bus2")
    circuit.add_resistor_element("resistor1", circuit.buses["bus1"], circuit.buses["bus2"], 5)
    circuit.add_load_element("load1", circuit.buses["bus2"], 2000, 100)
    circuit.add_vsource_element("vsource1", circuit.buses["bus1"], 100)
    solution = Solution(circuit)
    solution.do_power_flow()
