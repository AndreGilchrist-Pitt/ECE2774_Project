# Simple DC Circuit Simulator

## Introduction

The **Simple DC Circuit Simulator** is a Python-based tool designed to model and solve basic DC electrical
circuits. This simulator provides an intuitive, object-oriented approach to circuit analysis, allowing users to
construct circuits programmatically and automatically compute key electrical parameters such as bus voltages and circuit
currents.

### Purpose

The primary purpose of this simulator is to:

1. **Demonstrate circuit analysis principles** through practical implementation
2. **Provide a hands-on learning tool** for understanding DC circuit behavior
3. **Illustrate object-oriented programming concepts** in the context of the project hierarchy and class structure instructions
4. **Allow rapid prototyping and testing** of simple circuit configurations

### Key Features and Functionality

The Simple Circuit Simulator offers the following capabilities:

#### Circuit Modeling

- **Component-based architecture:** Define buses, resistors, loads, and voltage sources as individual objects
- **Flexible circuit construction:** Add components programmatically using intuitive methods
- **Multiple element support:** Handle circuits with various resistors and loads connected across buses

#### Electrical Analysis

- **Automatic power flow calculation:** Solve for all bus voltages and circuit currents
- **Conductance-based computation:** Utilize efficient conductance methods for circuit analysis
- **KVL and Ohm's Law implementation:** Apply fundamental electrical principles automatically

#### Results and Output

- **Nodal voltage display:** View voltage levels at all circuit buses
- **Current calculation:** Determine the current flowing through the circuit

---

## Problem Statement

The simulator addresses the following fundamental circuit analysis problem:

> **Given a DC circuit consisting of a voltage source, a series resistor, and a load connected between two buses,
determine the voltage at each bus and the current flowing through the circuit.**

### Circuit Configuration  

[Voltage Source] → [Bus A] → [Series Resistor] → [Bus B] → [Load] → [Ground]

**Known Parameters:**

- Voltage source value (V)
- Series resistor resistance (Ω)
- Load power rating (W)
- Load voltage rating (V)

**Unknown Parameters to Solve:**

- Voltage at Bus A (set by source)
- Voltage at Bus B (calculated)
- Circuit current (calculated)

## Solution Methodology

The simulator employs the following approach:

1. **Model each component** as a Python object with relevant electrical properties
2. **Calculate conductances** for resistive elements (G = 1/R) and loads (G = P/V²)
3. **Determine total circuit conductance** using series combination formulas
4. **Apply Ohm's Law** to calculate circuit current (I = V × G)
5. **Use Kirchhoff's Voltage Law (KVL)** to find bus voltages

---

## Real-World Applications

While simplified, this simulator provides foundational skills applicable to numerous real-world scenarios:

### Power Distribution Systems

**Application:** Modeling voltage drops in power transmission lines

In electrical power distribution, understanding voltage drops between substations (buses) due to line resistance is
critical. This simulator demonstrates:

- How series resistance affects voltage delivery
- The relationship between load power and voltage regulation
- Basic power flow analysis techniques

---

## Detailed Example Case

This section provides a step-by-step walkthrough of how the Simple Circuit Simulator solves a practical DC circuit problem.

### Problem Definition

**Scenario:** A small DC power system supplies power to a residential lighting load through a transmission line.

**Circuit Components:**
- **Voltage Source:** 120 V DC supply
- **Bus A (Source Bus):** Connection point at the voltage source
- **Series Resistor (Transmission Line):** 2.5 Ω representing line resistance
- **Bus B (Load Bus):** Connection point at the load
- **Load:** 500 W lighting system rated at 100 V

**Circuit Diagram:**
```
[120V Source] ─── Bus A ───[2.5Ω Line]─── Bus B ───[500W Load @ 100V]─── Ground
                 (V_A=?)                   (V_B=?)
                           I = ?
```

**Objective:** Determine:
1. Voltage at Bus A (V_A)
2. Voltage at Bus B (V_B)
3. Current flowing through the circuit (I)

### Solution Process

The simulator solves this problem using the following systematic approach:

#### Step 1: Initialize Circuit Components

```python
# Create buses
bus_a = Bus(name="Bus A")
bus_b = Bus(name="Bus B")

# Create voltage source (120V at Bus A)
source = VSource(voltage=120, bus=bus_a)

# Create series resistor (2.5Ω transmission line from Bus A to Bus B)
line_resistor = Resistor(resistance=2.5, from_bus=bus_a, to_bus=bus_b)

# Create load (500W rated at 100V, connected from Bus B to ground)
lighting_load = Load(power=500, voltage=100, from_bus=bus_b)

# Assemble circuit
circuit = Circuit()
circuit.add_bus(bus_a)
circuit.add_bus(bus_b)
circuit.add_voltage_source(source)
circuit.add_resistor(line_resistor)
circuit.add_load(lighting_load)
```

