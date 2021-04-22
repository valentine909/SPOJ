# don't pass the submit tests (wrong answer)
rows = [i for i in range(1, 1235)]
columns = [i for i in range(1, 5679)]


def row_swap(x, y):
    rows[x - 1], rows[y - 1] = rows[y - 1], rows[x - 1]


def column_swap(x, y):
    columns[x - 1], columns[y - 1] = columns[y - 1], columns[x - 1]


def get_value(x, y):
    print((rows[x - 1] - 1) * 5678 + (columns[y - 1]))


def get_index(z):
    if z % 5678:
        x = z // 5678 + 1
    else:
        x = z // 5678
    y = z % 5678
    print(rows[x - 1], columns[y - 1])


def main():
    import sys
    for line in sys.stdin.readlines():
        try:
            command = [line.strip().split()[0]] + [int(_) for _ in line.strip().split()[1:]]
        except IndexError:
            return
        if command[0] == "R":
            row_swap(command[1], command[2])
            # print(rows)
            # print(columns)
        elif command[0] == "C":
            column_swap(command[1], command[2])
            # print(rows)
            # print(columns)
        elif command[0] == "Q":
            get_value(command[1], command[2])
        elif command[0] == "W":
            get_index(command[1])
        else:
            return


main()
