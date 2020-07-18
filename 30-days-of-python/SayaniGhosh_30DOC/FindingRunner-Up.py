if __name__ == '__main__':
    n = int(input())
    arr = []
    arr = input().split()

    for i in range(0, n):
        arr[i] = int(arr[i])
    arr = sorted(arr)
    for i in range(0, n):
        if (arr[i] == max(arr)):
            c = i
            break
    print(arr[c - 1])
