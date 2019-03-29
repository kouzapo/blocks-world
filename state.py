from copy import deepcopy

class State:
    def __init__(self, layout, parent = None, move = []):
        self.layout = layout
        self.parent = parent
        self.move = move
    
    def __eq__(self, other_state):
        if other_state != None:
            return self.layout == other_state.layout
        else:
            return False

    def calcChildren(self):
        layout = self.layout
        children = []

        blocks_to_move = [key for key in layout if layout[key][1] == 'c']

        for moving_block in blocks_to_move:
            for target_block in blocks_to_move:
                if moving_block != target_block:
                    temp = deepcopy(layout)
                    move = []

                    released_block = temp[moving_block][0]

                    temp[moving_block][0] = target_block
                    temp[target_block][1] = 'u'

                    move.append(moving_block)

                    if released_block != '-':
                        temp[released_block][1] = 'c'

                        move.append(released_block)
                    else:
                        move.append('table')
                    
                    move.append(target_block)
                    children.append(State(layout = temp, parent = self, move = move))
            
            if layout[moving_block][0] != '-':
                temp = deepcopy(layout)
                move = []

                released_block = temp[moving_block][0]

                temp[moving_block][0] = '-'
                temp[released_block][1] = 'c'

                move.append(moving_block)
                move.append(released_block)
                move.append('table')

                children.append(State(layout = temp, parent = self, move = move))
        
        return children