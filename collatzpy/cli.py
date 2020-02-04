"""Console script for collatzpy."""
import sys
import os
import click
from collatzpy.helpers import save_to_json
from collatzpy.tree import CollatzTree as CTree


# @click.command()
@click.group()
def main():
    """CollatzPy CLI"""
    return 0


@click.option(
    '-s', '--save',
    help="Save data to the given filename.Accepts txt and json ext.")
@click.option(
    '-p/-np', '--display', is_flag=True,
    default=True, help="Print the results?")
@click.option(
    '-r', '--rng', is_flag=True,
    help="If n is given as a range, returns all paths in that range.")
@click.argument('n', nargs=-1, type=int)
@main.command()
def path(n: int, rng: bool, display: bool, save: str):
    "For each n, generate the sequence from n -> 1"

    if rng and len(n) == 2:
        n = [x for x in range(n[0], n[1] + 1)]

    tree = CTree()
    tree.collect_from_list(n)

    if display:
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
