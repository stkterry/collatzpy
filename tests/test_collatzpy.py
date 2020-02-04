#!/usr/bin/env python

"""Tests for `collatzpy` package."""


import unittest
import os
import json
import shutil
from mock import patch
from tempfile import NamedTemporaryFile, TemporaryDirectory, mkdtemp
from click.testing import CliRunner

import matplotlib.pyplot as plt
from collatzpy import tree as ctree
from collatzpy import plot as cplot
from collatzpy import fpaths
from collatzpy import cli


class TestCollatzpyTree(unittest.TestCase):
    """Tests for `collatzpy` package."""

    tree = ctree.CollatzTree()
    TEMP_FILE_LOC = NamedTemporaryFile().name

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

    def test_005_tree_collect_from_range(self):
        print('Expect tree to collect from range of nodes')
        self.tree.collect_from_range(0, 19)

        right = True
        for n in range(2, 20):
            if not self.tree[n].n == n or not self.tree[n].is_terminal:
                right = False
                break

        self.assertTrue(right)

    def test_006_tree_collect_from_list(self):
        print('Expect tree to collect from list of nodes')
        nlist = [20, 21, 22, 23, 24, 25, 26]
        self.tree.collect_from_list(nlist)

        for n in nlist:
            self.assertTrue(
                self.tree[n].n == n and self.tree[n].is_terminal)

    def test_007_tree_path(self):
        print('Does tree path return the right path?')
        self.assertListEqual(
            self.tree.path(5),
            [5, 16, 8, 4, 2, 1])

    def test_008_tree_filter(self):
        print('Does the tree filter... filter?')
        for _, node in self.tree.filter(lambda j: j[0] % 2):
            self.assertTrue(node.n % 2)

    def test_009_tree_size(self):
        print('Is the tree the right size?')
        self.assertIs(self.tree.size(), 153)

    def test_010_tree_terminals(self):
        print('Does terminals return all the terminals?')
        terminals = self.tree.terminals()

        self.assertIs(len(terminals), 28)
        for n in terminals:
            self.assertTrue(self.tree[n].is_terminal)

    def test_011_tree_save(self):
        print('Does the save_tree/load_tree func save/load a tree?')

        ctree.save_tree(self.tree, '', self.TEMP_FILE_LOC)
        self.assertTrue(os.path.exists(self.TEMP_FILE_LOC))

    def test_012_tree_load(self):
        print('Does the load_tree func load a tree?')

        tree_copy = ctree.load_tree('', self.TEMP_FILE_LOC)
        self.assertEqual(self.tree, tree_copy)


class TestCLI(unittest.TestCase):

    def test_CLI(self):
        """Test the CLI."""
        print('Does the CLI work?')
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'CollatzPy CLI' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

        path_result = runner.invoke(cli.path, '3')
        assert path_result.exit_code == 0
        assert '[3, 10, 5, 16, 8, 4, 2, 1]' in path_result.output

        path_result = runner.invoke(cli.path, '3 4 -r')
        assert path_result.exit_code == 0
        assert '[3, 10, 5, 16, 8, 4, 2, 1]\n[4, 2, 1]' in path_result.output


class TestFpaths(unittest.TestCase):
    """Tests for `collatzpy.fpaths`."""

    TEMP_DIR = TemporaryDirectory()
    SESSION_DIR = TemporaryDirectory()

    @patch('collatzpy.cfpaths._SESSION_DIR', SESSION_DIR.name)
    def test_000_fpaths(self):
        print('Does fpaths create the appropriate paths/variables?')

        paths = fpaths(dir=self.TEMP_DIR.name)

        self.assertEqual(paths['root'], self.TEMP_DIR.name)
        self.assertEqual(paths['imgs'], f'{self.TEMP_DIR.name}/images')
        self.assertEqual(paths['pickles'], f'{self.TEMP_DIR.name}/pickles')
        self.assertEqual(paths['dots'], f'{self.TEMP_DIR.name}/dots')

        new_paths = fpaths(reset=True)

        if os.path.exists(f'{self.SESSION_DIR.name}/session.json'):
            with open(f'{self.SESSION_DIR.name}/session.json') as f:
                dat = json.load(f) or {}

        self.assertDictEqual(new_paths, dat['paths'])


