import click
from typing import List

from .converter import Converter, make_converters


def main():
    converters = make_converters()

    click.clear()
    option = "main"

    while True:
        if option == "main":
            menu(converters)
            option = click.getchar()
        else:
            option = chosse_option(option, converters)


def menu(converters: List[Converter]) -> None:
    click.secho("Select a numeric system", bold=True, fg="white")

    for i, converter in enumerate(converters, start=1):
        click.secho(
            f"{ '└──  ' if len(converters) - i == 0 else '├──  '}",
            nl=False,
            fg=converter.color,
        )
        click.secho(f"{converter.abbr} - ", fg=converter.color, nl=False)
        click.echo(converter.base_name)

    for _ in range(2):
        click.echo()
    click.secho("q - quit", fg="red")
    click.echo()


def chosse_option(option: str, converters: List[Converter]):
    if option == "q":
        exit()

    for converter in converters:
        if converter.abbr == option:
            click.clear()
            click.pause(
                click.style(f"Option selected: {converter.base_name}", fg="green")
            )
            click.clear()
            return "main"

    click.pause(click.style("Invalid option", bold=True, fg="red"))
    click.clear()
    return "main"