#### Step 2: Calculate Component Conductances

The simulator converts resistance values to conductances for numerical computation.

**Line Resistor Conductance:**
```
G_line = 1 / R_line = 1 / 2.5 Ω = 0.4 S
```

**Load Conductance:**

First, calculate the load's equivalent resistance at rated conditions:
```
R_load = V_rated² / P_rated = (100 V)² / 500 W = 10000 / 500 = 20 Ω
```

Then convert to conductance:
```
G_load = 1 / R_load = 1 / 20 Ω = 0.05 S
```

#### Step 3: Calculate Total Circuit Conductance

For series elements, the total conductance is:
```
G_total = 1 / (1/G_line + 1/G_load)
        = 1 / (1/0.4 + 1/0.05)
        = 1 / (2.5 + 20)
        = 1 / 22.5
        = 0.0444 S
```

Alternatively, using resistances:
```
R_total = R_line + R_load = 2.5 Ω + 20 Ω = 22.5 Ω
```

#### Step 4: Solve for Circuit Current (Using Ohm's Law and KVL)

Apply KVL around the loop:
```
V_source = I × R_total
```

Solve for current:
```
I = V_source / R_total
  = 120 V / 22.5 Ω
  = 5.333 A
```

Or using conductance:
```
I = V_source × G_total
  = 120 V × 0.0444 S
  = 5.333 A
```

#### Step 5: Calculate Bus Voltages

**Bus A Voltage:**

Bus A is directly connected to the voltage source:
```
V_A = V_source = 120 V
```

**Bus B Voltage:**

Apply Ohm's Law to find voltage drop across the line resistor:
```
V_drop_line = I × R_line = 5.333 A × 2.5 Ω = 13.333 V
```

Apply KVL from Bus A to Bus B:
```
V_B = V_A - V_drop_line = 120 V - 13.333 V = 106.667 V
```

Alternatively, calculate voltage across the load:
```
V_load = I × R_load = 5.333 A × 20 Ω = 106.667 V
V_B = V_load = 106.667 V
```

#### Step 6: Verify Solution Using Power

**Power delivered by source:**
```
P_source = V_source × I = 120 V × 5.333 A = 640 W
```

**Power dissipated in line:**
```
P_line = I² × R_line = (5.333 A)² × 2.5 Ω = 71.11 W
```

**Power delivered to load:**
```
P_load = V_B × I = 106.667 V × 5.333 A = 568.89 W
```

**Verification (Power Balance):**
```
P_source = P_line + P_load
640 W ≈ 71.11 W + 568.89 W ≈ 640 W ✓
```

### Expected Output

When the simulator runs this example case, it produces the following output:

```
========================================
Simple DC Circuit Simulator
========================================

Circuit Configuration:
  Voltage Source: 120.0 V at Bus A
  Transmission Line: 2.5 Ω (Bus A → Bus B)
  Load: 500 W @ 100 V (Bus B → Ground)

========================================
Solution Results:
========================================

Circuit Current: 5.333 A

Bus Voltages:
  Bus A: 120.000 V
  Bus B: 106.667 V

Component Analysis:
  Line Resistor (2.5 Ω):
    Voltage Drop: 13.333 V
    Power Loss: 71.11 W
    Conductance: 0.400 S

  Lighting Load:
    Voltage: 106.667 V
    Power Delivered: 568.89 W
    Equivalent Resistance: 20.0 Ω
    Conductance: 0.050 S

Total Circuit Resistance: 22.5 Ω
Total Circuit Conductance: 0.0444 S

========================================
Power Balance:
========================================
  Source Power: 640.0 W
  Line Losses: 71.11 W
  Load Power: 568.89 W
  Efficiency: 88.9%

========================================
```

### Analysis and Observations

From this example, we can observe several important circuit characteristics:

1. **Voltage Drop:** The 2.5 Ω transmission line causes a voltage drop of 13.333 V (11.1% drop from source)

2. **Load Voltage vs Rating:** The load receives 106.667 V, which is 6.67% higher than its rated 100 V. This is acceptable for most loads but demonstrates the importance of voltage regulation.

3. **Power Efficiency:** Only 88.9% of the source power reaches the load, with 11.1% lost in the transmission line resistance.

4. **Current Magnitude:** The circuit draws 5.333 A, which can be used for wire sizing and protection device selection.

5. **Design Implications:**
   - To reduce line losses, decrease line resistance (larger wire) or reduce load power
   - To improve voltage regulation, consider using a higher source voltage or lower resistance line
   - The 71 W of line loss may require thermal management considerations

This example demonstrates how the simulator provides comprehensive insight into DC circuit behavior, enabling informed design and troubleshooting decisions.
