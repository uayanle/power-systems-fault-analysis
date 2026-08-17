import math


# 1. Calculate transformer impedance
def calculate_transformer_impedance(impedance_percentage, voltage, rating):
    impedance = (
        impedance_percentage / 100
    ) * (voltage ** 2 / rating)

    return impedance


# 2. Calculate cable impedance
def calculate_cable_impedance(impedance_per_km, cable_length):
    impedance = impedance_per_km * cable_length

    return impedance


# 3. Calculate three-phase fault current
def calculate_fault_current(voltage, total_impedance):
    fault_current = voltage / (
        math.sqrt(3) * total_impedance
    )

    return fault_current


# 4. Calculate fault level
def calculate_fault_level(voltage, fault_current):
    fault_level = (
        math.sqrt(3) * voltage * fault_current
    ) / 1_000_000

    return fault_level


# 5. Calculate voltage drop
def calculate_voltage_drop(current, cable_impedance):
    voltage_drop = current * cable_impedance

    return voltage_drop


transformer_z = calculate_transformer_impedance(
    6,
    11000,
    2000000
)

cable_z = calculate_cable_impedance(
    0.1,
    2
)

total_z = transformer_z + cable_z

print(total_z)

