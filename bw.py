import time
import sys

from state import State
from searching import breadth_first_search, depth_first_search, best_first_search
from utilities import read_input_file, write_output_file

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
        elif method == 'best':
            solution = best_first_search(current_state = initial_state, goal_state = goal_state)
        else:
            solution = None
            print('Usage: python bw.py <method> <input filename> <output filename>')

        if solution == goal_state:
            number_of_moves = write_output_file(solution = solution, filename = output_file)

            print('Solution found!')
            print('Number of blocks:', len(initial_state.layout.keys()))
            print('Method:', method)
            print('Number of moves:', number_of_moves)
            print('Execution time:', str(round(time.perf_counter() - st, 4)))
            
    else:
        print('Usage: python bw.py <method> <input filename> <output filename>')

if __name__ == '__main__':
	main()