import click

@click.group()
def cli():
    """Personal Finance Management Application"""
    pass

@cli.command()
def start():
    """Start the application"""
    click.echo("Welcome to the Personal Finance Management Application!")

if __name__ == '__main__':
    cli()
