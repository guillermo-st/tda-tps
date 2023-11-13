import sys


def parse_file(filename):
    A = []
    B = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            elems = line.split(',')
            B.append(set(elems))
            for elem in elems:
                if elem not in A:
                    A.append(elem)
    return A, B


def is_feasible(B, C):
    for b in B:
        if not b.intersection(C):
            return False
    return True

