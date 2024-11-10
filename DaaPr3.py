def fractional_knapsack(values, weights, W):
    n = len(values)
    
    # Calculate value/weight ratio for each item
    ratios = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]
    
    # Sort items based on ratio in non-increasing order
    ratios.sort(reverse=True)
    
    total_value = 0  # Initialize total value
    current_weight = 0  # Initialize current weight
    
    # Loop through all items
    for ratio, value, weight in ratios:
        if current_weight + weight <= W:
            # Add entire item
            total_value += value
            current_weight += weight
        else:
            # Add fraction of item
            fraction = (W - current_weight) / weight
            total_value += value * fraction
            break
    
    return total_value

# Take user input
values = list(map(int, input("Enter the values of the items (space-separated): ").split()))
weights = list(map(int, input("Enter the weights of the items (space-separated): ").split()))
W = int(input("Enter the maximum weight capacity of the knapsack: "))

# Ensure values and weights lists have the same length
if len(values) != len(weights):
    print("Error: The number of values and weights must be the same.")
else:
    # Calculate maximum value in knapsack
    max_value = fractional_knapsack(values, weights, W)
    print("Maximum value in knapsack =", max_value)
    print(f"Maximum profit (by Minimum Weight): {knapsack_w(limit, arr)}")
