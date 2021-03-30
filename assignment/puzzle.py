# Hung Yiu Pan
# 1155108381
# 1155108381@link.cuhk.edu.hk
# CSCI1040 2020-2021 Term 2 Assignment

# Global Variables
flag = True
MIN_WORD = 3 # length of the shortest word to search
FACTORS = 4 # number of factors in the product

# abstract base class Puzzle
class Puzzle:
    def __init__(self, puzzle, RowCol):
        self.puzzle = puzzle
        self.Row, self.Col = RowCol[0], RowCol[1]
    def solve(self):
        self.print()
    def print(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                print(self.puzzle[i][j], end=" ")
            print()
        print()

# SubClass WordPuzzle
class WordPuzzle(Puzzle):
    def __init__(self, puzzle, RowCol, dict):
        super().__init__(puzzle, RowCol)
        self.dict = dict
    def toStringList(self, str):
        strlist = []
        for i in range(len(str)):
            for j in range(i+1, len(str)+1):
                if len(str[i:j]) >= MIN_WORD:
                    strlist.append(str[i:j])
        return strlist
    def solve(self):
        super().solve()
        print("Words found:")
        # horizontal
        for i in range(self.Row):
            for word in self.toStringList("".join(self.puzzle[i]).lower()):
                # check if the strings in Row contain the word in dictionary
                if word in self.dict:  
                    print("row " + str(i) + ": " + word)
                    index = "".join(self.puzzle[i]).lower().find(word)
                    # Change the word found into UPPER
                    for j in range(index, index + len(word)):
                        self.puzzle[i][j] = self.puzzle[i][j].upper()
        # vertical
        puzzle_t = list(map(list, zip(*self.puzzle))) # transpose
        for i in range(self.Col):
            for word in self.toStringList("".join(puzzle_t[i]).lower()):
                # check if the strings in Column contain the word in dictionary
                if word in self.dict:
                    print("col " + str(i) + ": " + word)
                    index = "".join(puzzle_t[i]).lower().find(word)
                    # Change the word found into UPPER
                    for j in range(index, index + len(word)):
                        self.puzzle[j][i] = self.puzzle[j][i].upper()
        # print solved version
        print("\nPuzzle solved:")
        self.print()

# SubClass MathPuzzle
class MathPuzzle(Puzzle):
    def solve(self):
        super().solve()
        max_num, max_RowCol = 0, []
        for i in range(self.Row - FACTORS + 1):
            for j in range(self.Col - FACTORS + 1):
                sum_h, sum_v, sum_d, sum_d_rev = 1,1,1,1
                for k in range(FACTORS):
                    sum_h *= int(self.puzzle[i][j + k]) # horizontal 
                    sum_v *= int(self.puzzle[i + k][j]) # vertical
                    sum_d *= int(self.puzzle[i + k][j + k]) # diagonal
                    if (j >= FACTORS - 1):
                        sum_d_rev *= int(self.puzzle[i + k][j - k]) # diagonal (reversed)
                # Check Max product of k values
                if (max(sum_h, sum_v, sum_d, sum_d_rev) > max_num):
                    max_num = max(sum_h, sum_v, sum_d, sum_d_rev)
                    max_RowCol = [i,j]
        # print solution tuple
        print("Puzzle solved:")
        print((max_num, max_RowCol[0], max_RowCol[1]), "\n")

# Function for loading Dictionary File
def insert_dict(filename):
    try:
        with open(filename, "r") as f_dict:
            info = f_dict.readline().split()
            dictionary = f_dict.read().splitlines()
            return dictionary, int(info[0])
    except IOError:
        print("Failed to open file " + filename)
        exit()

# Function for loading Puzzle File
def insert_puz(filename):
    try:
        with open(filename, "r") as f_puz:
            info = f_puz.readline().split()
            info[0], info[1] = int(info[0]), int(info[1])
            puz = f_puz.read().splitlines()
            new_puz = []
            for i in puz:
                new_puz.append(i.split())
            return new_puz, info
    except IOError:
        print("Failed to open file " + filename)
        exit()

# Load Dictionary File
dictionary, lines = insert_dict(input("Enter dictionary file name: "))
print("Dictionary loaded with " + str(lines) + " words")

### MAIN ###
while flag:
    # Load Puzzle File
    filename = input("Enter puzzle file name: ")
    puz, RowCol = insert_puz(filename)

    # Solve the puzzle
    print("\nPuzzle:")
    p = WordPuzzle(puz, RowCol, dictionary) if ("word" in filename) else MathPuzzle(puz, RowCol)
    p.solve()
    
    # Check for continuing the game
    cont = input("Continue with next puzzle? (y/n): ")
    while (cont.lower() != "n" and cont.lower() != "y"):
        cont = input("Continue with next puzzle? (y/n): ")
    flag = not (cont.lower() == "n")
    
### END ###