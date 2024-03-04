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

    @staticmethod
    def _format_oct(value: int) -> str:
        octal_string = oct(value)[2:]
        octal = " ".join(
            reversed(
                [
                    octal_string[max(i - 3, 0) : i]
                    for i in range(len(octal_string), 0, -3)
                ]
            )
        )

        return octal

    @staticmethod
    def _format_dec(value: int) -> str:
        dec_string = str(value)
        decimal = ".".join(
            reversed(
                [dec_string[max(i - 3, 0) : i] for i in range(len(dec_string), 0, -3)]
            )
        )

        return decimal

    @staticmethod
    def _format_bin(value: int) -> str:
        bin_string = bin(value)[2:]
        missing_zeros = (4 - len(bin_string) % 4) % 4

        bin_string = f"{'0' * missing_zeros + bin_string}"
        binary = " ".join([bin_string[i : i + 4] for i in range(0, len(bin_string), 4)])

        return binary

    @staticmethod
    def _format_hex(value: int) -> str:
        hex_string = hex(value)[2:].upper()
        hexadecimal = " ".join(
            reversed(
                [hex_string[max(i - 4, 0) : i] for i in range(len(hex_string), 0, -4)]
            )
        )

        return hexadecimal

    def convert(self, value: int) -> Dict[str, str]:
        try:
            octal = self._format_oct(value)
            decimal = self._format_dec(value)
            binary = self._format_bin(value)
            hexadecimal = self._format_hex(value)

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
