if __name__ == '__main__':
    n = int(input())
    lists = []
    lis = []
    for i in range(0, n):
        name = input()
        score = float(input())
        li = [name, score]
        lists.append(li)
    lis = lists
    lis = sorted(lis, key=lambda x: x[1])
    for i in range(0, n):
        if (lis[i][1] > lis[0][1]):
            c = lis[i][1]
            break
    lists = sorted(lists)
    for i in range(0, n):
        if (lists[i][1] == c):
            print(lists[i][0])
