#
# name:Daniel Monzon

import random
rand = random.Random()
def inarow_Neast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading east and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading south and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading northeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start - (N-1) < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading southeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # the string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # bottom of the board

        # and the numbers underneath here

        return s       # the board is complete, return it

    def addMove(self, col, ox):
        """ This method takes two arguments: the first, col, represents the index of 
            the column to which the checker will be added. The second argument, ox,
            will be a 1-character string representing the checker to add to the board.
            That is, ox should either be 'X' or 'O' (again, capital O, not zero).
        """
        d = self.height -1
        for row in range(0, self.height):
            if self.data[d - row][col] == ' ' :
                self.data[d - row][col] = ox
                return 

    def clear(self):
        """ should clear the board that calls it
        """
        for row in range(0, self.height):
            for col in range(0, self.width):
                self.data[row][col] = ' ' 

    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'


    def allowsMove(self, c):
        """ This method should return True if the calling object (of type Board) does
            allow a move into column c. It returns False if column c is not a legal 
            column number for the calling object. It also returns False if column c is
            full. Thus, this method should check to be sure that c is within the range 
            from 0 to the last column and make sure that there is still room left in 
            the column!
        """
        if 0 <= c < self.width:
            for row in range(self.height-1):
                if self.data[row][c] == ' ':
                    return True
                else:
                    return False
        else:
            return False


    def isFull(self):
        """This method should return True if the calling object (of type Board) is 
            completely full of checkers. It should return False otherwise.
        """
        for row in range(0, self.height):
            for col in range(0, self.width):
               if self.data[row][col] == ' ':
                   return False
        return True

    def delMove(self, c): 
        """This method should do the opposite of addMove. It should remove the top
            checker from the column c. If the column is empty, then delMove should
            do nothing.
        """
        for row in range(0, self.height):
                if self.data[row][c] != ' ':
                    self.data[row][c] = ' '
                    return 
        
    def tetrisClear(self):
        '''Clears a col if it is full like it is similar to the way it works in tetris
        '''
        for col in range(self.width):
            for row in range(self.height):
                if self.data[row][col] != ' ':
                    if self.allowsMove(col) == False:
                        for row in range(self.height):
                            self.data[row][col] = ' '
                            
        

    def winsFor(self, ox):
        """This method's argument ox is a 1-character checker: either 'X' or 'O'. It 
            should return True if there are four checkers of type ox in a row on the board. 
            It should return False othwerwise. Important Note: you need to check whether the 
            player has won horizontally, vertically, or diagonally (and there are two different 
            directions for a diagonal win).
        """
        for row in range(0, self.height):
            for col in range(0, self.width):
                if inarow_Neast( ox, row, col, self.data, 4)\
                   or inarow_Nsouth( ox, row, col, self.data, 4)\
                   or inarow_Nnortheast( ox, row, col, self.data, 4)\
                   or inarow_Nsoutheast( ox, row, col, self.data, 4):
                    return True
        return False

    def hostGame(self):
        """This method brings everything together into the familiar game. It should host a game 
            of Connect Four, using the methods listed above to do so. In particular, it should 
            alternate turns between 'X' (who will always go first) and 'O' (who will always 
            go second). It should ask the user (with the input function) to select a 
            column number for each move.
        """
        while self.isFull() != True:
            cX = -1
            while not self.allowsMove(cX):
                cX = int(input("X'S CHOICE - Choose a column: "))
                type(cX)
            if self.allowsMove(cX):
                self.addMove(cX, 'X')
                print(self)
                if self.winsFor('X'):
                    print("X wins--Congratulations!")
                    break
            
            
            #cO = -1
            #while not self.allowsMove(cO):
            #    cO = int(input("O'S CHOICE - Choose a column: "))
            #    type(cO)
            d = self.aiMove('O')
            if self.allowsMove(d):
                self.addMove( d, 'O')
                print(self)
            if self.winsFor('O'):
                print("O wins--Congratulations!")
                break
        if self.isFull() == True:
            print("It's a tie!")
            
        print("Good Game!")

    def colsToWin(self, ox):
        """colsToWin method should return the list of columns where ox can move in 
            the next turn in order to win and finish the game.
        """
        L = []
        for col in range(0, self.width):
            if self.allowsMove(col):
                self.addMove(col, ox)
                if self.winsFor(ox):
                    L += [col]
                self.delMove(col)
        return L

    def aiMove(self, ox):
        """aiMove should return a single integer, which must be a legal column in which 
            to make a move.
        """
        L = self.colsToWin(ox)
        if ox == 'X':
            O = self.colsToWin('O')
        if ox == 'O':
            O = self.colsToWin('X')
        
        if L == []:
            if O == []:
                for c in range(0,self.width):
                    if self.allowsMove(c):
                        return c
            else:
                return O[0]
        else:
            return L[0]
    
    def playGame(self, px, po):
        """playGame does just that: it calls the nextMove method for two objects of type Player in order to play 
            a game. Those objects are named px and po.
        """
        while not self.isFull():
            if px == 'human':
                cX = -1
                while not self.allowsMove(cX):
                    cX = int(input("X'S CHOICE - Choose a column: "))
                    type(cX)
                self.addMove(cX, 'X')
            else:
                self.addMove(px.nextMove(self), "X")
            print(self)
            
            if self.winsFor('X'):
                print("X wins--Congratulations!")
                break
            self.tetrisClear()

            if po == 'human':
                cY = -1
                while not self.allowsMove(cY):
                    cY = int(input("O'S CHOICE - Choose a column: "))
                    type(cY)
                self.addMove(cY, 'O')
            else:
                self.addMove(po.nextMove(self), "O")
            print(self)

            if self.winsFor('O'):
                print("O wins--Congratulations!")
                break
            self.tetrisClear()
        if self.isFull():
            print("It's a tie!")
            

