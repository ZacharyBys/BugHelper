import click

from search import searchError

@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='world', required=False)
def main(name, as_cowboy):
    """Searches for command line errors and gives you the best answer from github"""
    greet = 'Howdy' if as_cowboy else 'Hello'
    click.echo(searchError())