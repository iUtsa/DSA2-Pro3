import timeit

# 1. Regular Recursion
def recurrence_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return recurrence_recursive(n-1) + 2 * recurrence_recursive(n-2) + 6 * n - 6

# 2. Top-down with Memoization
def recurrence_memoization(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n == 1 or n == 2:
        result = 1
    else:
        result = recurrence_memoization(n-1, memo) + 2 * recurrence_memoization(n-2, memo) + 6 * n - 6
    
    memo[n] = result
    return result

# 3. Bottom-up Dynamic Programming
def recurrence_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + 2 * dp[i-2] + 6 * i - 6
    
    return dp[n]

def time_function(func, n, *args):
    # Create a wrapper to handle memoization's optional memo argument
    if func.__name__ == 'recurrence_memoization':
        stmt = f"{func.__name__}({n})"
    else:
        stmt = f"{func.__name__}({n})"
    
    # Use timeit to run the function 100 times
    setup = f"from __main__ import {func.__name__}"
    time_taken = timeit.timeit(stmt, setup=setup, number=100) / 100  # Average time per run
    result = func(n, *args)  # Run once to get the result
    return result, time_taken

def main_recurrence():
    print("Custom Recurrence Relation Analysis (using timeit)")
    print("----------------------------------")
    
    n = 30
    recursive_n = min(n, 25)
    print(f"Testing with n = {recursive_n} for recursive approach (to avoid excessive runtime)")
    result_recursive, time_recursive = time_function(recurrence_recursive, recursive_n)
    print(f"Regular Recursion: a({recursive_n}) = {result_recursive}, Time: {time_recursive:.6f} seconds")
    
    print(f"Testing with n = {n} for memoization and bottom-up approaches")
    result_memo, time_memo = time_function(recurrence_memoization, n)
    print(f"Top-down with Memoization: a({n}) = {result_memo}, Time: {time_memo:.6f} seconds")
    
    result_bottom_up, time_bottom_up = time_function(recurrence_bottom_up, n)
    print(f"Bottom-up DP: a({n}) = {result_bottom_up}, Time: {time_bottom_up:.6f} seconds")
    
    print("\nComparison:")
    if time_recursive < time_memo and time_recursive < time_bottom_up:
        fastest = "Regular Recursion"
    elif time_memo < time_bottom_up:
        fastest = "Top-down with Memoization"
    else:
        fastest = "Bottom-up Dynamic Programming"
    
    print(f"The fastest approach for this custom recurrence relation is: {fastest}")

if __name__ == "__main__":
    main_recurrence()