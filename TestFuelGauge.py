# import pytest
from Fuel_Gauage_prog import taking_value, calculating_fuel_gauge

def test_taking_value():
    assert taking_value("what is the value?") == '1/4'
    assert taking_value("what is the value?") == '1/5'


def test_calculating_fuel_gauge():
    assert calculating_fuel_gauge() == '50'



#
#
# def test_taking_value(monkeypatch):
#     # Mock input to return "1/2" when called
#     monkeypatch.setattr('builtins.input', lambda _: "1/2")
#
#     # Test the function
#     assert taking_value("Enter the current value of your fuel meter? ") == "1/2"
#
#
# def test_calculating_fuel_gauge_valid(monkeypatch):
#     # Mock input to return "1/2"
#     monkeypatch.setattr('builtins.input', lambda _: "1/2")
#
#     # Test the function with the valid input
#     assert int(calculating_fuel_gauge()) == 50
#
#     # Mock input to return "3/4"
#     monkeypatch.setattr('builtins.input', lambda _: "3/4")
#
#     # Test the function with another valid input
#     assert int(calculating_fuel_gauge()) == 75
#
#
# def test_calculating_fuel_gauge_zero_division(monkeypatch):
#     # Mock input to return "1/0", which should be handled by the loop
#     monkeypatch.setattr('builtins.input', lambda _: "1/0")
#
#     # Since the function should keep looping, we'll need to set it up to return a valid value after the invalid one
#     monkeypatch.setattr('builtins.input', lambda _: "1/2")
#
#     # Test the function after correcting the input
#     assert int(calculating_fuel_gauge()) == 50
#
#
# def test_calculating_fuel_gauge_invalid_input(monkeypatch):
#     # Mock input to return an invalid input "abc/def"
#     monkeypatch.setattr('builtins.input', lambda _: "abc/def")
#
#     # Since the function should keep looping, we'll need to set it up to return a valid value after the invalid one
#     monkeypatch.setattr('builtins.input', lambda _: "1/2")
#
#     # Test the function after correcting the input
#     assert int(calculating_fuel_gauge()) == 50
