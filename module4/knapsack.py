def knapsack(w, g):
    n = len(g)
    d = [[0] * (n + 1) for _ in range(w + 1)]
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            d[j][i] = d[j][i-1]
            if g[i-1] <= j:
                d[j][i] = max(d[j][i], d[j - g[i-1]][i - 1] + g[i-1])
    return d[w][n]


def main():
    w, n = map(int, input().split())
    g = list(map(int, input().split()))
    print(knapsack(w, g))


if __name__ == "__main__":
    main()
