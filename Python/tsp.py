import math

def tsp(mask, pos, n, dist, dp):
    if mask == (1 << n) - 1:
        return dist[pos][0]
    
    if dp[mask][pos] != -1:
        return dp[mask][pos]
    
    min_cost = math.inf
    for city in range(n):
        if (mask & (1 << city)) == 0:
            new_cost = dist[pos][city] + tsp(mask | (1 << city), city, n, dist, dp)
            min_cost = min(min_cost, new_cost)
    
    dp[mask][pos] = min_cost
    return dp[mask][pos]

def solve_tsp(dist):
    n = len(dist)
    dp = [[-1] * n for _ in range(1 << n)]
    return tsp(1, 0, n, dist, dp)

if __name__ == "__main__":
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    result = solve_tsp(dist)
    print(f"Minimum cost of visiting all cities: {result}")
