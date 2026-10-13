"""Verbose unittest checks. Run with: python tests.py"""
import unittest
import conversions
from conversions_refactored import convert, ConversionNotPossible


class TemperatureTests(unittest.TestCase):
    def check_cases(self, function, cases):
        for value, expected in cases:
            with self.subTest(function=function.__name__, value=value):
                print(f"Checking {function.__name__}({value}): expected {expected}", flush=True)
                actual = function(value)
                self.assertIsInstance(actual, float)
                self.assertAlmostEqual(actual, expected, places=7)

    def test_convertCelsiusToKelvin(self):
        self.check_cases(conversions.convertCelsiusToKelvin, [(-40.0, 233.15), (0.0, 273.15), (100.0, 373.15), (300.0, 573.15), (-273.15, 0.0)])

    def test_convertCelsiusToFahrenheit(self):
        self.check_cases(conversions.convertCelsiusToFahrenheit, [(-40.0, -40.0), (0.0, 32.0), (100.0, 212.0), (300.0, 572.0), (-273.15, -459.67)])

    def test_convertFahrenheitToCelsius(self):
        self.check_cases(conversions.convertFahrenheitToCelsius, [(-40.0, -40.0), (32.0, 0.0), (212.0, 100.0), (572.0, 300.0), (-459.67, -273.15)])

    def test_convertFahrenheitToKelvin(self):
        self.check_cases(conversions.convertFahrenheitToKelvin, [(-40.0, 233.15), (32.0, 273.15), (212.0, 373.15), (572.0, 573.15), (-459.67, 0.0)])

    def test_convertKelvinToFahrenheit(self):
        self.check_cases(conversions.convertKelvinToFahrenheit, [(233.15, -40.0), (273.15, 32.0), (373.15, 212.0), (573.15, 572.0), (0.0, -459.67)])

    def test_convertKelvinToCelsius(self):
        self.check_cases(conversions.convertKelvinToCelsius, [(233.15, -40.0), (273.15, 0.0), (373.15, 100.0), (573.15, 300.0), (0.0, -273.15)])


class RefactoredTests(unittest.TestCase):
    def check_conversion(self, source, target, value, expected):
        with self.subTest(source=source, target=target, value=value):
            print(f"Checking {source} -> {target}: {value}, expected {expected}", flush=True)
            result = convert(source, target, value)
            self.assertIsInstance(result, float)
            self.assertAlmostEqual(result, expected, places=7)

    def test_all_temperature_conversions(self):
        # Known Celsius, Fahrenheit, Kelvin equivalents.
        rows = [(-40.0, -40.0, 233.15), (0.0, 32.0, 273.15),
                (100.0, 212.0, 373.15), (300.0, 572.0, 573.15),
                (-273.15, -459.67, 0.0)]
        units = ("Celsius", "Fahrenheit", "Kelvin")
        for i, source in enumerate(units):
            for j, target in enumerate(units):
                if i != j:
                    for row in rows:
                        self.check_conversion(source, target, row[i], row[j])

    def test_all_distance_conversions(self):
        # Fixed miles, yards, meters equivalents (international mile/yard).
        rows = [(0.0, 0.0, 0.0), (1.0, 1760.0, 1609.344),
                (0.5, 880.0, 804.672), (2.0, 3520.0, 3218.688),
                (5.0, 8800.0, 8046.72)]
        units = ("Miles", "Yards", "Meters")
        for i, source in enumerate(units):
            for j, target in enumerate(units):
                if i != j:
                    for row in rows:
                        self.check_conversion(source, target, row[i], row[j])

    def test_same_unit(self):
        for unit in ("Celsius", "Fahrenheit", "Kelvin", "Miles", "Yards", "Meters"):
            for value in (0.0, 1.0, 42.5):
                self.check_conversion(unit, unit, value, value)

    def test_incompatible_units(self):
        for temperature in ("Celsius", "Fahrenheit", "Kelvin"):
            for distance in ("Miles", "Yards", "Meters"):
                for source, target in ((temperature, distance), (distance, temperature)):
                    with self.subTest(source=source, target=target):
                        print(f"Checking {source} -> {target}: expect ConversionNotPossible", flush=True)
                        with self.assertRaises(ConversionNotPossible):
                            convert(source, target, 1.0)

    def test_unknown_units(self):
        for source, target in (("Feet", "Meters"), ("Meters", "Feet"), ("Feet", "Feet")):
            with self.subTest(source=source, target=target):
                print(f"Checking unknown units: {source} -> {target}", flush=True)
                with self.assertRaises(ConversionNotPossible):
                    convert(source, target, 1.0)

    def test_unit_name_normalization(self):
        self.check_conversion(" cELsius ", " FAHRENHEIT ", 100.0, 212.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
