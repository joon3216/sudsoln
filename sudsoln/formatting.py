
import questions

def formatting(sudoku_str):
    n = int(len(sudoku_str) ** .25)
    the_range = range(0, n ** 4 + 1, n ** 2)
    item = ''
    result = "'"
    sudoku_lst = list(sudoku_str)
    for c in enumerate(sudoku_lst):
        item += c[1]
        if c[0] != 0 and c[0] + 1 in the_range:
            if c[0] != n ** 4 - 1:
                result += item + "' +\\\n'"
            else:
                result += item + "'"
            item = ''
    print(result)

# if __name__ == '__main__':
#     formatting(questions.a_sta410_6)
