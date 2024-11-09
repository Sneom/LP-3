class Item:
    def __init__(self, pro, wt):
        self.pro = pro
        self.wt = wt

def knapsack(limit, arr):
    arr_copy = arr[:]
    arr_copy.sort(key=lambda x: (x.pro / x.wt), reverse=True)  # Max Profit/Weight
    total = 0.0
    for i in arr_copy:
        if i.wt <= limit:
            limit -= i.wt
            total += i.pro
        else:
            total += (i.pro * limit) / i.wt
            break
    return total

def knapsack_p(limit, arr):
    arr_copy = arr[:]
    arr_copy.sort(key=lambda x: (x.pro), reverse=True)  # Max profit
    total = 0.0
    for i in arr_copy:
        if i.wt <= limit:
            limit -= i.wt
            total += i.pro
        else:
            total += (i.pro * limit) / i.wt
            break
    return total

def knapsack_w(limit, arr):
    arr_copy = arr[:]
    arr_copy.sort(key=lambda x: (x.wt))  # Min Weight
    total = 0.0
    for i in arr_copy:
        if i.wt <= limit:
            limit -= i.wt
            total += i.pro
        else:
            total += (i.pro * limit) / i.wt
            break
    return total

if __name__ == "__main__":
    limit = float(input("Enter the knapsack limit: "))
    num_items = int(input("Enter the number of items: "))
    arr = []

    for i in range(num_items):
        pro = float(input(f"Enter profit for item {i+1}: "))
        wt = float(input(f"Enter weight for item {i+1}: "))
        arr.append(Item(pro, wt))

    print(f"Maximum profit (by Profit/Weight ratio): {knapsack(limit, arr)}")
    print(f"Maximum profit (by Profit): {knapsack_p(limit, arr)}")
    print(f"Maximum profit (by Minimum Weight): {knapsack_w(limit, arr)}")
