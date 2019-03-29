import time
import sys

from state import State
from searching import *
from utilities import *

def main():
    st = time.perf_counter()

    if len(sys.argv) == 4:
        method = sys.argv[1]
        input_file = sys.argv[2]
        output_file = sys.argv[3]

        initial_state, goal_state = read_input_file(filename = input_file)

        if method == 'breadth':
            solution = breadth_first_search(current_state = initial_state, goal_state = goal_state)
        elif method == 'depth':
            solution = depth_first_search(current_state = initial_state, goal_state = goal_state)
        else:
            solution = None
            print('Usage: python world.py <method> <input filename> <output filename>')

        if solution == goal_state:
            write_output_file(solution = solution, filename = output_file)

            print("Execution time: " + str(time.perf_counter() - st))
            
    else:
        print('Usage: python world.py <method> <input filename> <output filename>')

if __name__ == '__main__':
	main()