'''
Class Implementation:
VSource:
    Attributes:
        name (str): The user should provide this as an argument when defining the object
        bus1 (str): The user should provide this as an argument when defining the object.
        v (float): The user should provide this as an argument when defining the object.
'''

class VSource:
    def __init__(self, name: str, bus1: str, v: float):
        self.name = name
        self.bus1 = bus1
        self.v = v

if __name__ == "__main__":
    vs = VSource("vs1", "bus1", 100)
    print(f"VSource {vs.name},Bus: {vs.bus1} ,Voltage: {vs.v} V")