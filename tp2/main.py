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
# g_max(dia, cant_entrenamientos_consecutivos):
#   si cant_entrenamientos_consecutivos es 0:
#      g_max(dia - 1)
#   sino:
#      g_max(dia - 1, cant_entrenamientos_consecutivos - 1) + min(e[dia - 1], s[cant_entrenamientos_consecutivos - 1])
#
# g_max(dia)
#  max(g_max(dia - 1, 0), g_max(dia - 1, 1), ..., g_max(dia - 1, dia - 1))


def g_max(n, e, s):
    g = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for day in range(1, n + 1):
        for cons_trainings in range(day + 1):
            g[day][0] = max(g[day][0], g[day - 1][cons_trainings])
            if cons_trainings > 0:
                training_earning = min(e[day - 1], s[cons_trainings - 1])
                g[day][cons_trainings] = g[day - 1][cons_trainings - 1] + training_earning

    return max(g[n])


if __name__ == '__main__':
    if len(argv) != 2:
        print("Uso: python3 main.py <archivo>")
        exit(1)
    n, e, s = parse_input(argv[1])
    print("La ganancia máxima es:", g_max(n, e, s))

