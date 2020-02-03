"""Top-level package for collatzpy."""

__author__ = """Steven K Terry"""
__email__ = 'stkterry@gmail.com'
__version__ = '0.1.0'


from . import tree
from . import plot
from . import cfpaths

fpaths = cfpaths.fpaths

__all__ = ['fpaths', 'cfpaths', 'tree', 'plot']
