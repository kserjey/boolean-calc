import unittest
from src.core import perform


class TestPerform(unittest.TestCase):
    def test_inverse(self):
        self.assertEqual(perform('!', False), True, '!False should be True')
        self.assertEqual(perform('!', True), False, '!True should be False')


    def test_and(self):
        self.assertEqual(perform('*', False, False), False, 'False * False should be False')
        self.assertEqual(perform('*', False, True), False, 'False * True should be False')
        self.assertEqual(perform('*', True, False), False, 'True * False should be False')
        self.assertEqual(perform('*', True, True), True, 'True * True should be True')


    def test_or(self):
        self.assertEqual(perform('+', False, False), False, 'False + False should be False')
        self.assertEqual(perform('+', False, True), True, 'False + True should be False')
        self.assertEqual(perform('+', True, False), True, 'True + False should be False')
        self.assertEqual(perform('+', True, True), True, 'True + True should be False')


    def test_implic(self):
        self.assertEqual(perform('>', False, False), True, 'False > False should be True')
        self.assertEqual(perform('>', False, True), True, 'False > True should be True')
        self.assertEqual(perform('>', True, False), False, 'True, > False should be False')
        self.assertEqual(perform('>', True, True), True, 'True > True should be True')

    def test_equal(self):
        self.assertEqual(perform('=', False, False), True, 'False = False should be True')
        self.assertEqual(perform('=', False, True), False, 'False = True should be False')
        self.assertEqual(perform('=', True, False), False, 'True = False should be False')
        self.assertEqual(perform('=', True, True), True, 'True = True should be True')
