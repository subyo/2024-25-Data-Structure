def solve(matrix):
    pass  # solve fonksiyonunu buraya eklemelisiniz

def solve_and_print(matrix):
    print("Begin Solving")

    matrix = solve(matrix)

    if matrix is None:
        print("No Solution Found!!!")
    else:
        print("Solution Found:")
        for row in matrix:
            print(row)

# Sudoku çözümü için gerekli diğer fonksiyonları buraya ekleyebilirsiniz

# Fonksiyonu çağırmak için:
# solve_and_print(matrix)
# Örnek Sudoku bulmacası
example_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Fonksiyonu çağırarak çözümü bulmak ve yazdırmak
solve_and_print(example_board)
