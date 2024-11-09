import heapq

# Class to represent a Huffman Tree Node
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq  # Frequency of the character
        self.symbol = symbol  # The character itself
        self.left = left  # Left child
        self.right = right  # Right child
        self.huff = ""  # Huffman code for the character

    # Comparator function for priority queue (heapq)
    def __lt__(self, other):
        return self.freq < other.freq

# Function to print the Huffman codes and calculate the encoded lengths
def printNodes(node, val=""):
    new_val = val + node.huff  # Update the current Huffman code
    if node.left or node.right:  # If there are children, keep traversing
        if node.left:
            printNodes(node.left, new_val)
        if node.right:
            printNodes(node.right, new_val)
    else:
        # If it's a leaf node, print the symbol and its Huffman code
        print(f"{node.symbol} -> {new_val}")
        encoded_lengths[node.symbol] = len(new_val)

# Getting user input for characters and their frequencies
num_chars = int(input("Enter number of characters: "))
chars = []
freqs = []

for i in range(num_chars):
    char = input(f"Enter character {i + 1}: ")
    freq = int(input(f"Enter frequency of character {char}: "))
    chars.append(char)
    freqs.append(freq)

# Creating the priority queue (min heap) of nodes
nodes = []
for i in range(len(chars)):
    heapq.heappush(nodes, Node(freqs[i], chars[i]))

# Building the Huffman Tree
while len(nodes) > 1:
    left = heapq.heappop(nodes)  # Node with the lowest frequency
    right = heapq.heappop(nodes)  # Node with the second lowest frequency

    left.huff = "0"  # Assign 0 to the left child
    right.huff = "1"  # Assign 1 to the right child

    # Create a new internal node with the sum of the frequencies
    new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, new_node)

# Calculating total size before encoding
total_size_before = sum(freqs) * 8

# Printing the nodes and calculating encoded lengths
encoded_lengths = {}
print("Huffman Codes:")
printNodes(nodes[0])

# Calculating total size after encoding
total_size_after = sum(freqs[i] * encoded_lengths[chars[i]] for i in range(num_chars))

# Calculating encoded data representation (compressed size)
characters = num_chars * 8
frequency = sum(freqs)
encoded_data_representation = characters + frequency + total_size_after

# Output results
print("\nTotal size before encoding:", total_size_before, "bits")
print("Total size after encoding:", total_size_after, "bits")
print("Encoded Data Representation:", encoded_data_representation, "bits")
