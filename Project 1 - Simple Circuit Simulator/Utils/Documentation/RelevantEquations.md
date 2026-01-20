# Circuit Simulator - Electrical Equations Documentation

## Overview
This document provides a comprehensive reference for all electrical equations used in the Simple DC Circuit Simulator. Each equation is presented with its mathematical form, physical meaning, units, and implementation context.

---

## 1. Ohm's Law

### Definition
Ohm's Law describes the relationship between voltage, current, and resistance in an electrical circuit.

### Basic Forms

**Solving for Voltage:**
```
V = I × R
```

**Solving for Current:**
```
I = V / R
```

**Solving for Resistance:**
```
R = V / I
```

### Variables and Units
| Variable | Description | SI Unit | Symbol |
|----------|-------------|---------|--------|
| V | Voltage | Volt | V |
| I | Current | Ampere | A |
| R | Resistance | Ohm | Ω |

### Physical Meaning
Ohm's Law states that the voltage drop across a resistor is directly proportional to the current flowing through it, with resistance as the proportionality constant.

### Implementation in Simulator
```python
# Calculating voltage drop across resistor
V_drop = I * R_resistor

# Using conductance form
V_drop = I / G_resistor
```

---

## 2. Power-Voltage Relationship

### Definition
Power dissipation in circuit elements relates to voltage and current, or equivalently to voltage/current and resistance.

### Basic Forms

**Power from Voltage and Current:**
```
P = V × I
```

**Power from Current and Resistance:**
```
P = I² × R
```

**Power from Voltage and Resistance:**
```
P = V² / R
```

**Power from Voltage and Conductance:**
```
P = V² × G
```

### Variables and Units
| Variable | Description | SI Unit | Symbol |
|----------|-------------|---------|--------|
| P | Power | Watt | W |
| V | Voltage | Volt | V |
| I | Current | Ampere | A |
| R | Resistance | Ohm | Ω |
| G | Conductance | Siemens | S |

### Physical Meaning
Power represents the rate of energy dissipation or transfer in a circuit element. In resistors, electrical energy is converted to heat. In loads, electrical energy may be converted to other forms (mechanical, light, etc.).

### Implementation in Simulator
```python
# Power dissipated in resistor
P_resistor = I**2 * R_resistor

# Power delivered to load
P_load = V_load * I_load

# Using conductance
P = V**2 * G
```

---

## 3. Conductance Calculations

### Definition
Conductance is the reciprocal of resistance and represents the ease with which current flows through an element.

### Basic Form
```
G = 1 / R
```

Or equivalently:
```
R = 1 / G
```

### Variables and Units
| Variable | Description | SI Unit | Symbol |
|----------|-------------|---------|--------|
| G | Conductance | Siemens | S (or Ω⁻¹) |
| R | Resistance | Ohm | Ω |

### Physical Meaning
Conductance quantifies how easily current flows through a component. Higher conductance means lower resistance. This form is particularly useful in nodal analysis where conductances sum directly.

### Implementation in Simulator
```python
# Converting resistance to conductance
G = 1.0 / R

# Using conductance in Ohm's law
I = V * G

# Parallel conductances add directly
G_total = G1 + G2 + G3
```

---

## 4. Kirchhoff's Voltage Law (KVL)

### Definition
KVL states that the sum of all voltages around any closed loop in a circuit equals zero.

### Mathematical Form
```
Σ V_loop = 0
```

Or equivalently, the sum of voltage rises equals the sum of voltage drops:
```
Σ V_sources = Σ V_drops
```

### For Simple Series Circuit
```
V_source = V_R1 + V_R2 + ... + V_Rn + V_load
```

### Variables and Units
| Variable | Description | SI Unit | Symbol |
|----------|-------------|---------|--------|
| V | Voltage | Volt | V |

### Physical Meaning
KVL is a consequence of energy conservation. As charge moves around a closed loop, the net energy change must be zero. Energy gained from sources equals energy lost in resistive elements.

### Implementation in Simulator

**Single Loop Circuit:**
```python
# For series circuit: V_source = sum of all voltage drops
V_source = I * (R1 + R2 + ... + Rn + R_load)

# Solving for current
I = V_source / (R1 + R2 + ... + Rn + R_load)
```

**Using Conductance Form:**
```python
# Total conductance for series elements
G_total = 1 / (1/G1 + 1/G2 + ... + 1/Gn)

# Or equivalently
R_total = 1/G1 + 1/G2 + ... + 1/Gn
```

**Matrix Form for Complex Circuits:**
```python
# Nodal analysis using conductance matrix
# [G] × [V] = [I]
# Where:
#   [G] = conductance matrix (derived from KVL/KCL)
#   [V] = node voltage vector
#   [I] = current source vector
```

### Application to System Voltage and Current Solution

For the simulator, KVL is applied to:
1. **Identify the circuit loop** (series path from source through all components)
2. **Sum all resistances** (or equivalently, compute equivalent conductance)
3. **Apply KVL** to get: V_source = I × R_total
4. **Solve for current**: I = V_source / R_total
5. **Calculate individual voltages** using Ohm's Law: V_i = I × R_i

---

## 5. Summary of Key Equations Used in Simulator

### Circuit Solution Process
```python
# Step 1: Calculate total resistance
R_total = R1 + R2 + ... + Rn + R_load

# Step 2: Solve for circuit current (KVL)
I = V_source / R_total

# Step 3: Calculate voltage across each element (Ohm's Law)
V_i = I * R_i

# Step 4: Calculate power in each element
P_i = I**2 * R_i  # or V_i * I or V_i**2 / R_i
```

### Using Conductance Form
```python
# Step 1: Convert resistances to conductances
G_i = 1 / R_i

# Step 2: Calculate total conductance for series
G_total = 1 / (1/G1 + 1/G2 + ... + 1/Gn)

# Step 3: Solve for current
I = V_source * G_total

# Step 4: Calculate voltages and power
V_i = I / G_i
P_i = V_i**2 * G_i
```

---

## References and Notes

- All equations assume DC (steady-state) operation
- Sign conventions: current flows from positive to negative terminal
- Power values are positive for energy dissipation
- Conductance form is preferred for numerical stability in some implementations
