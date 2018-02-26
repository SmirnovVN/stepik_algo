def gcd(a, b):
    if a > b > 0:
        return gcd(a % b, b)
    elif b > a > 0:
        return gcd(b % a, a)
    else:
        return a if b == 0 else b


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