class Player:
    """An AI player for Connect Four."""
    def __init__(self, ox, tbt, ply):
        """This constructor first takes in a one-character string ox: this will be either 
        'X' or 'O'. Second, it takes in tbt, a string representing the tiebreaking type of 
        the player. It will be one of 'LEFT', 'RIGHT', or 'RANDOM'. The third argument, ply, 
        will be a nonnegative integer representing the number of moves that the player should 
        look into the future when evaluating where to go next. 
        """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply
    
    def __repr__(self):
        """Create a string represenation of the player."""
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s

    def oppCh(self): 
        """This method should return the other kind of checker or playing piece, 
        i.e., the piece being played by self's opponent. In particular, if self 
        is playing 'X', this method returns 'O' and vice-versa.
        """
        if self.ox == 'X':
            return 'O'
        elif self.ox == 'O':
            return 'X'
        else:
            return 

    def scoreBoard(self, b):
        """This method should return a single float value representing the score of the input b, 
        which you may assume will be an object of type Board. This should return 100.0 if the board b 
        is a win for self. It should return 50.0 if it is neither a win nor a loss for self, and it 
        should return 0.0 if it is a loss for self (i.e., the opponent has won).
        """
        if b.winsFor(self.ox):
            return 100.0
        elif b.winsFor(self.oppCh()):
            return 0.0
        else:
            return 50.0

    def tiebreakMove(self, scores):
        '''This method takes in scores, which will be a nonempty 
        list of floating-point numbers. If there is only one highest score 
        in that scores list, this method should return its COLUMN number, not 
        the actual score! Note that the column number is the same as the index into the list scores. 
        If there is more than one highest score because of a tie, this method should return the COLUMN 
        number of the highest score appropriate to the player's tiebreaking type. 
        '''
        maxIndices = []
        for x in range(len(scores)):
            if scores[x] == max(scores):
                maxIndices = maxIndices + [x]
        if len(scores) == 1:
           return maxIndices[0]
        if self.tbt == 'LEFT':
            return maxIndices[0]
        if self.tbt == 'RIGHT':
            return maxIndices[len(maxIndices)-1]
        if self.tbt == 'RANDOM':
            return rand.choice(maxIndices)
            #maxIndices[randint( 0, len(maxIndices))]
  

    def scoresFor(self, b):
        """ This method is the heart of the Player class! Its job is to return a list of scores, with the 
        cth score representing the "goodness" of the input board after the player moves to column c. And, 
        "goodness" is measured by what happens in the game after self.ply moves.
        """
       
        scores = [50]*b.width
        for x in range(0, b.width):
            scores[x] = self.scoreBoard(b)
            if not b.allowsMove(x):
                scores[x] = -1
            elif self.ply > 0:
                b.addMove( x, self.ox)
                if b.isFull():
                    scores[x] = self.scoreBoard(b)
                else:
                    op = Player(self.oppCh(), self.tbt, self.ply-1)
                    opscores = op.scoresFor(b)
                    scores[x] = 100 - max(opscores)
                b.delMove(x)
        return scores

    def nextMove(self, b):
        """ This method accepts b, an object of type Board, and returns an integer—namely, the column number 
            that the calling object (of class Player) chooses to move to.
        """
        scores = self.scoresFor(b)
        return self.tiebreakMove(scores)
