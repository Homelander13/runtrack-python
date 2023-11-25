def draw_diagonal_carpet(size):
    for i in range(size + 1):
        line = "|"
        for j in range(size + 1):
            if i == j:
                line += "   #"
            else:
                line += " #"
        line += "   |"
        print(line, i + 1)


draw_diagonal_carpet(10)