@patch("matplotlib.pyplot.show")
class TestPlot(unittest.TestCase):
    """Tests for `collatzpy.plot`."""

    TEMP_DIR = TemporaryDirectory()
    selection = [x for x in range(1, 100)]
    tree = ctree.CollatzTree()
    tree.collect_from_list(selection)
    cwd = os.getcwd()

    # @contextmanager
    # def tempwd(self):
    #     temp_dir = mkdtemp()
    #     oldpwd = os.getcwd()
    #     os.chdir(temp_dir)
    #     try:
    #         yield
    #     finally:
    #         os.chdir(oldpwd)
    #         shutil.rmtree(temp_dir)
    #         plt.close('all')

    # def run(self, res=None):
    #     with self.tempwd() as temp_wd:
    #         self.temp_wd = temp_wd
    #         super(TestPlot, self).run(res)

    def setUp(self):
        self.temp_dir = mkdtemp()
        os.chdir(self.temp_dir)

    def tearDown(self):
        os.chdir(self.cwd)
        shutil.rmtree(self.temp_dir)
        plt.close('all')

    def test_000_plot_scatter_heat(self, mock_show):
        print("Can we plot with scatter_heat?")

        cplot.scatter_heat(self.tree, self.selection)
        assert mock_show.called

        cplot.scatter_heat(self.tree, save=True)
        self.assertRegex(
            os.listdir()[0],
            r'(\d{4})-(\d{2})-(\d{2})_(\d{2}):(\d{2}):(\d{2})\.png')

        cplot.scatter_heat(
            self.tree, output_name='scatter_heat.png')

        assert os.path.isfile('scatter_heat.png')

    def test_001_plot_scatter_tsts(self, mock_show):
        print("Can we plot with scatter_tst?")

        cplot.scatter_tst(self.tree, self.selection)
        assert mock_show.called

        cplot.scatter_tst(self.tree, save=True)
        self.assertRegex(
            os.listdir()[0],
            r'(\d{4})-(\d{2})-(\d{2})_(\d{2}):(\d{2}):(\d{2})\.png')

        cplot.scatter_tst(
            self.tree, output_name='scatter_tst.png')

        assert os.path.isfile('scatter_tst.png')

    def test_002_plot_hexbin(self, mock_show):
        print("Can we plot with scatter_hexbin?")

        cplot.hexbin(self.tree, self.selection, gridsize=55)
        assert mock_show.called

        cplot.hexbin(self.tree, save=True)
        self.assertRegex(
            os.listdir()[0],
            r'(\d{4})-(\d{2})-(\d{2})_(\d{2}):(\d{2}):(\d{2})\.png')

        cplot.hexbin(
            self.tree, output_name='hexbin.png')

        assert os.path.isfile('hexbin.png')

    def test_003_plot_path(self, mock_show):
        print("Can we plot with path?")

        cplot.path(self.tree, 27)
        assert mock_show.called

        cplot.path(self.tree, 31, save=True)
        self.assertRegex(
            os.listdir()[0],
            r'(\d{4})-(\d{2})-(\d{2})_(\d{2}):(\d{2}):(\d{2})\.png')

        cplot.path(
            self.tree, 97, output_name='path.png')

        assert os.path.isfile('path.png')

    def test_003_plot_paths(self, mock_show):
        print("Can we plot with paths?")
        paths = [27, 97, 87, 31]
        cplot.paths(self.tree, paths)
        assert mock_show.called

        cplot.paths(self.tree, paths, save=True)
        self.assertRegex(
            os.listdir()[0],
            r'(\d{4})-(\d{2})-(\d{2})_(\d{2}):(\d{2}):(\d{2})\.png')

        cplot.paths(
            self.tree, paths, output_name='path.png')

        assert os.path.isfile('path.png')

    def test_004_plot_histogram(self, mock_show):
        print("Can we plot with paths?")

        cplot.hist(self.tree, self.selection)
        assert mock_show.called

        cplot.hist(self.tree, save=True)
        self.assertRegex(
            os.listdir()[0],
            r'(\d{4})-(\d{2})-(\d{2})_(\d{2}):(\d{2}):(\d{2})\.png')

        cplot.hist(
            self.tree, output_name='histogram.png')

        assert os.path.isfile('histogram.png')

    def test_005_plot_angle_path(self, mock_show):
        print("Can we plot with paths?")

        path_args = {'alpha': 1.1, 'beta': .386, 'gamma': 1,
                     'sigma': 1.3, 'cmName': 'gnuplot2',
                     'cmR': (0, 1), 'pointed': True}
        fig_args = {'pxw': 1600, 'pxh': 900, 'dpi': 96,
                    'facecolor': 'gray'}

        cplot.angle_path(self.tree, self.selection, **path_args, **fig_args)
        assert mock_show.called

        cplot.angle_path(self.tree, save=True)
        self.assertRegex(
            os.listdir()[0],
            r'(\d{4})-(\d{2})-(\d{2})_(\d{2}):(\d{2}):(\d{2})\.png')

        cplot.angle_path(
            self.tree, output_name='angle_path.png')

        assert os.path.isfile('angle_path.png')


class TestPlotNode(unittest.TestCase):
    TEMP_DIR = TemporaryDirectory()
    selection = [x for x in range(1, 100)]
    tree = ctree.CollatzTree()
    tree.collect_from_list(selection)
    cwd = os.getcwd()

    def setUp(self):
        self.temp_dir = mkdtemp()
        os.chdir(self.temp_dir)

    def tearDown(self):
        os.chdir(self.cwd)
        shutil.rmtree(self.temp_dir)

    def test_000_node_node_graph(self):
        print("Can we generate a node graph?")

        cplot.node_graph(self.tree, self.selection, save=True, write_dot=True)

        dirfiles = os.listdir()
        png = dirfiles.pop() if dirfiles[1][-4:] == '.png' else dirfiles[0]
        dot = dirfiles.pop()
        self.assertRegex(
            dot,
            r'(\d{4})-(\d{2})-(\d{2})_(\d{2}):(\d{2}):(\d{2})\.dot')
        self.assertRegex(
            png,
            r'(\d{4})-(\d{2})-(\d{2})_(\d{2}):(\d{2}):(\d{2})\.png')

        cplot.node_graph(self.tree, img_name="graph.png", dot_name="graph.dot")

        assert os.path.isfile('graph.png')
        assert os.path.isfile('graph.dot')
