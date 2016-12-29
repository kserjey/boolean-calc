import unittest
from src.utils import *


class TestConvertationToPostfix(unittest.TestCase):
    def test_simple_convert(self):
        self.assertEqual(convert_to_postfix('A + B'), ['A', 'B', '+'], 'Should convert to postfix notation')
        self.assertEqual(convert_to_postfix('A+B+C'), ['A', 'B', '+', 'C', '+'], 'Should convert to postfix notation')


    def test_brackets(self):
        self.assertEqual(convert_to_postfix('( A + B ) * C'), ['A', 'B', '+', 'C', '*'], 'Brackets should be considered')
        self.assertEqual(convert_to_postfix('(A*B+(A+B))*C'), ['A', 'B', '*', 'A', 'B', '+', '+', 'C', '*'], 'Brackets should be considered')


    def test_opreration_priority(self):
        self.assertEqual(convert_to_postfix('A + B * C'), ['A', 'B', 'C', '*', '+'], 'Operator priority should be considered')
        self.assertEqual(convert_to_postfix('A>B=C+A*B'), ['A', 'B', '>', 'C', 'A', 'B', '*', '+', '='], 'Operator priority should be considered')


class TestInitTable(unittest.TestCase):
    def test_init_table(self):
        self.assertEqual(init_table(2), [[False, False], [False, True], [True, False], [True, True]], 'Should initialize logic table')


class TestCountArguments(unittest.TestCase):
    def test_not_repeated_arguments(self):
        self.assertEqual(count_arguments('A'), 1, 'Should count non repeated arguments')
        self.assertEqual(count_arguments('A + B'), 2, 'Should count non repeated arguments')
        self.assertEqual(count_arguments('A + B * C > D'), 4, 'Should count non repeated arguments')


    def test_repeated_arguments(self):
        self.assertEqual(count_arguments('A + A'), 1, 'Should count repeated arguments')
        self.assertEqual(count_arguments('D + D + D + D'), 1, 'Should count repeated arguments')
        self.assertEqual(count_arguments('A + A * B + C * A + A'), 3, 'Should count repeated arguments')


class TestParseConverstation(unittest.TestCase):
    def test_one_arument(self):
        self.assertEqual(parse_expression('A + A'), [[False, False], [True, True]])
        self.assertEqual(parse_expression('A + A * A'), [[False, False], [True, True]])


    def test_multiplie_arguments(self):
        self.assertEqual(parse_expression('A + B'), [[False, False, False], [False, True, True], [True, False, True], [True, True, True]])
        self.assertEqual(parse_expression('A + B * A'), [[False, False, False], [False, True, False], [True, False, True], [True, True, True]])
