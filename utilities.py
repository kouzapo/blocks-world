from state import State

"""
This module contains two utility functions for reading and writing files.
"""

def read_input_file(filename):
    with open('problems/' + filename) as f:
        lines = [line.split() for line in f]

        blocks_names = lines[0][1:]
        blocks_names[-1] = blocks_names[-1][:-1]

        initial = lines[1][1:-1]
        initial = [i.replace('(', '') for i in initial]
        initial = [i.replace(')', '') for i in initial]

        goal = lines[2][2:]
        goal = [i.replace('(', '') for i in goal]
        goal = [i.replace(')', '') for i in goal]

        initial_layout = {key: ['-', 'c'] for key in blocks_names}
        goal_layout = {key: ['-', 'c'] for key in blocks_names}

        for i in range(len(initial)):
            '''if initial[i] == 'CLEAR':
                initial_layout[initial[i + 1]][1] = 'c'

            elif initial[i] == 'ONTABLE':
                initial_layout[initial[i + 1]][0] = '-'''
            
            if initial[i] == 'ON':
                initial_layout[initial[i + 1]][0] = initial[i + 2]
                initial_layout[initial[i + 2]][1] = 'u'
        
        for i in range(len(goal)):
            '''if goal[i] == 'CLEAR':
                goal_layout[goal[i + 1]][1] = 'c'

            elif goal[i] == 'ONTABLE':
                goal_layout[goal[i + 1]][0] = '-'''
            
            if goal[i] == 'ON':
                goal_layout[goal[i + 1]][0] = goal[i + 2]
                goal_layout[goal[i + 2]][1] = 'u'

    return State(layout = initial_layout), State(layout = goal_layout)

def write_output_file(solution, filename):
    current_state = solution
    path = []
    i = 1
    
    while True:
        path.append(current_state)

        current_state = current_state.parent
        
        if current_state.parent == None:
            path.append(current_state)
            break
    
    path.reverse()
    
    with open(filename, 'w') as f:
        for state in path[1:]:
            move = state.move

            f.write(str(i) + '. Move(' + move[0] + ', ' + move[1] + ', ' + move[2] + ')\n')
            i += 1
    
    return len(path[1:])