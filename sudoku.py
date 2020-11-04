"""
-------------------------------------------------------
sudoku.py
9x9 Sudoku Puzzle implementation as described in class
-------------------------------------------------------
CP468
Assignment 2
Authors:  Keven Iskander, Carla Castaneda, Nicole Laslavic, Alexander Francis
__updated__ = "2020-11-02"
-------------------------------------------------------
"""

# Some Sudoku puzzle examples taken from here:
# https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html

class Sudoku:

    def __init__(self):
        f = open('sudoku1.txt', 'r')
        lines = f.readlines()
        if len(lines)!=9:
            print('ERROR: Invalid puzzle file')
            self.table = [[0 for i in range(9)] for j in range(9)]
        else:
            self.table = [[0 for i in range(9)] for j in range(9)]
            for i in range(len(lines)):
                for j in range(len(self.table)):
                    self.table[i][j] = int(lines[i][j])

        f.close()

    def __eq__(self, sudoku2):
        if self.table == sudoku2.table:
            return True
        return False


    # Code taken from https://stackoverflow.com/questions/37952851/formating-sudoku-grids-python-3
    def print_table(self):
        print("-"*37)
        
        for i, row in enumerate(self.table):
            print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
            if i == 8:
                print("-"*37)
            elif i % 3 == 2:
                print("|" + "---+"*8 + "---|")
            else:
                print("|" + "   +"*8 + "   |")

    # https://www.educative.io/edpresso/how-to-check-if-a-sudoku-board-is-valid

    def is_valid_row(self, i):
        
        temp =  self.table[i]
        temp = list(filter(lambda a: a != 0, temp))

        if len(temp) == len(list(set(temp))):
            return True
        else:
            return False

    def is_valid_col(self, j):

        temp = [row[j] for row in self.table]
        temp = list(filter(lambda a: a != 0, temp))

        if len(temp) == len(list(set(temp))):
            return True
        else:
            return False

    def is_valid(self):
        # seen = set()
        for i in range(len(self.table)):
            if self.is_valid_row(i) == False or self.is_valid_col(i) == False:
                print('test3')
                return False

        return True


def main():
    sud = Sudoku()
    sud.print_table()
    print(sud.is_valid())

if __name__ == "__main__":
    main()