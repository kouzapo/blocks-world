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

def breadth_first_search(current_state, goal_state):
    Q = deque([])
    discovered = []

    Q.append(current_state)
    discovered.append(current_state)

    while Q:
        state = Q.popleft()

        if state == goal_state:
            return state
        
        children = state.calcChildren()

        for child in children:
            if child not in discovered:
                discovered.append(child)
                child.parent = state

                Q.append(child)

def depth_first_search(current_state, goal_state):
    S = []
    discovered = []

    S.append(current_state)

    while S:
        state = S.pop()

        if state == goal_state:
            return state
        
        if state not in discovered:
            discovered.append(state)

            children = state.calcChildren()

            for child in children:
                if child not in discovered:
                    S.append(child)

def best_first_search(current_state, goal_state):
    F = []
    discovered = []
    blocks_keys = list(current_state.layout.keys())

    F.append(current_state)
    discovered.append(current_state)

    while F:
        i = __out_of_place_heuristic(F, goal_state.layout, blocks_keys)
        state = F.pop(i)

        if state == goal_state:
            return state
        
        children = state.calcChildren()

        for child in children:
            if child not in discovered:
                discovered.append(child)
                child.parent = state

                F.append(child)
