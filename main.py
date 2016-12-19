import argparse
from src.utils import *

#parser = argparse.ArgumentParser(prog='boolean-calc', description='Construction of logical tables')
#parser.add_argument('expression', nargs=1, type=str, help='boolean expression')
#
#args = parser.parse_args()
#print(args.expression)

format(parse_expression('( A > B ) = C'))
