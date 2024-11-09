# 0/1 Knapsack problem solution
def knapsack_dp(values, weights, capacity):
    n = len(values)

    print("Values:", values)
    print("Weights:", weights)
    print("Capacity:", capacity)

    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:

                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


capacity = int(input("Enter the knapsack capacity: "))
n = int(input("Enter the number of items: "))
values = []
weights = []
for i in range(n):
    value = int(input(f"Enter value for item {i+1}: "))
    weight = int(input(f"Enter weight for item {i+1}: "))
    values.append(value)
    weights.append(weight)


max_value = knapsack_dp(values, weights, capacity)
print(f"The maximum value the knapsack can hold is: {max_value}")
