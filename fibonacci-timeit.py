import timeit

# 1. Regular Recursion
def fib_recursive(n):
    if n < 1:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        f_n_8 = fib_recursive(n-8) if n-8 >= 0 else 0
        return fib_recursive(n-1) + fib_recursive(n-2) - f_n_8

# 2. Top-down with Memoization
def fib_memoization(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n < 1:
        result = 0
    elif n == 1 or n == 2:
        result = 1
    else:
        f_n_8 = fib_memoization(n-8, memo) if n-8 >= 0 else 0
        result = fib_memoization(n-1, memo) + fib_memoization(n-2, memo) - f_n_8
    
    memo[n] = result
    return result

# 3. Bottom-up Dynamic Programming
def fib_bottom_up(n):
    if n < 1:
        return 0
    
    dp = [0] * max(9, n+1)
    dp[1] = 1
    dp[2] = 1
    
    for i in range(3, n+1):
        f_i_8 = dp[i-8] if i-8 >= 0 else 0
        dp[i] = dp[i-1] + dp[i-2] - f_i_8
    
    return dp[n]

def time_function(func, n, *args):
    # Create a wrapper to handle memoization's optional memo argument
    if func.__name__ == 'fib_memoization':
        stmt = f"{func.__name__}({n})"
    else:
        stmt = f"{func.__name__}({n})"
    
    # Use timeit to run the function 100 times
    setup = f"from __main__ import {func.__name__}"
    time_taken = timeit.timeit(stmt, setup=setup, number=100) / 100  # Average time per run
    result = func(n, *args)  # Run once to get the result
    return result, time_taken

def main_fibonacci():
    print("Modified Fibonacci Sequence Analysis (using timeit)")
    print("-----------------------------------")
    
    n = 30
    recursive_n = min(n, 25)
    print(f"Testing with n = {recursive_n} for recursive approach (to avoid excessive runtime)")
    result_recursive, time_recursive = time_function(fib_recursive, recursive_n)
    print(f"Regular Recursion: f({recursive_n}) = {result_recursive}, Time: {time_recursive:.6f} seconds")
    
    print(f"Testing with n = {n} for memoization and bottom-up approaches")
    result_memo, time_memo = time_function(fib_memoization, n)
    print(f"Top-down with Memoization: f({n}) = {result_memo}, Time: {time_memo:.6f} seconds")
    
    result_bottom_up, time_bottom_up = time_function(fib_bottom_up, n)
    print(f"Bottom-up DP: f({n}) = {result_bottom_up}, Time: {time_bottom_up:.6f} seconds")
    
    print("\nComparison:")
    if time_recursive < time_memo and time_recursive < time_bottom_up:
        fastest = "Regular Recursion"
    elif time_memo < time_bottom_up:
        fastest = "Top-down with Memoization"
    else:
        fastest = "Bottom-up Dynamic Programming"
    
    print(f"The fastest approach for this modified Fibonacci sequence is: {fastest}")

if __name__ == "__main__":
    main_fibonacci()