def validate_positive_number(value):
    try:
        number = float(value)
    except (ValueError, TypeError):
        raise ValueError("The value must be a positive number.")
    except (ValueError, TypeError):
        raise ValueError("The value must be a valid number.")

    if number <= 0:
        raise ValueError("The value must be a positive number.")

    return number


def validate_transformer(rating, voltage, impedance):
    rating = validate_positive_number(rating)
    voltage = validate_positive_number(voltage)
    impedance = validate_positive_number(impedance)

    return rating, voltage, impedance


def validate_cable(length, impedance_per_km):
    length = validate_positive_number(length)
    impedance_per_km = validate_positive_number(impedance_per_km)

    return length, impedance_per_km


print(validate_positive_number(-10))
