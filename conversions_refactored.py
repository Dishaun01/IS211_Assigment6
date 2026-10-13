"""General conversions using a common base unit for each category."""


class ConversionNotPossible(Exception):
    """Raised for unknown units or conversions between incompatible units."""


# Each entry contains category, scale, and offset.
# base_value = value * scale + offset (Celsius or meters).
_UNITS = {
    "celsius": ("temperature", 1.0, 0.0),
    "fahrenheit": ("temperature", 5.0 / 9.0, -32.0 * 5.0 / 9.0),
    "kelvin": ("temperature", 1.0, -273.15),
    "miles": ("distance", 1609.344, 0.0),
    "yards": ("distance", 0.9144, 0.0),
    "meters": ("distance", 1.0, 0.0),
}


def convert(fromUnit, toUnit, value):
    """Convert between supported units; names ignore case and outer spaces."""
    try:
        source = _UNITS[fromUnit.strip().lower()]
        target = _UNITS[toUnit.strip().lower()]
    except (KeyError, AttributeError) as error:
        raise ConversionNotPossible(
            f"Unknown unit: {fromUnit!r} or {toUnit!r}"
        ) from error

    if source[0] != target[0]:
        raise ConversionNotPossible(
            f"Cannot convert {fromUnit} to {toUnit}"
        )

    numeric_value = float(value)
    if source == target:
        return numeric_value
    base_value = numeric_value * source[1] + source[2]
    return float((base_value - target[2]) / target[1])
