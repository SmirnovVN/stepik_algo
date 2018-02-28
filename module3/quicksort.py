import random


def quicksort(a):
    def partition(left, right):
        m = random.randint(left, right - 1)
        a[m], a[left] = a[left], a[m]
        j = left
        x = a[left]
        for i in range(left + 1, right):
            if a[i] < x:
                j += 1
                a[i], a[j] = a[j], a[i]
        a[left], a[j] = a[j], a[left]
        return j

    def _quicksort(left, right):
        while left < right:
            m = partition(left, right)
            if m - left < right - m:
                _quicksort(left, m - 1)
                left = m + 1
            else:
                _quicksort(m + 1, right)
                right = m - 1
        return a
    return _quicksort(0, len(a))


def main():
    _ = input()
    a = list(map(int, input().split()))
    print(" ".join(map(str, quicksort(a))))


if __name__ == "__main__":
    main()
