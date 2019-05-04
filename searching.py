import time
from collections import deque

"""
Four algorithms are implemented in order to sovle the problems:
    
    1) Breadth First Search algorithm (breadth_first_search).
    2) Depth First Search algorithm (depth_first_search).
    3) Best First Search algorithm (heuristic_search with __out_of_place_heuristic as heuristic function).
    4) A* Search algorithm (heuristic_search with __astar_heuristic as heuristic function).

Moreover, two heuristic functions are implemented and used 
in the Best First Search and A* Search algorithms.
"""

def __out_of_place_heuristic(F, goal_layout, blocks_keys):
    """
    The __out_of_place_heuristic is a private heuristic function that
    is used in the Best First Search algorithm. 

    It takes as arguments a search frontier F containing State objects,
    a dict object (goal_layout), containing the layout of the goal state,
    and a list object (blocks_keys), containing the names/keys of the blocks.

    The function counts how many blocks from each state in F are out of place,
    and returns the index of the state with the minimum score 
    i.e. the smallest number of blocks that are not in the final position.
    """
    scores = []     #A list object containing the score of each state.

    for state in F:
        out_of_place = 0     #Initialize each score to 0.

        for key in blocks_keys:     #For each block...
            if state.layout[key] != goal_layout[key]:     #If it is not in its final position...
                out_of_place += 1     #Add 1 to score.
        
        scores.append(out_of_place)
    
    return scores.index(min(scores))     #Return the index of the state with the minimun score.

def __astar_heuristic(F, goal_layout, blocks_keys):
    """
    The __astar_heuristic is a private heuristic function that
    is used in the A* Search algorithm.

    It takes as arguments a search frontier F containing State objects,
    a dict object (goal_layout), containing the layout of the goal state,
    and a list object (blocks_keys), containing the names/keys of the blocks.

    The function is a variation of the __out_of_place_heuristic function,
    with the addition of the distance attribute in the calculation of the scores.
    It counts how many blocks are not in the final position and adds the total number
    of steps from the root. So between two states with equal out of place blocks,
    the heuristic function chooses the one with the smallest distance from the root.
    """
    scores = []     #A list object containing the score of each state.

    for state in F:
        score = 0     #Initialize each score to 0.

        for key in blocks_keys:     #For each block...
            if state.layout[key] != goal_layout[key]:     #If it is not in its final position...
                score += 1     #Add 1 to score.
        
        score += state.distance     #Add the distance from the root to score.
        
        scores.append(score)
    
    return scores.index(min(scores))     #Return the index of the state with the minimun score.

def breadth_first_search(current_state, goal_state, timeout = 60):
    """
    An implementation of the BFS algorithm, taking as arguments a current_state
    i.e. initial state, a goal state and an optional argument timeout (default 60)
    indicating the time before the algorithm stops if no solution is found.

    A queue is used as a structure for storing the nodes/states and a set for keeping the 
    ids of the discovered states in order to check quicker whether a node has been discovered.
    """
    Q = deque([])     #A queue for storing the nodes/states.
    discovered = set()     #A set for keeping the ids of the discovered states.

    Q.append(current_state)     #Add the current/initial state to the queue.
    discovered.add(current_state.id)     #Add the id of the state to the set.

    st = time.perf_counter()     #Start a time counter.

    while Q:     #While Q is not empty...
        if time.perf_counter() - st > timeout:     #If the execution time exceeds the timeout...
            print('Timeout!')
            return None     #Break.

        state = Q.popleft()     #Dequeue an element from the left of the Q.

        if state == goal_state:     #If the state is the goal state, return it and break.
            return state
        
        children = state.calcChildren()     #Else, calculate the children of this state.

        for child in children:     #For each child...
            if child.id not in discovered:     #If this child has not been discovered...
                discovered.add(child.id)     #Mark it as discovered.
                child.parent = state     #Set the parent attribute of the child to be the state that has been dequeued.

                Q.append(child)     #Append the child to Q.

def depth_first_search(current_state, goal_state, timeout = 60):
    """
    An implementation of the DFS algorithm, taking as arguments a current_state
    i.e. initial state, a goal state and an optional argument timeout (default 60)
    indicating the time before the algorithm stops if no solution is found.

    A stack is used as a structure for storing the nodes/states and a set for keeping the 
    ids of the discovered states in order to check quicker whether a node has been discovered.
    """
    S = []     #A stack fot storing the nodes/states.
    discovered = set()     #A set for keeping the ids of the discovered states.

    S.append(current_state)     #Add the current/initial state to the stack.

    st = time.perf_counter()     #Start a time counter.

    while S:     #While S is not empty...
        if time.perf_counter() - st > timeout:     #If the execution time exceeds the timeout...
            print('Timeout!')
            return None      #Break.

        state = S.pop()     #Pop an element from the left of the S.

        if state == goal_state:     #If the state is the goal state, return it and break.
            return state

        if state.id in discovered:     #If the state has been discovered, do nothing.
        	continue

        children = state.calcChildren()     #Else, calculate the children of this state.

        for child in children:     #For each child...
        	S.append(child)     #Append the child to S.

        discovered.add(state.id)     #Mark state as discovered.

def heuristic_search(current_state, goal_state, method, timeout = 60):
    """
    This function implements a heuristic search algorithm. Essensialy, the implementation is the
    same with BFS but the structure for storing the nodes/states is now a list and the choice of the
    node to be examined is made by a heuristic function.

    The functions takes as arguments a current/initial state, a goal state, a method
    i.e. the name of the heuristic function and an optional timeout.
    """
    if method == 'best':     #If the keyword 'best' is passed, the algorithm becomes the Best First Search algorithm.
        heuristic_function = __out_of_place_heuristic
    elif method == 'astar':     #If the keyword 'astar' is passed, the algorithm becomes the A* Search algorithm.
        heuristic_function = __astar_heuristic

    F = []     #A list fot storing the nodes/states.
    discovered = set()     #A set for keeping the ids of the discovered states.
    blocks_keys = list(current_state.layout.keys())     #A list with the names/keys of the blocks.

    F.append(current_state)     #Add the current/initial state to the list.
    discovered.add(current_state.id)     #Add the id of the state to the set.

    st = time.perf_counter()     #Start a time counter.

    while F:     #While F is not empty...
        if time.perf_counter() - st > timeout:     #If the execution time exceeds the timeout...
            print('Timeout!')
            return None     #Break.

        i = heuristic_function(F, goal_state.layout, blocks_keys)     #Return the index of the state with the minimum score in F.
        state = F.pop(i)     #Pop the state with the minimum score.

        if state == goal_state:     #If the state is the goal state, return it and break.
            return state
        
        children = state.calcChildren()     #Else, calculate the children of this state.

        for child in children:     #For each child...
            if child.id not in discovered:     #If this child has not been discovered...
                discovered.add(child.id)     #Mark it as discovered.
                child.parent = state     #Set the parent attribute of the child to be the state that has been poped.

                F.append(child)     #Append the child to F.