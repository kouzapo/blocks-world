"""
The Blocks World AI problem implemented and sovled with Python.

Creator: Apostolos Anastasios Kouzoukos, dai17038
Email: kouzoukos97@gmail.com
Github: https://github.com/kouzapo
"""

import time
import sys
import os

from state import State
from searching import breadth_first_search, depth_first_search, heuristic_search
from utilities import read_input_file, write_output_file

def main():
    st = time.perf_counter()     #Start a time counter.

    if len(sys.argv) == 4:     #If the length of the keyword arguments is four...
        method = sys.argv[1]     #The second argument is the method/algorithm used to find a solution.
        input_file = sys.argv[2]     #The third argument is a .txt file containing the initial and final state of the problem.
        output_file = sys.argv[3]     #The fourth argument is a .txt file containing the solution of the problem.

        initial_state, goal_state = read_input_file(filename = input_file)     #Read the input file and return two state objects.

        if method == 'breadth':     #Check which method is selected and solve the problem accordingly.
            solution = breadth_first_search(current_state = initial_state, goal_state = goal_state)
        elif method == 'depth':
            solution = depth_first_search(current_state = initial_state, goal_state = goal_state)
        elif method == 'best':
            solution = heuristic_search(current_state = initial_state, goal_state = goal_state, method = 'best', timeout = 3000)
        elif method == 'astar':
            solution = heuristic_search(current_state = initial_state, goal_state = goal_state, method = 'astar', timeout = 3000)
        else:     #If the method argument is none of the above, print a usage message.
            solution = None
            print('Usage: python bw.py <method> <input filename> <output filename>')

        if solution == goal_state:     #If the solution is equal to the goal state...
            number_of_moves = write_output_file(solution = solution, filename = output_file)     #Write the solution file and return the number of moves.

            print('Solution found!')
            print('Number of blocks:', len(initial_state.layout.keys()))
            print('Method:', method)
            print('Number of moves:', number_of_moves)
            print('Execution time:', str(round(time.perf_counter() - st, 4)))
    else:     #Else, if the length of the keyword arguments is not equal to four, print a usage message.
        print('Usage: python bw.py <method> <input filename> <output filename>')

if __name__ == '__main__':
	main()