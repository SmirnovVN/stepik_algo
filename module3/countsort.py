def countsort(a):
    b = [0]*11
    res = [0]*len(a)
    for i in range(len(a)):
        b[a[i]] += 1
    for i in range(1, 11):
        b[i] += b[i - 1]
    for i in range(len(a)-1, -1, -1):
        res[b[a[i]]-1] = a[i]
        b[a[i]] -= 1
    return res


def main():
    _ = input()
    a = list(map(int, input().split()))
    print(" ".join(map(str, countsort(a))))


if __name__ == "__main__":
    main()
