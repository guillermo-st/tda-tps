import sys
import pulp
from common import parse_file


def aproximated_hitting_set(A, B):
    prob = pulp.LpProblem("HittingSetProblem_Relaxed", pulp.LpMinimize)
    x = pulp.LpVariable.dicts("x", A, 0, 1)
    for b in B:
        prob += sum(x[a] for a in b if a in A) >= 1
    prob += sum(x[a] for a in A)
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    b = max(len(b) for b in B)
    return set(a for a in A if x[a].value() >= 1/b)


def main():
    argv = sys.argv
    if len(argv) != 2:
        print('Usage: python3 lineal.py <filename>')
        return

    filename = argv[1]

    A, B = parse_file(filename)
    C = aproximated_hitting_set(A, B)
    print(C)


if __name__ == '__main__':
    main()
