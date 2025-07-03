import pytest
from app.conversor import fahrenheit_para_celsius, celsius_para_fahrenheit

# Usamos pytest para os testes unitários

def test_fahrenheit_para_celsius():
    assert fahrenheit_para_celsius(32.0) == pytest.approx(0.0)
    assert fahrenheit_para_celsius(212.0) == pytest.approx(100.0)
    assert fahrenheit_para_celsius(0.0) == pytest.approx(-17.77777777777778)
    assert fahrenheit_para_celsius(100.0) == pytest.approx(37.77777777777778)

def test_celsius_para_fahrenheit():
    assert celsius_para_fahrenheit(0.0) == pytest.approx(32.0)
    assert celsius_para_fahrenheit(100.0) == pytest.approx(212.0)
    assert celsius_para_fahrenheit(-20.0) == pytest.approx(-4.0)