#in the given task we have to print the given array in reverse order
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
for e in arr[::-1]:#specify stride and slice
    print(e,end=' ')