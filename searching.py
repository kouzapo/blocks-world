from collections import deque

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