from functools import lru_cache


def edit_distance(s1, s2):
    @lru_cache(maxsize=None)
    def d(i, j):
        if i == 0 or j == 0:
            return max(i, j)
        else:
            return min(d(i, j - 1) + 1,
                       d(i - 1, j) + 1,
                       d(i - 1, j - 1) + (s1[i - 1] != s2[j - 1]))

    return d(len(s1), len(s2))


def main():
    s1 = input()
    s2 = input()
    print(edit_distance(s1, s2))


if __name__ == "__main__":
    main()
