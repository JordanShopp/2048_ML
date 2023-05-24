import numpy as np
import random

#Future feature: enable the addition of prepresenting everything as log base 2


class Board:

    def __init__(self):
        self.FOUR_RATE = .1
        self.board = np.zeros((4,4))
        self.initBoard()
    def __str__(self):
        return str(self.board)
    def initBoard(self):
        self.board = np.zeros((4,4))
        self.fillEmptySpace()
        self.fillEmptySpace()

    def fillEmptySpace(self):
        num_eligible_spots = 16-np.count_nonzero(self.board)
        end_count = random.randint(1,num_eligible_spots)-1
        count = 0
        found=False
        
        for i in range(4):
            if found:
               break
            for j in range(4):
                if found:
                   break
                if(self.board[i][j]==0):
                    if count == end_count:
                        self.board[i][j]= self.nextNewNum()
                        print("hu")
                        found=True
                        count+=1
                    else:
                        count+=1 
                
    def nextNewNum(self):
        if random.random()<self.FOUR_RATE:   
            return(4)
        else:
            return(2)
myBoard = Board()
print(myBoard)

