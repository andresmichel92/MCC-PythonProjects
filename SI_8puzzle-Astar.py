# import sys
from copy import deepcopy
from heapq import heappush, heappop
from collections import deque
import time


goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

move_options = [[["D", "R"], ["D", "L", "R"], ["D", "L"]], [["U", "D", "R"], ["U", "D", "L", "R"], ["U", "D", "L"]],
                [["U", "R"], ["U", "L", "R"], ["U", "L"]]]


def read_list(file_name):
    master_list = []
    ins = open(file_name, 'r')
    for line in ins:
        n_strings= line.split()
        numbers = [int(n) for n in n_strings]
        master_list.append(numbers)
    ins.close()
    return master_list


def get_pos(list1, val):
    pos = []
    for i, x in enumerate(list1):
        if val in x:
            pos = [i, x.index(val)]
    return pos


def move_zero(puzzle_parent, direction):
        position = puzzle_parent.zero_pos
        moved = deepcopy(puzzle_parent.state)
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


class Puzzle:

    def __init__(self, state):
        self.state = state
        self.state_options = None
        self.h_value = self.get_h()
        self.zero_pos = get_pos(self.state, 0)
        self.moves = move_options[self.zero_pos[0]][self.zero_pos[1]]

    def get_h(self):
        h = 0
        for i in range(3):
            for j in range(3):
                goal_pos = get_pos(goal, self.state[i][j])
                if self.state[i][j] == 0:
                    continue
                h = h + abs(goal_pos[0] - i) + abs(goal_pos[1]-j)
                # print("["+str(i)+", "+str(j)+"]="+ str(self.state[i][j])+" @goal =" + str(goal_pos)+"  h:" + str(h))
        return h

    def __repr__(self):
        return str(self.state)


class TreeNode:

    def __init__(self, puzzle, path=''):
        self.puzzle = puzzle
        self.down_child = None
        self.up_child = None
        self.right_child = None
        self.left_child = None
        self.path = path
        self.level = len(path)
        self.f_value = self.level + self.puzzle.h_value
        self.n_children = len(puzzle.moves)
        self.children = None

    def get_children(self):
        self.children = []
        for a in range(len(self.puzzle.moves)):
            if self.puzzle.moves[a] == "U":
                u_child = Puzzle(move_zero(self.puzzle, "U"))
                self.up_child = TreeNode(u_child, self.path + "U")
                self.children.append(self.up_child)
            if self.puzzle.moves[a] == "D":
                d_child = Puzzle(move_zero(self.puzzle, "D"))
                self.down_child = TreeNode(d_child, self.path + "D")
                self.children.append(self.down_child)
            if self.puzzle.moves[a] == "L":
                l_child = Puzzle(move_zero(self.puzzle, "L"))
                self.left_child = TreeNode(l_child, self.path + "L")
                self.children.append(self.left_child)
            if self.puzzle.moves[a] == "R":
                r_child = Puzzle(move_zero(self.puzzle, "R"))
                self.right_child = TreeNode(r_child, self.path + "R")
                self.children.append(self.right_child)

    def __lt__(self, other):
        return self.f_value < other.f_value

    def __repr__(self):
        return "Node with puzzle: " + str(self.puzzle) + " F value = " + str(self.f_value) + " path =" + self.path


def a_star_solver(initial_puzzle, the_goal):
    start_time = time.time()
    visited = 1
    if initial_puzzle == the_goal:
        print("Success")
    else:
        goal_found = False
        root = TreeNode(initial_puzzle)
        the_heap = []
        root.get_children()
        for c in range(root.n_children):
            heappush(the_heap, root.children[c])
        while not goal_found:
            current_node = heappop(the_heap)
            visited = visited + 1
            if current_node.puzzle.state == the_goal:
                goal_found = True
                print("Path to goal:  " + str(list(current_node.path)))
                print("Cost to Path:  " + str(current_node.level))
                print("Visited Nodes: " + str(visited))
            else:
                current_node.get_children()
                for c in range(current_node.n_children):
                    heappush(the_heap, current_node.children[c])

    print("Elapsed time : " + str(time.time()-start_time))
    print("Used memory : " + str(visited * 72) +" bytes")


# state2 = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
# state3 = [[1, 2, 8], [6, 7, 0], [3, 5, 4]]
# state4 = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]

new_state = read_list("input.txt")
challenge_puzzle = Puzzle(new_state)
a_star_solver(challenge_puzzle, goal)
