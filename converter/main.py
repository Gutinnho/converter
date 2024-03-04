import click
from typing import List

from .converter import Converter, make_converters


def main():
    converters = make_converters()

    option = "main"

    click.clear()
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
        exiting()

    for converter in converters:
        if converter.abbr == option:
            valid_option(converter)
            ask_continue()
            return "main"

    invalid_option()
    return "main"


def valid_option(converter: Converter):
    click.clear()
    while True:
        try:
            click.clear()
            number = click.prompt(
                click.style(f"{converter.base_name}:", fg=converter.color),
                prompt_suffix=" ",
            )
            number_int = converter.validate(number)
            break
        except click.BadParameter as e:
            click.pause(click.style(e, fg="red"), err=True)

    result = converter.convert(number_int)

    click.clear()

    colors = ["red", "green", "blue", "magenta"]
    for index, (base_name, value) in enumerate(result.items()):
        click.secho(f"{base_name}: ", fg=colors[index], nl=False)
        click.secho(value)
    click.echo()

    click.pause("...")


def invalid_option():
    click.pause(click.style("Invalid Option", fg="red"), err=True)
    click.clear()


def exiting():
    click.clear()
    click.secho("Exiting!", bold=True, fg="white")
    exit()


def ask_continue():
    while True:
        click.clear()
        click.secho("Continue?", nl=True, bold=True, fg="white")

        option = click.getchar().lower()
        if option == "y":
            click.clear()
            break
        elif option == "n":
            exiting()
        else:
            click.echo()
            click.secho("Invalid option", bold=True, fg="red")
            click.pause(
                click.style("Please type 'y' or 'n'", fg="red"),
                err=True,
            )
