import click
from typing import Dict, List


class Converter:
    def __init__(self, abbr: str, base_name: str, base: int, color: str):
        if not isinstance(abbr, str):
            raise click.BadParameter("abbr must be a string")
        self.abbr = abbr
        if not isinstance(base_name, str):
            raise click.BadParameter("base_name must be a string")
        self.base_name = base_name
        if not isinstance(base, int):
            raise click.BadParameter("base must be a integer")
        self.base = base
        if not isinstance(color, str):
            raise click.BadParameter("color must be a string")
        self.color = color

    def validate(self, value: str) -> int:
        try:
            value_int = int(value, self.base)
            return value_int
        except ValueError:
            raise click.BadParameter(
                f"{value} is not a valid number in {self.base_name} base"
            )

    def convert(self, value: int) -> Dict[str, str]:
        try:
            octal = oct(value)[2:]
            decimal = str(int(value))

            binary_value = bin(value)[2:]
            zeros_missing = (4 - len(binary_value) % 4) % 4
            binary_value = ("0" * zeros_missing) + binary_value
            binary = " ".join(
                [binary_value[i : i + 4] for i in range(0, len(binary_value), 4)]
            )

            hexadecimal = hex(value)[2:].upper()

            return {
                "OCT": octal,
                "DEC": decimal,
                "BIN": binary,
                "HEX": hexadecimal,
            }
        except ValueError:
            raise click.BadParameter("Error in convertion")


def make_converters() -> List[Converter]:
    return [
        Converter("o", "Octal", 8, "red"),
        Converter("d", "Decimal", 10, "green"),
        Converter("b", "Binary", 2, "blue"),
        Converter("h", "Hexadecimal", 16, "magenta"),
    ]