from state import State

"""
This module contains two utility functions for reading and writing files.
"""

def read_input_file(filename):
    """
    This function reads a problem file and returns two State objects, one for the initial
    state and one for the goal state.
    """
    with open('problems/' + filename) as f:
        lines = [line.split() for line in f]     #Read the file by line and split it.

        blocks_names = lines[0][1:]     #Get the blocks names.
        blocks_names[-1] = blocks_names[-1][:-1]     #Remove the parenthesis from the last block name.

        initial = lines[1][1:-1]     #Get the initial state.
        initial = [i.replace('(', '') for i in initial]     #Remove the parentheses.
        initial = [i.replace(')', '') for i in initial]

        goal = lines[2][2:]     #Get the goal state.
        goal = [i.replace('(', '') for i in goal]     #Remove the parentheses.
        goal = [i.replace(')', '') for i in goal]

        initial_layout = {key: ['-', 'c'] for key in blocks_names}     #Construct the inital layout.
        goal_layout = {key: ['-', 'c'] for key in blocks_names}     #Construct the goal layout.

        for i in range(len(initial)):
            if initial[i] == 'ON':
                initial_layout[initial[i + 1]][0] = initial[i + 2]
                initial_layout[initial[i + 2]][1] = 'u'
        
        for i in range(len(goal)):
            if goal[i] == 'ON':
                goal_layout[goal[i + 1]][0] = goal[i + 2]
                goal_layout[goal[i + 2]][1] = 'u'

    return State(layout = initial_layout), State(layout = goal_layout)     #Return two state objects.

def write_output_file(solution, filename):
    """
    This function is taking as arguments a State object which is a solution of the problem,
    and a filename to write the steps towards the solution.
    """
    current_state = solution     #The state we start, which is the last i.e. the solution.
    path = []     #The path from the solution towards the intial state.
    i = 1
    
    while True:
        path.append(current_state)     #Add the current state i.e. solution, in the list.

        current_state = current_state.parent     #The current state now becomes the parent of it.
        
        if current_state.parent == None:     #If the current state has no parent...
            path.append(current_state)     #Add the current state in the list.
            break
    
    path.reverse()     #Reverse the list.
    
    with open(filename, 'w') as f:     #Open the output file.
        for state in path[1:]:     #For every state in the path, except the first one which is the initial state that has no previous move...
            move = state.move     #Get the move.

            f.write(str(i) + '. Move(' + move[0] + ', ' + move[1] + ', ' + move[2] + ')\n')     #Write the move.
            i += 1     #Increment the counter.
    
    return len(path[1:])     #Return the number of steps.