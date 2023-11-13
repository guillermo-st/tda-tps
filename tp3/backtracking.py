import sys
from common import parse_file, is_feasible

def _hitting_set_rec(A, B, k, C, i):
    if len(C) > k:
        return None
    if is_feasible(B, C):
        return C
    if i >= len(A):
        return None
    C.add(A[i])
    res = _hitting_set_rec(A, B, k, C, i+1)
    if res:
        return res
    C.remove(A[i])
    return _hitting_set_rec(A, B, k, C, i+1)


def hitting_set(A, B, k):
    C = set()
    return _hitting_set_rec(A, B, k, C, 0)


def main():
    argv = sys.argv
    if len(argv) != 3:
        print('Usage: python3 backtracking.py <filename> <k>')
        return

    filename = argv[1]
    k = int(argv[2])

    try:
        A, B = parse_file(filename)
        C = hitting_set(A, B, k)
        print(C)
    except:
        print('Error: check your input file')
        return


if __name__ == '__main__':
    main()
