class Transformer:
    def __init__(self, rating, voltage, impedance):
        self.rating = rating
        self.voltage = voltage
        self.impedance = impedance


transformer1 = Transformer(
    -2_000_000,
    11_000,
    6,
)

print("Transformer rating:", transformer1.rating, "VA")
print("Transformer voltage:", transformer1.voltage, "V")
print("Transformer impedance:", transformer1.impedance, "%")

transformer2 = Transformer(
    5_000_000,
    11_000,
    7
)

print("Transformer rating:", transformer2.rating, "VA")
print("Transformer voltage:", transformer2.voltage, "V")
print("Transformer impedance:", transformer2.impedance, "%")


class Cable:
    def __init__(self, length, impedance_per_km):
        self.length = length
        self.impedance_per_km = impedance_per_km


cable1 = Cable(
    2,
    0.1
)

print("Cable length:", cable1.length, "km")
print("Cable impedance per km:", cable1.impedance_per_km, "Ω/km")

cable2 = Cable(
    5,
    0.05
)

print("Cable length:", cable2.length, "km")
print("Cable impedance per km:", cable2.impedance_per_km, "Ω/km")


class PowerSystem:
    def __init__(self, transformer, cable):
        self.transformer = transformer
        self.cable = cable


power_system1 = PowerSystem(transformer1, cable1)
print("Power system 1: Transformer rating:", power_system1.transformer.rating,
      "VA, Cable length:", power_system1.cable.length, "km")

power_system2 = PowerSystem(transformer2, cable2)
print("Power system 2: Transformer rating:", power_system2.transformer.rating,
      "VA, Cable length:", power_system2.cable.length, "km")
