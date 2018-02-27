import heapq


def main():
    n = int(input())
    h = []
    heapq.heapify(h)
    for i in range(n):
        op = input()
        if op.find("Insert") == 0:
            _, x = op.split()
            heapq.heappush(h, -int(x))
        elif op.find("ExtractMax") == 0:
            print(-heapq.heappop(h))


if __name__ == "__main__":
    main()
