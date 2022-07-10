matrix = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]

for r, row in enumerate(matrix):
    for c, letter in enumerate(row):
        print(r, c, letter)

for row, r in enumerate(matrix):
    print(r, row)
