# CP468_A2 - Artificial Intelligence Sudoku Solving Algorithm

Assignment written for CP468 Artifical Intelligence. sudoku.py includes functions to read sudoku puzzle inputs in .txt format, verify validity of columns, rows and subsquares and both backtracking and AC3 AI algorithms to solve. 

## Algorithm Implementation

### AC-3

To implement the AC-3 algorithm, every alldi constraint was organised into a tuple. The rst
element of the tuple contains the current node, and the second element contains the neighbour
constraint, which is any node in the same row, column, and sub-square. The binary constraints
(tuples) managed by a queue and removed to be processed in the revise function. The domain of
the rst node in the tuple will potentially have an item in it's domain removed if there is no value
in the domain of the second node that satises the constraint between the two. If the domain
was revised, all neighbours of that node will be inserted into the queue. This time the neighbour
node will be the rst item in the tuple so that the domain of the neighbour is revised according
to the current node. If at any point the domain of a node is empty, there is an inconsistency
within the Sudoku puzzle that cannot be solved using the AC-3 algorithm alone and the function
will return false.

### Backtracking

The backtracking algorithm works by iterating through the empty squares in the matrix and
inserting nodes from a list of possible values. While iterating through, if all possibles val-
ues are exhausted for a single square the algorithm will iterate backwards to the previously
looked at square to try another value. This function uses the helper functions `is valid()' and
`MRV heuristic()'. The is valid() function checks each node to make sure there are no repeat
values in the row, column and sub-squares. The MRV heuristic() function nds the next empty
square with the shortest length of possible values to increase eciency.

## Getting Started

For testing purposes, download all files from repo

### Prerequisites

Latest version of python installed


https://www.python.org/downloads/


### Installing

1) Pull all files to a folder

2) Run sudoku.py in cmd or using an interpreter (example: VS Code)

To run in cmd we first need to cd the project directory

```
cd C:\Users\...directory
```

Then we run the script:

```
python sudoku.py
```

Assuming the latest version of python is installed to your system.

The __init__ function specifies which sudoku.txt is being solved. A collection of unsolved sudoku files are included in the repository for testing purposes. To change the input file, make sure the file is in the same folder as the sudoku.py and utilities.py files, and edit line 43:

```
f = open('sudoku8.txt', 'r')
```

and replace sudoku8.txt with whichever file you choose (so long as it matches the format below.

## sudoku.txt file format

The puzzle that are provided to the AC3 and backtracking algorithms are prepared as text les
with the following constraints:
1. All puzzle values must be integers within the text le
2. No puzzle may exceed 81 digits
3. The le must have 9 digits per row, and 9 rows in total
4. Empty spaces are to be represented as 0.
An example of a valid Sudoku puzzle text le input:
```
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300
```

## Running the tests

Run sudoku.py for all testing

### What are you testing?


The following input and output examples demonstrate how our implementation of the AC3 and
backtracking algorithms work on a given puzzle. 

### Before

```
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300
```

### After

```
-------------------------------
| 4  8  3 | 9  2  1 | 6  5  7 |
| 9  6  7 | 3  4  5 | 8  2  1 |
| 2  5  1 | 8  7  6 | 4  9  3 |
-------------------------------
| 5  4  8 | 1  3  2 | 9  7  6 |
| 7  2  9 | 5  6  4 | 1  3  8 |
| 1  3  6 | 7  9  8 | 2  4  5 |
-------------------------------
| 3  7  2 | 6  8  9 | 5  1  4 |
| 8  1  4 | 2  5  3 | 7  6  9 |
| 6  9  5 | 4  1  7 | 3  8  2 |
-------------------------------

The AC-3 algorithm was able to solve the Sudoku Puzzle
Total Execution Time: 6.1266093254089355 sec
```



### Is the output accurate?
 
The console will output a complete sudoku puzzle that respect the following constraints:

1. No row may have any duplicate values
2. No column may have any duplicate values
3. No sub-square may contain any duplicate values. The 9x9 puzzle consists of nine 3x3 sub-
squares, also arranged in a 3x3 fashion. In the image above, each sub-square is separated
by hyphens and line breaks.

## Versioning

Version 1.0

## Authors

**Keven Iskander** 
**Carla Castaneda** 
**Alexander Francis** 
**Nicole Laslavic** 

