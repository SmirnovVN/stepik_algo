def main():
    length_a, *a = map(int, input().split())
    length_b, *b = map(int, input().split())

    def binary(i):
        left, right = 0, len(a) - 1
        while left <= right:
            m = (left + right) // 2
            if (m + 1 < len(a) and a[m] <= i <= a[m + 1]) or (m + 1 == len(a) and a[m] <= i):
                return m
            elif a[m] > i:
                right = m - 1
            else:
                left = m + 1
        return -1
    print(" ".join(map(str, map(binary, b))))


if __name__ == "__main__":
    main()
