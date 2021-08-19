from constants import (
    CUP_SIZE,
    TREE_DEPTH
)

class CupNode: 
    def __init__(self, x, y, size=CUP_SIZE): 
        self.x = x
        self.y = y
        self.size = size 

        self.amount = 0
        self.left = None 
        self.right = None
    
    def fill(self, pour_amount):
        if self.amount + pour_amount >= self.size:
            pre_pour_amount = self.amount
            self.amount = self.size
            return pre_pour_amount + pour_amount - self.size
        else: 
            self.amount += pour_amount
            return 0

class CupTree: 
    def __init__(self, depth=TREE_DEPTH, CUP_SIZE=CUP_SIZE): 
        self.coord_map = {}
        # map for O(1) lookups of nodes 
        initial = CupNode(0,0, CUP_SIZE)
        self.coord_map[(0,0)] = initial
        process = [initial]
        # BFS to generate tree
        while process:
            _node = process.pop(0)
            if _node.x + 1 < depth and _node.y + 1 < depth: 
                _left_coords = (_node.x+1, _node.y)
                _right_coords = (_node.x+1, _node.y+1)

                _left = self.coord_map.get(_left_coords)
                if _left is None:
                    _left = CupNode(*_left_coords, CUP_SIZE)
                    process.append(_left)
                    self.coord_map[_left_coords] = _left

                _right = self.coord_map.get(_right_coords)
                if _right is None:
                    _right = CupNode(*_right_coords, CUP_SIZE)
                    process.append(_right) 
                    self.coord_map[_right_coords] = _right
                _node.left = _left
                _node.right = _right
    
    def reset(self):
        for _cup in self.coord_map.values():
            _cup.amount = 0 

    def get_cup_amount(self, i, j):
        return self.coord_map[(i,j)].amount

    def pour(self, amount): 
        # BFS same as the construction of the tree 
        initial = self.coord_map[(0,0)]
        process = [
            (initial, amount)
        ]
        while process:
            _node, _pour = process.pop(0)
            over_flow = _node.fill(_pour)
            if over_flow > 0: 
                distribution_pour = over_flow / 2
                if _node.left:
                    process.append(
                        (_node.left, distribution_pour)
                    )
                if _node.right: 
                    process.append(
                        (_node.right, distribution_pour)
                    )








