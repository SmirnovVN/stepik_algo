f = [0, 1]
cycle = [0, 1]


def fib_mod(n, m):
    for i in range(2, n + 1):
        buf = f[1]
        f[1] = (f[0] + f[1]) % m
        f[0] = buf
        if f[1] == 1 and cycle[-1] == 0:
            del cycle[-1]
            break
        else:
            cycle.append(f[1])
    return cycle[n % (len(cycle))]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
