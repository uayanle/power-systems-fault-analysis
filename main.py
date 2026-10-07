from calculations import calculate_transformer_impedance, calculate_cable_impedance, calculate_fault_current, calculate_fault_level, calculate_voltage_drop
from components import Transformer, Cable, PowerSystem
from validations import validate_transformer, validate_cable
from protections import select_breaker


# Create instances of Transformer and Cable
transformer = Transformer(rating=2_000_000, voltage=11_000, impedance=6)
cable = Cable(length=2, impedance_per_km=0.1)

# Create an instance of PowerSystem
transformer_cable_system = PowerSystem(transformer=transformer, cable=cable)

# validate transfomer and cable
validate_transformer(transformer.rating,
                     transformer.voltage, transformer.impedance)

validate_cable(cable.length, cable.impedance_per_km)

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

fault_current_kA = fault_current / 1000  # Convert to kA
selected_breaker = select_breaker(fault_current_kA)


# select breaker based on fault current
if selected_breaker:
    breaker_rating = selected_breaker['rating_kA']
    breaker_type = selected_breaker['type']
else:
    breaker_rating = None
    breaker_type = None


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


print("=" * 60)
print("              POWER SYSTEM FAULT ANALYSIS")
print("=" * 60)

print("\nSYSTEM DATA")
print("-" * 60)
print(f"System Voltage              {transformer.voltage / 1000:.1f} kV")
print(f"Transformer Rating          {transformer.rating / 1_000_000:.1f} MVA")
print(f"Transformer Impedance       {transformer.impedance:.1f} %")
print(f"Cable Length                {cable.length:.1f} km")
print(f"Cable Impedance             {cable.impedance_per_km:.2f} Ω/km")

print("\nFAULT ANALYSIS")
print("-" * 60)
print(f"Transformer Impedance       {transformer_impedance:.2f} Ω")
print(f"Cable Impedance             {cable_impedance:.2f} Ω")
print(f"Total System Impedance      {total_impedance:.2f} Ω")
print(f"Fault Current               {fault_current_kA:.2f} kA")
print(f"Fault Level                 {fault_level:.2f} MVA")
print(f"Voltage Drop                {voltage_drop:.2f} V")

print("\nPROTECTION")
print("-" * 60)

if selected_breaker:
    print(
        f"Recommended Breaker         {breaker_rating:.1f} kA {breaker_type}")
    print("Protection Status            SUITABLE")
else:
    print("Recommended Breaker         NO SUITABLE BREAKER FOUND")
    print("Protection Status            UNSUITABLE")

print("=" * 60)
