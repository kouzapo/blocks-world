from state import State

def read_input_file(filename):
    with open('problems/' + filename) as f:
        lines = [line.split() for line in f]

        blocks_names = lines[0][1:]
        blocks_names[-1] = blocks_names[-1][:-1]

        init = lines[1][1:-1]
        init = [i.replace('(', '') for i in init]
        init = [i.replace(')', '') for i in init]

        goal = lines[2][2:]
        goal = [i.replace('(', '') for i in goal]
        goal = [i.replace(')', '') for i in goal]

        initial_layout = {key: ['-', 'c'] for key in blocks_names}
        goal_layout = {key: ['-', 'c'] for key in blocks_names}

        for i in range(len(init)):
            if init[i] == 'CLEAR':
                initial_layout[init[i + 1]][1] = 'c'

            elif init[i] == 'ONTABLE':
                initial_layout[init[i + 1]][0] = '-'
            
            elif init[i] == 'ON':
                initial_layout[init[i + 1]][0] = init[i + 2]
                initial_layout[init[i + 2]][1] = 'u'
        
        for i in range(len(goal)):
            if goal[i] == 'CLEAR':
                goal_layout[goal[i + 1]][1] = 'c'

            elif goal[i] == 'ONTABLE':
                goal_layout[goal[i + 1]][0] = '-'
            
            elif goal[i] == 'ON':
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