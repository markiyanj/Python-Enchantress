import click


@click.command('hello')
def hello():
    val = click.prompt('say hello', type=str, default="hello")
    print(val)


@click.command('boom')
def boom():
    if click.confirm('do you wanna boom your database?'):
        click.echo('Whell done! Your database just gone!')


@click.command()
@click.confirmation_option(prompt='Are you sure you want to drop the db?')
def dropdb():
    click.echo('Dropped all tables!')


if __name__ == '__main__':
    dropdb()
