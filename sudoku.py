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

class Sudoku:

    def __init__(self):
        self.table = [[1 for i in range(9)] for j in range(9)]

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


def main():
    sud = Sudoku()
    sud.print_table()

if __name__ == "__main__":
    main()