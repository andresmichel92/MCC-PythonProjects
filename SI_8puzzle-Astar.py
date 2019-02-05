import sys
from copy import deepcopy
from collections import deque
import time
start_time = time.time()

goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

move_options = [[["D", "R"], ["D", "L", "R"], ["D", "L"]], [["U", "D", "R"], ["U", "D", "L", "R"], ["U", "D", "L"]],
                [["U", "R"], ["U", "L", "R"], ["U", "L"]]]


class Puzzle:

    def __init__(self, state):
        self.state = state
        self.state_options = None
        self.state_fitness = self.get_fitness()
        self.zero_pos = self.get_zero_pos()
        self.moves = move_options[self.zero_pos[0]][self.zero_pos[1]]

    def get_zero_pos(self):
        for i, x in enumerate(self.state):
            if 0 in x:
                self.zero_pos = [i, x.index(0)]
        return self.zero_pos

    def get_fitness(self):
        count = 0
        for i, x in enumerate(goal):
            if self.state[i][0] == goal[i][0]:
                count = count + 1
            if self.state[i][1] == goal[i][1]:
                count = count + 1
            if self.state[i][2] == goal[i][2]:
                count = count + 1
        return count

    def move_zero(self, direction, position):
        moved = deepcopy(self.state)
        if direction == "U":
            moved[position[0]][position[1]] = moved[position[0]-1][position[1]]
            moved[position[0] - 1][position[1]] = 0
        elif direction == "D":
            moved[position[0]][position[1]] = moved[position[0]+1][position[1]]
            moved[position[0] + 1][position[1]] = 0
        elif direction == "R":
            moved[position[0]][position[1]] = moved[position[0]][position[1]+1]
            moved[position[0]][position[1]+1] = 0
        elif direction == "L":
            moved[position[0]][position[1]] = moved[position[0]][position[1]-1]
            moved[position[0]][position[1]-1] = 0
        return moved


class TreeNode:

    def __init__(self, puzzle, path=''):
        self.puzzle = puzzle
        self.down_child = None
        self.up_child = None
        self.right_child = None
        self.left_child = None
        self.path = path


state2 = [[8,1,2],[6,7,0],[3,5,4]]
puzzle1 = Puzzle(state2)
print(puzzle1.zero_pos)
print(puzzle1.moves)
print(puzzle1.move_zero(puzzle1.moves[2], puzzle1.zero_pos))
print(puzzle1.state)
