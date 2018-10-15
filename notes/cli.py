# -*- coding: utf-8 -*-
"""Console script for notes."""
import click

from . import notes

@click.command()
def main(args=None):
    """Console script for notes."""
    click.echo("Replace this message by putting your code into "
               "notes.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    main()