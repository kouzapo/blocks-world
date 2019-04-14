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

def breadth_first_search(current_state, goal_state, timeout = 60):
    Q = deque([])
    discovered = set()

    Q.append(current_state)
    discovered.add(current_state.id)

    st = time.perf_counter()

    while Q:
        if time.perf_counter() - st > timeout:
            print('Timeout!')
            return None

        state = Q.popleft()

        if state == goal_state:
            return state
        
        children = state.calcChildren()

        for child in children:
            if child.id not in discovered:
                discovered.add(child.id)
                child.parent = state

                Q.append(child)

def depth_first_search(current_state, goal_state, timeout = 60):
    S = []
    discovered = set()

    S.append(current_state)

    st = time.perf_counter()

    while S:
        if time.perf_counter() - st > timeout:
            print('Timeout!')
            return None

        state = S.pop()

        if state == goal_state:
            return state

        if state.id in discovered:
        	continue
            #discovered.append(state)
        children = state.calcChildren()

        for child in children:
        	S.append(child)

        discovered.add(state.id)

def heuristic_search(current_state, goal_state, method, timeout = 60):
    if method == 'best':
        heuristic_function = __out_of_place_heuristic
    elif method == 'astar':
        heuristic_function = __astar_heuristic

    F = []
    discovered = set()
    blocks_keys = list(current_state.layout.keys())

    F.append(current_state)
    discovered.add(current_state.id)

    st = time.perf_counter()

    while F:
        if time.perf_counter() - st > timeout:
            print('Timeout!')
            return None

        i = heuristic_function(F, goal_state.layout, blocks_keys)
        state = F.pop(i)

        if state == goal_state:
            return state
        
        children = state.calcChildren()

        for child in children:
            if child.id not in discovered:
                discovered.add(child.id)
                child.parent = state

                F.append(child)