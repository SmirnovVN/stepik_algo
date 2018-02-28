def binary(lines, i):
    left, right = 0, len(lines) - 1
    while left <= right:
        m = (left + right) // 2
        if (m + 1 < len(lines) and lines[m][0] <= i < lines[m + 1][0]) or (
                            m + 1 == len(lines) and lines[m][0] <= i):
            return m + 1
        elif lines[m][0] > i:
            right = m - 1
        else:
            left = m + 1
    return 0


def binary2(lines, i):
    left, right = 0, len(lines) - 1
    while left <= right:
        m = (left + right) // 2
        if (m + 1 < len(lines) and lines[m][1] >= i > lines[m + 1][1]) or (
                            m + 1 == len(lines) and lines[m][1] >= i):
            return len(lines) - m - 1
        elif lines[m][1] < i:
            right = m - 1
        else:
            left = m + 1
    return len(lines)


def cover(lines, points):
    lines = sorted(lines, key=lambda x: x[0])
    res = [0] * len(points)
    for i in range(len(points)):
        res[i] = binary(lines, points[i])
    lines = sorted(lines, key=lambda x: x[1], reverse=True)
    for i in range(len(points)):
        res[i] -= binary2(lines, points[i])
    return res


def main():
    n, m = map(int, input().split())
    o = []
    for i in range(n):
        o.append(list(map(int, input().split())))
    d = list(map(int, input().split()))
    print(" ".join(map(str, cover(o, d))))


if __name__ == "__main__":
    main()
