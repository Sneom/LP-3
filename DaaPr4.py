# 0/1 Knapsack problem solution
def knapsack_01(n, values, weights, W):
    # Create a 2D DP array to store the maximum value at each n, w
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the DP table
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:  # Base case: no items or no capacity
                dp[i][w] = 0
            elif weights[i - 1] <= w:  # If item i can be included
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]  # Item i cannot be included

    # To find selected items
    selected_items = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # Item i is included
            selected_items.append(i - 1)  # Append the index of the selected item
            w -= weights[i - 1]

    return dp[n][W], selected_items

# Taking input from the user
n = int(input("Enter the number of items: "))  # Number of items
values = list(map(int, input("Enter the values of the items separated by space: ").split()))
weights = list(map(int, input("Enter the weights of the items separated by space: ").split()))
W = int(input("Enter the maximum capacity of the knapsack: "))  # Maximum knapsack capacity

# Getting the maximum value and selected items
max_value, selected_items = knapsack_01(n, values, weights, W)

# Output results
print("Maximum value:", max_value)
print("Selected items (0-indexed):", selected_items)
