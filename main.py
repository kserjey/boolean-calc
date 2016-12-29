import argparse
from src.utils import *

parser = argparse.ArgumentParser(prog='boolean-calc', description='Calculator that build logical table from boolean expression')
parser.add_argument('expression', nargs='+', help='boolean expression')
args = parser.parse_args()

print("Expression:", expression)

format(parse_expression(expression))
