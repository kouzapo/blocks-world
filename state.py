from copy import deepcopy

class State:
    """
    The State class. Each State object represents a possible arrangement of the blocks on the table.

    Attributes:

        layout: 
        A dict structure with keys the names of the blocks and values a list with two items.
        The first item is a character on which the block stands on. If the blocks is on the table,
        the '-' character represents this possibility. The second item is a character 
        indicating whether or not the block if free to move. 'c' for clear, 'u' for unclear.

            example:                                    |A|
            For a state with an arrangement like this:  |B|C|

            The layout attribute is {'A': ['B', 'c'], 'B': ['-', 'u'], 'C': ['-', 'c']}.
        
        The dictionary data structure in Python has constant access time complexity O(1).

        parent: 
        A State object indicating the parent of the current state. Basically, it is a pointer
        to another state object. The initial state hash parent = None.

        move:
        A list with 3 items which represents the move from which the current state is created.
        The first item is the block that has benn moved. The second item is the block that
        has been released and the third item is the destination block.

            example:
            |A|           |A| 
            |B|C| ----> |B|C|   The move attribute is ['A', 'B', 'C']
        
        The inital state has move = [].
        
        distance:
        An integer indicating the distance from the root - inital state.
        Basically counts how many moves have been done to get to this state.
        The initial state has distance = 0.

        id:
        A string which is unique for each state. Each state hash an is which is constructed
        using the items of the layout attribute so two states have the same id if and only if
        they have the same items in their layout attributes. The id is used by the searching
        algorithms in order to check whether or not a state has been discoverd.

            example:                                      |A|
            For a state with an arrangement like this:  |B|C|
            and layout {'A': ['B', 'c'], 'B': ['-', 'u'], 'C': ['-', 'c']},
            the id is 'Bc-u-c'.
    """

    def __init__(self, layout, parent = None, move = [], distance = 0):
        self.layout = layout
        self.parent = parent
        self.move = move
        self.distance = distance

        values = list(self.layout.values())     #A list of the names of the blocks.

        self.id = ''.join([str(i) for s in values for i in s])     #Create the id attribute.
    
    def __eq__(self, other_state):
        """
        Override the build in __eq__ method. Two states are equal if and only if they have
        the same id.
        """
        if other_state != None:
            return self.id == other_state.id
        else:
            return False

    def calcChildren(self):
        """
        The method creates a list of all the states that can be produced from a given state.
        It moves all the clear blocks to all available destinations and creates a new state 
        for each alteration.

        example:                                      |A|
        For a state with an arrangement like this:  |B|C|
        the free blocks are |A| and |B|. The children that can be created are:

                        |B|
        |A|             |A|
        |B|C|, |A|B|C|, |C|.

        """
        layout = self.layout
        children = []

        free_blocks = [key for key in layout if layout[key][1] == 'c']     #The blocks that can be moved.

        for moving_block in free_blocks:     #For each free block that will be moved...
            for target_block in free_blocks:
                if moving_block != target_block:
                    temp = deepcopy(layout)     #Copy the current layout in order to alter it.
                    move = []
                    distance = 0

                    released_block = temp[moving_block][0]     #The 'released_block' is the first item of the list in layout with key == moving_block.

                    temp[moving_block][0] = target_block     #The 'moving block' now is on top of the 'target_block'.
                    temp[target_block][1] = 'u'     #And the 'target_block' is now unclear.

                    move.append(moving_block)     #Add the 'moving_block' to 'move' list. 

                    if released_block != '-':     #If the 'released_block" is not '-' i.e. is not the table...
                        temp[released_block][1] = 'c'     #Set the block clear.

                        move.append(released_block)     #Add the 'released_block' to 'move' list.
                    else:
                        move.append('table')
                    
                    move.append(target_block)     #Add the 'target_block' to 'move' list.
                    distance = self.distance + 1     #The distance of the child is the distance of the parent plus 1.

                    children.append(State(layout = temp, parent = self, move = move, distance = distance))     #Add to 'children' list a new State object.
            
            if layout[moving_block][0] != '-':     #If the 'moving_block' is not currently on the table, create a state that it is.
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