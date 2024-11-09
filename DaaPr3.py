class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalknapsack(w, arr):
    # Sort items by profit-to-weight ratio in decreasing order
    arr.sort(key=lambda x: x.profit / x.weight, reverse=True)
    
    final_value = 0.0  # Variable to store the total value in knapsack
    
    for item in arr:
        if w >= item.weight:
            # Take the whole item
            final_value += item.profit
            w -= item.weight
        else:
            # Take the fraction of the item that fits
            final_value += item.profit * (w / item.weight)
            break

    return final_value

if __name__ == "__main__":
    n = int(input("Enter number of items:\n"))
    
    arr = []
    for i in range(n):
        profit = int(input("Enter profit of item " + str(i+1) + ":\n"))
        weight = int(input("Enter weight of item " + str(i+1) + ":\n"))
        arr.append(Item(profit, weight))
    
    w = int(input("Enter capacity of knapsack:\n"))

    print("Maximum value in knapsack:", fractionalknapsack(w, arr))
