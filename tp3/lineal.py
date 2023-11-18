import sys
import pulp
from common import parse_file


def lineal_hitting_set(A, B):
    prob = pulp.LpProblem('Hitting_Set', pulp.LpMinimize)
    x = pulp.LpVariable.dicts('x', A, cat=pulp.LpBinary)
    prob += pulp.lpSum([x[a] for a in A])
    for b in B:
        prob += pulp.lpSum([x[a] for a in b]) >= 1
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    return set(a for a in A if x[a].value() == 1)


def main():
    argv = sys.argv
    if len(argv) != 2:
        print('Usage: python3 lineal.py <filename>')
        return

    filename = argv[1]

    A, B = parse_file(filename)
    C = lineal_hitting_set(A, B)
    print(C)


if __name__ == '__main__':
    main()
