from calculations import calculate_transformer_impedance, calculate_cable_impedance, calculate_fault_current, calculate_fault_level, calculate_voltage_drop
from components import Transformer, Cable, PowerSystem
from validations import validate_transformer, validate_cable

# Create instances of Transformer and Cable
transformer = Transformer(rating=2_000_000, voltage=11_000, impedance=6)
cable = Cable(length=2, impedance_per_km=0.1)

# Create an instance of PowerSystem
transformer_cable_system = PowerSystem(transformer=transformer, cable=cable)

# Calculate transformer impedance
transformer_impedance = calculate_transformer_impedance(
    transformer_cable_system.transformer.impedance,
    transformer_cable_system.transformer.voltage,
    transformer_cable_system.transformer.rating
)

# Calculate cable impedance
cable_impedance = calculate_cable_impedance(
    transformer_cable_system.cable.impedance_per_km,
    transformer_cable_system.cable.length
)

# Calculate total impedance
total_impedance = transformer_impedance + cable_impedance

# calculate fault current
fault_current = calculate_fault_current(
    transformer_cable_system.transformer.voltage,
    total_impedance
)

# Calculate fault level
fault_level = calculate_fault_level(
    transformer_cable_system.transformer.voltage,
    fault_current
)

# Calculate voltage drop
voltage_drop = calculate_voltage_drop(
    fault_current,
    cable_impedance
)


print("Transformer impedance:", transformer_impedance, "Ω")
print("Cable impedance:", cable_impedance, "Ω")
print("Total impedance:", total_impedance, "Ω")
print("Fault current:", fault_current, "A")
print("Fault level:", fault_level, "MVA")
print("Voltage drop:", voltage_drop, "V")
