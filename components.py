class Transformer:
    def __init__(self, rating, voltage, impedance):
        self.rating = rating
        self.voltage = voltage
        self.impedance = impedance


class Cable:
    def __init__(self, length, impedance_per_km):
        self.length = length
        self.impedance_per_km = impedance_per_km


class PowerSystem:
    def __init__(self, transformer, cable):
        self.transformer = transformer
        self.cable = cable
