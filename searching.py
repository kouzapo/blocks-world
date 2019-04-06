import time
from collections import deque

def __out_of_place_heuristic(F, goal_layout, blocks_keys):
    scores = []

    for state in F:
        out_of_place = 0

        for key in blocks_keys:
            if state.layout[key] != goal_layout[key]:
                out_of_place += 1
        
        scores.append(out_of_place)
    
    return scores.index(min(scores))

def __astar_heuristic(F, goal_layout, blocks_keys):
    scores = []

    for state in F:
        score = 0

        for key in blocks_keys:
            if state.layout[key] != goal_layout[key]:
                score += 1
        
        score += state.distance
        
        scores.append(score)
    
    return scores.index(min(scores))


def breadth_first_search(current_state, goal_state):
    Q = deque([])
    discovered = set()
    #discovered = []

    Q.append(current_state)
    discovered.add(current_state)
    #discovered.append(current_state)

    st = time.perf_counter()

    while Q:
        if time.perf_counter() - st > 60:
            print('Timeout!')
            return None

        state = Q.popleft()

        if state == goal_state:
            return state
        
        children = state.calcChildren()

        for child in children:
            if child not in discovered:
                discovered.add(child)
                #discovered.append(child)
                child.parent = state

                Q.append(child)

def depth_first_search(current_state, goal_state):
    S = []
    discovered = set()
    #discovered = []

    S.append(current_state)

    st = time.perf_counter()

    while S:
        if time.perf_counter() - st > 60:
            print('Timeout!')
            return None

        state = S.pop()

        if state == goal_state:
            return state
        
        if state not in discovered:
            discovered.add(state)
            #discovered.append(state)

            children = state.calcChildren()

            for child in children:
                if child not in discovered:
                    S.append(child)

def heuristic_search(current_state, goal_state, method):
    if method == 'best':
        heuristic_function = __out_of_place_heuristic
    elif method == 'astar':
        heuristic_function = __astar_heuristic

    F = []
    discovered = set()
    #discovered = []
    blocks_keys = list(current_state.layout.keys())

    F.append(current_state)
    #discovered.append(current_state)
    discovered.add(current_state)

    st = time.perf_counter()

    while F:
        if time.perf_counter() - st > 60:
            print('Timeout!')
            return None

        i = heuristic_function(F, goal_state.layout, blocks_keys)
        state = F.pop(i)

        if state == goal_state:
            return state
        
        children = state.calcChildren()

        for child in children:
            if child not in discovered:
                #discovered.append(child)
                discovered.add(child)
                child.parent = state

                F.append(child)