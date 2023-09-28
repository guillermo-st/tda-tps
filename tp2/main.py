from sys import argv


def parse_input(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        E, S = [], []
        for i in range(n):
            E.append(int(lines[i + 1]))
        for i in range(n):
            S.append(int(lines[i + n + 1]))
    return n, E, S


def earning(G, E, S, i, d):
    if i == 0:
        return min(E[0], S[0]), d

    if i == 1:
        no_break_earning = G[i - 1] + min(E[i], S[i - d])
        break_earning = 0 + min(E[i], S[0])
        break_before_earning = 0
    elif i == 2:
        break_before_earning = 0 + min(E[i - 1], S[0]) + min(E[i], S[1])
        no_break_earning = G[i - 1] + min(E[i], S[i - d])
        break_earning = G[i - 2] + min(E[i], S[0])
    else:
        break_before_earning = G[i - 3] + min(E[i - 1], S[0]) + min(E[i], S[1])
        no_break_earning = G[i - 1] + min(E[i], S[i - d])
        break_earning = G[i - 2] + min(E[i], S[0])

    if break_before_earning >= break_earning and break_before_earning >= no_break_earning:
        return break_before_earning, i - 1

    if break_earning >= no_break_earning:
        return break_earning, i
    return no_break_earning, d


def main():
    if len(argv) != 2:
        print("Usage: python main.py <input_file>")
        exit(1)
    file_name = argv[1]

    n, E, S = parse_input(file_name)
    G = []
    d = 0

    for i in range(n):
        earn, d = earning(G, E, S, i, d)
        G.append(earn)

    print(G)
    print(G[n - 1])


if __name__ == '__main__':
    main()
