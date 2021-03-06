import numpy as np

class Game:

    def __init__(self,num_rows, num_cols, action_space, obs_space):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.action_space = action_space
        self.obs_space = obs_space
    
    def board2array(self):
        new_board = np.zeros(self.obs_space)
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                val = self.board[row][col]
                new_board[(3 * self.num_cols) * row + 3 * col + val] = 1
        return(new_board)

class TicTacToe(Game):

    def __init__(self):
        self.board = np.zeros((3,3),dtype="int")
        self.terminal = False
        super().__init__(3,3,9,27)

    def restart(self):
        self.board = np.zeros((3,3),dtype="int")
        self.terminal = False

    def is_valid(self, action):
        if self.board[int(np.floor(action / 3))][action % 3] != 0:
            return False
        else:
            return True

    def invert_board(self):
        for row in range(3):
            for col in range(3):
                if(self.board[row][col] == 1):
                    self.board[row][col] = 2
                elif(self.board[row][col] == 2):
                    self.board[row][col] = 1

    def step(self,action):
        """
        PARAMS: a valid action (int 0 to 8)
        RETURN: reward (-1,0,1)

        self.board    is updated in the process
        self.terminal is updated in the process
        """

        # insert
        row_index = int(np.floor(action / 3))
        col_index = action % 3
        self.board[row_index][col_index] = 1

        # undecided
        terminal = 1

        # to check for 3 in a row horizontal
        for row in range(3):
            for col in range(3):
                if(self.board[row][col] != 1):
                    terminal = 0
            if(terminal == 1):
                self.terminal = True
                return +1
            else:
                terminal = 1

        # to check for 3 in a row vertical
        for col in range(3):
            for row in range(3):
                if(self.board[row][col] != 1):
                    terminal = 0
            if(terminal == 1):
                self.terminal = True
                return +1
            else:
                terminal = 1

        # diagonal top-left to bottom-right
        for diag in range(3):
            if(self.board[diag][diag] != 1):
                terminal = 0
        if(terminal == 1):
            self.terminal = True
            return +1
        else:
            terminal = 1

        # diagonal bottom-left to top-right
        for diag in range(3):
            if(self.board[2 - diag][diag] != 1):
                terminal = 0
        if(terminal == 1):
            self.terminal = True
            return +1
        else:
            terminal = 1

        # checks if board is filled completely
        for row in range(3):
            for col in range(3):
                if(self.board[row][col] == 0):
                    terminal = 0
                    break
        if terminal == 1:
            self.terminal = True
            
        return 0

    def render(self):
        """
        print to screen the full board nicely
        """
        
        for i in range(3):
            print('\n|', end="")
            for j in range(3):
                if self.board[i][j] == 1:
                    print(' X |' , end="")
                elif self.board[i][j] == 0:
                    print('   |' , end="")
                else:
                    print(' O |' , end="")
        print('\n')
