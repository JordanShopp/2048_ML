import numpy as np
import random

#Future feature: enable the addition of prepresenting everything as log base 2

DIRECTIONS = {'U':0, 'R':1, 'D':2, 'L':3}
class Board:
    def __init__(self):
        self.FOUR_RATE = .1
        self.board = np.zeros((4,4))
        self.init_board()
        self.score=0
    def __str__(self):
        return str(self.board)
    def init_board(self):
        self.board = np.zeros((4,4))
        self.fill_empty_space()
        self.fill_empty_space()
    def get_elgible_moves(self):
        result = np.zeros(4)
        k=0
        for key in DIRECTIONS:
            if self.board != self.get_move_result(key):
                result[k]=1
            k+=1
        return(result)
    def get_score(self):
        return self.score
    def move(self, direction):
        """Updates the board with the correct move. Throws an exception if the direction is illegal
        FUTURE UPDATE: Maybe throw exception if its an impossible move
        Args:
            direction (int): 0 is up, 1 is right, 2 is down, 3 is left

        Returns:
            int: amount of points gained from moving
        """
        
        new_board, points_gained=self.get_move_result(direction)
        if (new_board!=self.board).any():
            self.board=new_board
            self.score+=points_gained
            self.fill_empty_space()
    
    
    def get_move_result(self, direction):
        board_copy= np.copy(self.board)
        board_copy= np.rot90(board_copy,DIRECTIONS[direction])
        points = 0
        #match matches
        for j in range(4):
            #clear empty spots
            for i in range(3,0,-1):
                if board_copy[i][j]!=0 and board_copy[i-1][j]==0:
                    board_copy[i-1][j]= board_copy[i][j]
                    board_copy[i][j]=0
            #match them
            for i in range (3):
                if board_copy[i][j]==board_copy[i+1][j] and  board_copy[i][j] != 0: #No, the next spot below
                    points+= board_copy[i][j]*2
                    board_copy[i][j]*=2
                    board_copy[i+1][j]=0
            #clear empty spots
            for i in range(3,0,-1):
                if board_copy[i][j]!=0 and board_copy[i-1][j]==0:
                    board_copy[i-1][j]= board_copy[i][j]
                    board_copy[i][j]=0
        board_copy = np.rot90(board_copy,4-DIRECTIONS[direction])
        return board_copy,points
                   
    def check_loss(self):
        """Determines whether or not the board is lost
        
        Returns:
            boolean: 1 if the game is lost
        """
        print(f"Elgible moves: {self.get_elgible_moves()}")
        return((self.get_elgible_moves()==[0,0,0,0]).all())
    def fill_empty_space(self):
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
                        self.board[i][j]= self.next_new_num()
                        found=True
                        count+=1
                    else:
                        count+=1 
    def next_new_num(self):
        if random.random()<self.FOUR_RATE:   
            return(4)
        else:
            return(2)

class GameKeyBoard:
    def __init__(self):
        self.myBoard = Board()
    def get_direction_kb():
        result = ""
        while not result in DIRECTIONS.keys():       
            result=input("Type U, L, D, or R?")
        return(result)
    def turn(self):
        print(f"Is Lost: {self.myBoard.check_loss()}")
        self.myBoard.move(GameKeyBoard.get_direction_kb())
    def play(self):
        while(not self.myBoard.check_loss()):
            print(self.myBoard)
            print(f"score: {self.myBoard.get_score()}")
            self.turn()
        

        
Game = GameKeyBoard()
Game.play()

