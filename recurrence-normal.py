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

def main_recurrence():
    print("Custom Recurrence Relation Results")
    print("----------------------------------")
    
    n = 30
    recursive_n = min(n, 25)
    print(f"Testing with n = {recursive_n} for recursive approach (to avoid excessive runtime)")
    result_recursive = recurrence_recursive(recursive_n)
    print(f"Regular Recursion: a({recursive_n}) = {result_recursive}")
    
    print(f"Testing with n = {n} for memoization and bottom-up approaches")
    result_memo = recurrence_memoization(n)
    print(f"Top-down with Memoization: a({n}) = {result_memo}")
    
    result_bottom_up = recurrence_bottom_up(n)
    print(f"Bottom-up DP: a({n}) = {result_bottom_up}")

if __name__ == "__main__":
    main_recurrence()