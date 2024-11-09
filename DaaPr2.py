class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''  # Huffman code for this node

# Function to print the Huffman codes for each symbol
def printNodes(node, val=''):
    # Create a new Huffman code by appending the current node's Huffman code
    newVal = val + str(node.huff)

    # If the node has a left child, recursively call the function
    if node.left:
        printNodes(node.left, newVal)

    # If the node has a right child, recursively call the function
    if node.right:
        printNodes(node.right, newVal)

    # If it's a leaf node (no children), print the symbol and its Huffman code
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")

# Input: Number of symbols and their frequencies
num_symbols = int(input("Enter the number of symbols: "))
chars = []
freq = []

print("Enter the symbols and their frequencies:")
for i in range(num_symbols):
    symbol = input(f"Enter symbol {i+1}: ")
    frequency = int(input(f"Enter frequency of {symbol}: "))
    chars.append(symbol)
    freq.append(frequency)

# Create a list of nodes for each symbol
nodes = []
for i in range(len(chars)):
    nodes.append(Node(freq[i], chars[i]))

# Construct the Huffman Tree
while len(nodes) > 1:
    # Sort the nodes based on frequency (ascending order)
    nodes = sorted(nodes, key=lambda x: x.freq)

    # Select the two nodes with the lowest frequency
    left = nodes[0]
    right = nodes[1]

    # Assign Huffman codes (0 for left, 1 for right)
    left.huff = 0
    right.huff = 1

    # Create a new node by combining the two nodes
    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    # Remove the two nodes from the list and add the new node
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

# Print the Huffman codes
print("\nHuffman Codes:")
printNodes(nodes[0])
