"""Six individual temperature conversion functions."""


def convertCelsiusToKelvin(celsius):
    """Return the converted temperature as a float."""
    return float(celsius) + 273.15


def convertCelsiusToFahrenheit(celsius):
    """Return the converted temperature as a float."""
    return float(celsius) * 9.0 / 5.0 + 32.0


def convertFahrenheitToCelsius(fahrenheit):
    """Return the converted temperature as a float."""
    return (float(fahrenheit) - 32.0) * 5.0 / 9.0


def convertFahrenheitToKelvin(fahrenheit):
    """Return the converted temperature as a float."""
    return (float(fahrenheit) - 32.0) * 5.0 / 9.0 + 273.15


def convertKelvinToFahrenheit(kelvin):
    """Return the converted temperature as a float."""
    return (float(kelvin) - 273.15) * 9.0 / 5.0 + 32.0


def convertKelvinToCelsius(kelvin):
    """Return the converted temperature as a float."""
    return float(kelvin) - 273.15
