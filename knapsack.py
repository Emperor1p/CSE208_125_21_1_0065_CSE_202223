def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a table to store the max values for each capacity and item
    table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    # Build the table using bottom-up dynamic programming
    for i in range(1, n+1):
        for j in range(1, capacity +1):
            if weights[i - 1] > j:
                #if the current items's weight is greater than the remaining capacity,take the previous item's value for the same capacity
                table[1][j] = table[i - 1][j]
            else:
                #Take the max of including or excluding the curr item
                table[i][j] = max(table[i -1][j], values[i - 1] + table[i -1][j - weights[i -1]])
        #Fing the item included in the knapsack
    include_item =[]
    i, j = n, capacity
    while i > 0 and j > 0:
        if table[i][j] != table[i -1][j]:
            include_item.append(i -1)
            j -= weights[i -1]
        i -= 1
        #Return the max value and the included items
    return table[n][capacity], include_item[::-1]
    #Example usage
weights = [2, 3, 4, 5, 6, 7 ]
values = [3, 4, 5, 6, 8, 10, 12]
capacity = 20
max_value, included_items = knapsack(weights, values, capacity)
print("Maximum value is:", max_value)
print("Included items is:", included_items)
