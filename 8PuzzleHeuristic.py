# Calvin Aduma
# CPSC 4420
# Assignment 1

import random

class AssignmentOne:
    # initializes a puzzle board object with a current state
    def __init__(self, current_state:str):
        self.puzzle_board = []
        self.possible_states = []
        self.current_state = current_state
        row = []
        for character in current_state:
            row.append(int(character))
            if len(row) == 3:
                self.puzzle_board.append(row)
                row = []
    # gets current state
    def getCurrentState(self):
        return self.current_state

    # returns 10 randomly selected states from list of possible states
    def list_10_random_states(self)->list[str]:
        random_states = []
        for i in range(10):
            random_state_number = random.randint(0,len(self.possible_states))
            random_states.append(self.possible_states[random_state_number])
        return random_states

    # sets puzzle board to specific state
    def setState(self, state:str)->None:
        self.puzzle_board = []
        row = []
        for character in state:
            row.append(int(character))
            if len(row) == 3:
                self.puzzle_board.append(row)
                row = []

    # prints all possible states
    def listStates(self)->list[str]:
        for state in self.possible_states:
            print(state)

    # finds all possible states with recursion
    def findPossibleStates(self, current_state)->None:
        # recurse to find possible staes
        # check every possible move and in visited before going into new state.
        if current_state not in self.possible_states:
            self.possible_states.append(current_state)
        else:
            return
        self.findPossibleStates(self.actionState(1))
        self.findPossibleStates(self.actionState(2))
        self.findPossibleStates(self.actionState(3))
        self.findPossibleStates(self.actionState(4))

    # returns the current state
    def currentState(self)->str:
        state = ""
        for row in self.puzzle_board:
            for col in row:
                state += str(col)
        return state

    # returns the position of the zero/empty block as a list [x,y]
    def zeroPosition(self)->list:
        position = []
        for rowIdx in range(len(self.puzzle_board)):
            for colIdx in range(len(self.puzzle_board[rowIdx])):
                if self.puzzle_board[rowIdx][colIdx] == 0:
                    position.append(rowIdx)
                    position.append(colIdx)
        return position

    # checks if move is valid or not
    def checkValidMove(self, move:int)->bool:
        zero_position = self.zeroPosition()
        if move == 1:
            # up
            if zero_position[0] - 1 < 0:
                return False
        elif move == 2:
            # down
            if zero_position[0] + 1 >= len(self.puzzle_board):
                return False
        elif move == 3:
            # left
            if zero_position[1] - 1 < 0:
                return False
        elif move == 4:
            # right
            if zero_position[1] - 1 >= len(self.puzzle_board[0]):
                return False
        return True
        
    # takes an action on the puzzle board given an input
    def actionState(self, move:int)->None:
        zero_position = self.zeroPosition()
        if move == 1 and self.checkValidMove(move) is True:
            # up
            swap_item_position = zero_position.copy()
            swap_item_position[0] -= 1
            self.swap(swap_item_position, zero_position)
        elif move == 2 and self.checkValidMove(move) is True:
            # down
            swap_item_position = zero_position.copy()
            swap_item_position[0] += 1
            self.swap(swap_item_position, zero_position)
        elif move == 3 and self.checkValidMove(move) is True:
            # left
            swap_item_position = zero_position.copy()
            swap_item_position[1] -= 1
            self.swap(swap_item_position, zero_position)
        elif move == 4 and self.checkValidMove(move) is True:
            # right
            swap_item_position = zero_position.copy()
            swap_item_position[1] += 1
            self.swap(swap_item_position, zero_position)
        return self.currentState

    # swaps 2 valid positions: pos1 and pos2
    def swap(self, pos1:list[str], pos2:list[str])->None:
        temp = self.puzzle_board[pos1[0]][pos1[1]]
        self.puzzle_board[pos1[0]][pos1[1]] = self.puzzle_board[pos2[0]][pos2[1]]
        self.puzzle_board[pos2[0]][pos2[1]] = temp

#current_state = input("Current State: ")
#A1 = AssignmentOne(current_state)
#action = int(input("Action: "))
#A1.actionState(action)
A1 = AssignmentOne('724506831')
A1.actionState(3)
A1.findPossibleStates(A1.getCurrentState())
A1.listStates()
