from copy import deepcopy
from hashlib import md5

class State:
    def __init__(self, layout, parent = None, move = [], distance = 0):
        self.layout = layout
        self.parent = parent
        self.move = move
        self.distance = distance

        values = list(self.layout.values())

        self.id = ''.join([str(i) for s in values for i in s])
    
    def __eq__(self, other_state):
        if other_state != None:
            return self.id == other_state.id
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
                    distance = 0

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
                    distance = self.distance + 1

                    children.append(State(layout = temp, parent = self, move = move, distance = distance))
            
            if layout[moving_block][0] != '-':
                temp = deepcopy(layout)
                move = []
                distance = 0

                released_block = temp[moving_block][0]

                temp[moving_block][0] = '-'
                temp[released_block][1] = 'c'

                move.append(moving_block)
                move.append(released_block)
                move.append('table')

                distance = self.distance + 1

                children.append(State(layout = temp, parent = self, move = move, distance = distance))
        
        return children