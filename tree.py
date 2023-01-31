'''Creating a binary tree'''
# encoding : utf8
class BinaryTree():
    '''Creating class binary tree'''
    def __init__(self):
        '''Defining initial attributes: root'''
        self.root=None
    def print_tree(self):
        '''Method allowing to build one-sided display of the tree'''
        print(self.root.display_node())
    def print_tree_facultatif(self):
        '''Method allowing to build two-sided display of the tree'''
        print(self.root.display_node_facultatif())

class Node():
    '''Creating class node'''
    def __init__(self, value):
        '''Defining initial attributes: node value and depth.
        Creating empty variables for left and right branchs'''
        self.value=value
        self.right= None
        self.left= None
        self.depth= 0

    def add(self, left = None, right = None):
        '''Method allowing to add left or right branch to existing node'''
        self.left = left
        self.right = right
        if self.left:
            left.depth = self.depth + 1
            left.update_children_depth()
        if self.right:
            right.depth = self.depth + 1
            right.update_children_depth()

    def update_children_depth(self):
        '''Method allowing to update children depth of branches'''
        if self.left:
            self.left.depth = self.depth + 1
            self.left.update_children_depth()
        if self.right:
            self.right.depth = self.depth + 1
            self.right.update_children_depth()

    def display_node(self):
        '''Method allowing to create a one-sided display of the tree according to depth of node'''
        #stocking information about the node accorting to definite in  __str__ method
        retour = str(self)
        #if right branch exists
        if self.right:
            #add to variable "retour" line break
            retour +="\n"
            #add as many tabulations as the node depth value 
            # and repeat the function for the right node
            retour +=int(self.right.depth)*"\t" + self.right.display_node()
        #if left branch exists
        if self.left:
            #add to variable "retour" line break
            retour += "\n"
            #add as many tabulations as the node depth value
            #and repeat the function for the left node
            retour +=int(self.left.depth)*"\t" + self.left.display_node()
        return retour

    def display_node_facultatif(self):
        '''Method allowing to create a two-sided display of the tree according to depth of node'''
        #Create an empty variable will contain str
        retour =""
        #if both left and right branch exists
        if self.left and self.right:
            #find the max depth of left branch and stock this value in variable
            max_depth_left=self.left.get_max_depth()
            #if the depth of the node is equal to zero
            if self.depth==0:
                #moves by as many tabulations as the max depth of the left branch
                #and retrieve information about the node
                #updating the variable retour
                retour = int(max_depth_left)*"\t"+ str(self)
            retour += "\n"
            #add to variable retour as many tabulations as the left node depth value - 1
            #retrieve information about the left node and repeat the function with left node
            #add to variable retour two tabulations
            #retrieve information about the right node and repeat the function with right node
            retour +=((int(self.left.depth)-1)*"\t" +str(self.left)
            + self.left.display_node_facultatif()
            + 2*"\t"+str(self.right) + self.right.display_node_facultatif())
            retour += "\n"
        else:
            # if right branch exists
            if self.right:
                #add to variable retour as many tabulations as the right node depth value  + 1
                #retrieve information about the right node
                #repeat the function
                retour +=(int(self.right.depth + 1)*"\t"
                +str(self.right)+ self.right.display_node_facultatif())
                #retour += "\n"
            if self.left:
                retour += "\n"
                #add to variable retour as many tabulations as the left node depth value  + 1
                #retrieve information about the left node
                #repeat the function
                retour +=((int(self.left.depth)+ 1)*"\t" +str(self.left)
                + self.left.display_node_facultatif())
                retour += "\n"
        return retour

    def __str__(self):
        '''Method allowing the string representation of an object'''
        return str(self.value) + "/" + str(self.depth)

    def is_leaf(self):
        '''Method allowing to check if self.left == None and self.right == None'''
        return not(self.left or self.right)

    def get_max_depth(self,max_depth=0):
        '''Method allowing to find the max depth
        of branch by looking for the first to the last element'''
        if self.is_leaf():
            if self.depth > max_depth:
                return self.depth
            else:
                return max_depth
        else:
            if self.right:
                max_depth = self.right.get_max_depth(max_depth)

            if self.left:
                max_depth = self.left.get_max_depth(max_depth)
            return max_depth


node1 = Node(0)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node3.add(node4)
node1.add(node2, node3)
node5.add(node6, node7)
node4.add(node5)
node7.add(node8)


tree1=BinaryTree()
tree1.root=node1

tree1.print_tree()
tree1.print_tree_facultatif()
