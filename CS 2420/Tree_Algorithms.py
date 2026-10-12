from Algo_and_Struts_06_i_tree_node import TreeNode

def numberOfLeaves(n :TreeNode) -> int:
    if n == None:               
        return 0    
    if n.is_leaf():             
        return 1
    return numberOfLeaves(n.left_child) + numberOfLeaves(n.right_child) # Recursively adding the leaves of each node together
	
def numberOfNodesWithASingleChild(n :TreeNode) -> int:
    if n == None:
        return 0
    nodeCount = 0
    if (n.left_child == None) != (n.right_child == None):
        nodeCount = 1
    return nodeCount + numberOfNodesWithASingleChild(n.left_child) + numberOfNodesWithASingleChild(n.right_child)

def numberOfNodesWithTwoChildren(n :TreeNode) -> int:
    if n == None:
        return 0
    if n.has_children() == True:
        nodeCount = 1
    else:
        return 0
    return nodeCount + numberOfNodesWithTwoChildren(n.left_child) + numberOfNodesWithTwoChildren(n.right_child)
	
def numberOfNodesWithEvenDataItems(n :TreeNode) -> int:
    if n == None:
        return 0
    nodeCount = 0
    if n.value % 2 == 0:
        nodeCount = 1
    return nodeCount + numberOfNodesWithEvenDataItems(n.left_child) + numberOfNodesWithEvenDataItems(n.right_child)

def sumOfAllItems(n :TreeNode)  -> int:
    if n == None:
        return 0
    return n.value + sumOfAllItems(n.left_child) + sumOfAllItems(n.right_child)

def printRuntimes():
    #TODO type in the runtimes on these lines: i.e. log(n), n, n log(n), n*n, etc
    print("BigOh runtime of numberOfLeaves is: n*n since there will always be at least 1 more child node")
    print("BigOh runtime of numberOfNodesWithOneNonNullChild is: n since it has to traverse through all of the nodes")
    print("BigOh runtime of numberOfNodesWithTwoNonNullChildren is: n since it has to traverse through all of the nodes")
    print("BigOh runtime of numberOfNodesWithEvenDataItems is: n since it has to traverse through all of the values")
    print("BigOh runtime of sumOfAllItems is: n since it also has to traverse through all of the items")
		