# Brute Force (recursive)
def knapsack_brute_force(weights, values, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    
    if weights[n-1] > capacity:
        return knapsack_brute_force(weights, values, capacity, n-1)
    
    # Take or don't take the item
    return max(
        values[n-1] + knapsack_brute_force(weights, values, capacity - weights[n-1], n-1),
        knapsack_brute_force(weights, values, capacity, n-1)
    )

# Example
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
n = len(weights)
print("Brute Force:", knapsack_brute_force(weights, values, capacity, n))

# Dynamic Programming (0/1 Knapsack)
def knapsack_dp(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
    
    return dp[n][capacity]

# Example
print("Dynamic Programming:", knapsack_dp(weights, values, capacity))

# Greedy Approach (Fractional Knapsack)
def fractional_knapsack(weights, values, capacity):
    items = sorted(zip(weights, values), key=lambda x: x[1]/x[0], reverse=True)
    total_value = 0
    
    for weight, value in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += (value / weight) * capacity
            break
    
    return total_value

# Example
print("Fractional Knapsack (Greedy):", fractional_knapsack(weights, values, capacity))

# Unbounded Approach (DP)
def unbounded_knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for w in range(capacity + 1):
        for i in range(n):
            if weights[i] <= w:
                dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    
    return dp[capacity]

# Example
print("Unbounded Knapsack:", unbounded_knapsack(weights, values, capacity))
