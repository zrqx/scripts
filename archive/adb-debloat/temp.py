import click
@click.command()
# @click.option('--name', prompt="Enter your name in case you haven't passed it with command",default="ajith",help='The help message')
@click.option('--day',type=click.Choice(['sun','mon','fri']),prompt="Enter the day")
def main(day):
    print(day)
main()