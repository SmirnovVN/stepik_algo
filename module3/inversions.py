def count(a):
    count_merge(a, 0, len(a) - 1)
    return res


def count_merge(a, left, right):
    if left < right:
        m = (left + right) // 2
        return merge(count_merge(a, left, m), count_merge(a, m + 1, right))
    else:
        return [a[left]]


def merge(l1, l2):
    global res
    i = j = 0
    merged = []
    while i < len(l1) or j < len(l2):
        if i < len(l1):
            if j < len(l2) and l1[i] > l2[j]:
                merged.append(l2[j])
                j += 1
                res += len(l1) - i
            else:
                merged.append(l1[i])
                i += 1
        elif j < len(l2):
            if i < len(l1) and l1[i] <= l2[j]:
                merged.append(l1[i])
                i += 1
            else:
                merged.append(l2[j])
                j += 1
    return merged


def main():
    _ = input()
    a = list(map(int, input().split()))
    print(count(a))


if __name__ == "__main__":
    res = 0
    main()
