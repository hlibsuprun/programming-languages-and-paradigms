# Procedural - Dynamic Programming

def dynamic_knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    max_value = dp[n][capacity]
    w = capacity
    selected_items = []

    for i in range(n, 0, -1):
        if max_value != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
            max_value -= values[i - 1]

    return dp[n][capacity], selected_items


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
max_value, items = dynamic_knapsack(weights, values, capacity)
print("Maximal value (Procedural):", max_value)
print("Selected items (Procedural):", items)


# Functional - Recursive

def functional_knapsack(weights, values, capacity):
    def recursive_knapsack(n, remaining_capacity):
        if n == 0 or remaining_capacity == 0:
            return 0, []

        if weights[n - 1] > remaining_capacity:
            return recursive_knapsack(n - 1, remaining_capacity)

        value_without, items_without = recursive_knapsack(n - 1, remaining_capacity)

        value_with, items_with = recursive_knapsack(n - 1, remaining_capacity - weights[n - 1])
        value_with += values[n - 1]
        items_with = items_with + [n - 1]

        if value_with > value_without:
            return value_with, items_with
        else:
            return value_without, items_without

    max_value, selected_items = recursive_knapsack(len(weights), capacity)
    return max_value, selected_items


max_value, items = functional_knapsack(weights, values, capacity)
print("Maximal value (Functional):", max_value)
print("Selected items (Functional):", items)
