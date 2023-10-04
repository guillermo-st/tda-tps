from sys import argv


def parse_input(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        e, s = [], []
        for i in range(n):
            e.append(int(lines[i + 1]))
            s.append(int(lines[i + n + 1]))
    return n, e, s


# EC de recurrencia:
# OPT(i, j) = max(min(E[i], S[j]) + OPT(i + 1, j + 1), OPT(i + 1, 0))


def g_max(n, e, s):
    g = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    max_g = 0

    for day in range(1, n + 1):
        for energy_index in range(day + 1):
            g[day][0] = max(g[day][0], g[day - 1][energy_index])
            if energy_index > 0:
                training_earning = min(e[day - 1], s[energy_index - 1])
                g[day][energy_index] = g[day - 1][energy_index - 1] + training_earning

                if g[day][energy_index] > max_g:
                    max_g = g[day][energy_index]

    return g, max_g

def max_index(row):
    max = row[0]
    max_idx = 0
    for i in range(len(row)):
        if row[i] > max:
            max = row[i]
            max_idx = i
    
    return max_idx

def show_trained_days(g, n):
    i = n
    while i > 0:
        j = max_index(g[i])

        for t in range(j):
            print("Dia " + str(i) + ": Entrenamiento")
            i -= 1

        if i == 0:
            break 

        print("Dia " + str(i) + ": Descanso")
        i = i -1


if __name__ == '__main__':
    if len(argv) != 2:
        print("Uso: python3 main.py <archivo>")
        exit(1)
    n, e, s = parse_input(argv[1])
    g, max_g = g_max(n, e ,s)
    print("La ganancia máxima es:", max_g)
    show_trained_days(g, n)

