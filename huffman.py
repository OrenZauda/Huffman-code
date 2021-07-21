# A Huffman Tree Node
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq
 
        # symbol name (charecter)
        self.symbol = symbol
 
        # node left of current node
        self.left = left
 
        # node right of current node
        self.right = right
 
        # tree direction (0/1)
        self.huff = ''
 
# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree
 
 
def printNodes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.huff)
 
    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
 
        # if node is edge node then
        # display its huffman code
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")
 
 
# charecters for huffman tree
chars = ['aleph','bet','gimel','dalet','hey','vav','zain','het','tet','yood','kaff','lamed','mem','noon',
'sameh','ayin','peh','tzadik','koof','resh','shin','taf']
 
# frequency of charecters
freq = [ 6.34, 4.74, 1.3, 2.59, 10.87, 10.38,1.33,2.48,1.24,11.06,3.51,7.39,7.62,3.96,1.48,3.23,1.96,1.34,2.14,
5.61,4.41,5.01]
 
# list containing unused nodes
nodes = []
 
# converting ccharecters and frequencies
# into huffman tree nodes
for x in range(len(chars)):
    nodes.append(node(freq[x], chars[x]))
 
while len(nodes) > 1:
    # sort all the nodes in ascending order
    # based on theri frequency
    nodes = sorted(nodes, key=lambda x: x.freq)
 
    # pick 2 smallest nodes
    left = nodes[0]
    right = nodes[1]
 
    # assign directional value to these nodes
    left.huff = 0
    right.huff = 1
 
    # combine the 2 smallest nodes to create
    # new node as their parent
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
 
    # remove the 2 nodes and add their
    # parent as new node among others
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)
 
# Huffman Tree is ready!
printNodes(nodes[0])
