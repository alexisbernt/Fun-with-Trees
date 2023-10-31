class Tree:
    class Position:
        # abstraction representing the location of a single element
        def element(self):
            # return the element stored at the position
            raise NotImplementedError('must be implemented by subclass')
        def __eq__(self, other):
            # Return true if other Position represents the same location
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            # Return True if other does not represent the same location
            return not (self == other) # opposite of __eq__

        def root(self):
            raise NotImplementedError('must be implemented by sublcass')

        def parent(self, p):
            # return Position representing p's parent (or None if p is the root)
            raise NotImplementedError('must be implemented by subclass')

        def num_children(self, p):
            # return the number of children that Position p has 
            raise NotImplementedError('must be implemented by subclass')

        def chilren(self, p):
            # Generate an itertion of Positions representing p's children
            raise NotImplementedError('must be implemented by subclass')

        def __len__(self):
            # return the total amount of elements in the tree (total number of elements)
            raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        # Return True if Position p represents the root of the tree 
        return self.root() == p

    def is_leaf(self, p):
        # Return True if Position p does not have any children
        return self.num_children(p) == 0

    def is_empty(self):
        # Return True if the tree is empty
        return len(self) == 0 
          
A) Give a direct implementation of the num children method within the class BinaryTree.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
class BinaryTree(Tree):

    def 

B) Implement the binary tree ADT using the array-based representation.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # Trees can be represented as (1) Dynamic Node Representation (Linked Representation) (2) Array Representation (Sequential Representation)
# Implementation of tree using array
# Numbering starts from 0 to n-1
tree = [None] * 8

def root(key):
    if tree[0] != None:
        print('The tree already had a root') 
    else:
        tree[0] = key 

def set_left(key, parent):
    tree[(parent * 2) + 1] = key 
        
