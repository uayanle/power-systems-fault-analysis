import csv


def load_breakers():
    breakers = []
    with open('data/breakers.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['rating_kA'] = float(row['rating_kA'])
            breakers.append(row)
    return breakers


print(load_breakers())


def select_breaker(fault_current_kA):
    breakers = load_breakers()
    suitable_breakers = [
        breaker for breaker in breakers if breaker['rating_kA'] >= fault_current_kA]
    if suitable_breakers:
        return min(suitable_breakers, key=lambda x: x['rating_kA'])
    else:
        return None
