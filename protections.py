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
