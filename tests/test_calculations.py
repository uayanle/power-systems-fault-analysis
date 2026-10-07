import pytest
from calculations import calculate_transformer_impedance


def test_calculate_transformer_impedance():
    result = calculate_transformer_impedance(6, 11000, 2000000)
    # Allowing a small relative tolerance
    assert result == pytest.approx(3.63, rel=1e-2)
