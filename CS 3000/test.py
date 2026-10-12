def memoized_cut_rod(p, n):
    """
    Returns the maximum revenue for a rod of length n
    p: list of prices where p[i] is the price of a rod of length i (1-based indexing)
    n: rod length
    """
    # Initialize memoization array with -1 (meaning "not computed yet")
    r = [-1] * (n + 1)
    
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]  # Return cached value
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1, n + 1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q
    print(q)
    return q 


# Example usage:
# Prices for rods of length 1..10 (1-based indexing)
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  # p[0] is unused
n = 10
max_revenue = memoized_cut_rod(prices, n)
print("Maximum revenue for rod of length", n, "is", max_revenue)