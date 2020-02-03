#!/usr/bin/env python

"""Tests for `collatzpy` package."""


import unittest
import os
from tempfile import NamedTemporaryFile, TemporaryDirectory
from click.testing import CliRunner

# from collatzpy import collatzpy
from collatzpy import tree as ctree
from collatzpy import fpaths
from collatzpy import cli

_TEMP_DILL = NamedTemporaryFile()
_TEMP_DIR = TemporaryDirectory()



class TestCollatzpy(unittest.TestCase):
    """Tests for `collatzpy` package."""

    tree = ctree.CollatzTree()

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""
        

    def test_000a_node(self):
        print('Check the node properties')
        node1 = ctree.CollatzNode(3)
        node2 = ctree.CollatzNode(10)

        node1.next = node2
        self.assertIs(node1.n, 3)
        self.assertIs(node1.next, node2)
        self.assertFalse(node1.is_terminal)

    def test_000b_calc_next(self):
        print('Does the basic calc_next function work?')
        self.assertIs(self.tree.calc_next(5), 16)
        self.assertIs(self.tree.calc_next(16), 8)

    def test_001_tree_collect(self):
        print('Expect tree to contain new values')

        self.tree.collect(27)
        node27 = self.tree[27]
        self.assertIsInstance(node27, ctree.CollatzNode)
        self.assertIs(node27.n, 27)
        self.assertIs(node27.next, self.tree[82])
        self.assertIs(node27.seq_len, 111)
        self.assertTrue(node27.is_terminal)

    def test_002_tree_has(self):
        print('Checks whether the tree has a node')
        self.assertTrue(self.tree.has(27))
        self.assertFalse(self.tree.has(26))

    def test_003_tree_splay(self):
        print('Does splay return the right dict info?')
        self.assertDictEqual(
            self.tree.splay(82),
            {'n': 82, 'seq_len': 110,
             'next': 41, 'is_terminal': False})

        self.assertIs(self.tree.splay(11), None)

    def test_004_tree_best(self):
        print('Does best return the right dict info?')
        self.tree.collect(97)
        self.assertDictEqual(
            self.tree.best(),
            {'n': 97, 'seq_len': 118,
             'next': 292, 'is_terminal': True})

    def test_004_tree_collect_from_range(self):
        print('Expect tree to collect from range of nodes')
        self.tree.collect_from_range(0, 19)

        right = True
        for n in range(2, 20):
            if not self.tree[n].n == n or not self.tree[n].is_terminal:
                right = False
                break

        self.assertTrue(right)

    def test_005_tree_collect_from_list(self):
        print('Expect tree to collect from list of nodes')
        nlist = [28, 29, 30, 31, 32]
        self.tree.collect_from_list(nlist)

        for n in nlist:
            self.assertTrue(
                self.tree[n].n == n and self.tree[n].is_terminal)

    def test_006_tree_path(self):
        print('Does tree path return the right path?')
        self.assertListEqual(
            self.tree.path(5),
            [5, 16, 8, 4, 2, 1])

    def test_007_tree_filter(self):
        print('Does the tree filter... filter?')
        for _, node in self.tree.filter(lambda j: j[0] % 2):
            self.assertTrue(node.n % 2)

    def test_008_tree_size(self):
        print('Is the tree the right size?')
        self.assertIs(self.tree.size(), 148)

    def test_009_tree_terminals(self):
        print('Does terminals return all the terminals?')
        terminals = self.tree.terminals()

        self.assertIs(len(terminals), 26)
        for n in terminals:
            self.assertTrue(self.tree[n].is_terminal)
  
    def test_010_tree_save(self):
        print('Does the save_tree/load_tree func save/load a tree?')

        ctree.save_tree(self.tree, '', _TEMP_DILL.name)
        self.assertTrue(os.path.exists(_TEMP_DILL.name))

    def test_011_tree_load(self):
        print('Does the load_tree func load a tree?')

        tree_copy = ctree.load_tree('', _TEMP_DILL.name)
        self.assertEqual(self.tree, tree_copy)

    def test_012_fpaths(self):
        print('Does fpaths create the appropriate paths/variables?')

        paths = fpaths(dir=_TEMP_DIR.name)

        self.assertEqual(paths['root'], _TEMP_DIR.name)
        self.assertEqual(paths['imgs'], f'{_TEMP_DIR.name}/images')
        self.assertEqual(paths['pickles'], f'{_TEMP_DIR.name}/pickles')
        self.assertEqual(paths['dots'], f'{_TEMP_DIR.name}/dots')




    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'collatzpy.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
