"""Top-level package for collatzpy."""

__author__ = """Steven K Terry"""
__email__ = 'stkterry@gmail.com'
__version__ = '0.1.0'

from .fpaths import fpaths
from . import tree
from . import plot

__all__ = ['fpaths', 'tree', 'plot']
