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


def hitting_set(A, B):
    low, high = 0, len(A)
    C = None
    while low < high:
        mid = (low + high) // 2
        res = _hitting_set_rec(A, B, mid, set(), 0)
        if res:
            if not C:
                C = res.copy()
            elif len(res) < len(C):
                C = res.copy()
            high = mid
        else:
            low = mid + 1
    return C


def main():
    argv = sys.argv
    if len(argv) != 2:
        print('Usage: python3 backtracking.py <filename>')
        return

    filename = argv[1]

    try:
        A, B = parse_file(filename)
        C = hitting_set(A, B)
        print(C)
    except:
        print('Error: check your input file')
        return


if __name__ == '__main__':
    main()