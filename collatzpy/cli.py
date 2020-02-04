"""Console script for collatzpy."""
import sys
import os
import click

from collatzpy.helpers import save_to_json
from collatzpy.tree import CollatzTree as CTree


# @click.command()
@click.group()
def main():
    """Console script for collatzpy."""
    # click.echo("Replace this message by putting your code into "
    #            "collatzpy.cli.main")
    # click.echo("See click documentation at https://click.palletsprojects.com/")
    # return 0


@click.option('-s', '--save', help="Save to file?")
@click.option('-p', '--printer', is_flag=True, help="Print the path?")
@click.argument('n', type=int)
@main.command()
def path(n: int, printer: bool, save: str):
    """Generate sequence from n -> 1"""

    path = CTree.qpath(n)

    if printer:
        print(path)

    if save:
        if save.endswith('.txt'):
            file = open(f'{save}', 'w+')
            for n in path:
                file.write(f'{n}\n')
            file.close()
        elif save.endswith('.json'):
            save_to_json(os.getcwd(), save, {str(n): path})
        else:
            print(
                'Failed to save file. \n',
                'Accepted extensions are "txt" and "json".')


@click.option('-s', '--save', help="Save to file?")
@click.option('-p', '--printer', is_flag=True, help="Print the path?")
@click.argument('n', nargs=-1, type=int)
@main.command()
def paths(n: int, printer: bool, save: str):
    "For each n, generate the sequence from n -> 1"

    tree = CTree()
    tree.collect_from_list(n)
    
    if printer:
        for k in n:
            print(tree.path(k))

    if save:
        try:
            assert save.endswith('.txt') or save.endswith('.json')
        except AssertionError:
            print(
                'Failed to save file. \n',
                'Accepted extensions are "txt" and "json".')

        paths = {}
        for k in n:
            paths[k] = tree.path(k)

        if save.endswith('.txt'):
            file = open(f'{save}', 'w+')
            for _, path in paths.items():
                file.write(', '.join(map(str, path)) + '\n')
            file.close()
        elif save.endswith('.json'):
            save_to_json(os.getcwd(), save, paths)




if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

