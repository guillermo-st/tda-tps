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
