import math, string
from .core import *


def convert_to_postfix(expression):
    """
    Convert infix expression to postfix style. Return list of symbols in postfix notation.
    """
    infix = list(expression.replace(" ", ""))
    opr_priority = {'!': 4, '*': 3, '+': 2, '>': 1, '=': 1, '(': 0}
    postfix = []
    stack = []

    for token in infix:
        if token in string.ascii_uppercase:
            postfix.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            stack_token = stack.pop()
            while stack_token != '(':
                postfix.append(stack_token)
                stack_token = stack.pop()
        else:
            while stack and (opr_priority[stack[len(stack)-1]] >= opr_priority[token]):
                postfix.append(stack.pop())
            stack.append(token)

    while stack:
        postfix.append(stack.pop())

    return postfix


def count_arguments(expression):
    """
    Count number of arguments in expression. Return number of arguments.
    """
    stack = []

    for token in expression:
        if (not token in stack) and (token in string.ascii_uppercase):
            stack.append(token)

    return len(stack)


def parse_expression(str_expression):
    """
    Parse expression and create table with postfix notation for each row in logic table.
    Return logic table with arguments and results
    """
    expression = convert_to_postfix(str_expression)
    var_count = count_arguments(str_expression)
    table = init_table(var_count)
    parsed_table = [[] for i in range(len(table))]

    for token in expression:
        for i, row in enumerate(table):
            if token in string.ascii_uppercase:
                parsed_table[i].append(row[ord(token) - 65])
            else:
                parsed_table[i].append(token)


    for i, row in enumerate(parsed_table):
        table[i].append(solve(row))

    return table


def init_table(var_count):
    """
    Create table in file and return stream
    """
    rows_count = int(math.pow(2, var_count))
    table = open('table', 'w+')

    for i in range(rows_count):
        for k in range(var_count):
            tmp = rows_count // math.pow(2, (k + 1))
            table.write(str(int(i // tmp % 2)))
        table.write('\n')

    table.seek(0)

    return table


def format(table):
    """
    Print fromatted table
    """
    var_count = len(table[0]) - 1
    header = list(string.ascii_uppercase[:var_count])
    header.append('Result')
    table.insert(0, header)

    col_width = [max(len(str(x)) for x in col) for col in zip(*table)]
    for line in table:
        print("| " + " | ".join("{:{}}".format(str(x), col_width[i]) for i, x in enumerate(line)) + " |")
