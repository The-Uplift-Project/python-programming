def fibseries(n):
    arr=[0,1]

    while len(arr) < n+1:
        arr.append(0)
    
    if n==1 or n==0:
        return n
    else:
        if arr[n-2] ==0:
            arr[n-2] =fibseries(n-2)
        if arr[n-1] ==0:
            arr[n-1] =fibseries(n-1)
        
    arr[n] = arr[n-1] + arr[n-2]
    return arr[n]

n=int(input())
print(fibseries(n))