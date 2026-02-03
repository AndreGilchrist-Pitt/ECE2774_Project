from Utils.Classes.circuit import Circuit
from Utils.Classes.solution import Solution

if __name__ == '__main__':
    circuit = Circuit("Simple DC Circuit")
    circuit.add_bus("A")
    circuit.add_bus("B")

    circuit.add_vsource_element("Va", circuit.buses["A"], 100.0)

    circuit.add_resistor_element("Rab", circuit.buses["A"], circuit.buses["B"], 5)

    circuit.add_load_element("Lb", circuit.buses["B"], 2000.0, 100.0)

    solution = Solution(circuit)
    solution.do_power_flow()
    circuit.print_nodal_voltage()
    circuit.print_circuit_current()
