# Set in Python 
# HackerRank : https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
def average(array):
    # your code goes here
    per_set = set(array)
    s = sum(per_set)/len(per_set)
    return(s)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
