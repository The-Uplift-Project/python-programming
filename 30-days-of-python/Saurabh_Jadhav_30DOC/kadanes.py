from sys import maxint
print(maxint)

max_so_far =0 
max_ending_here = 0
arr = [0,1,-1,3,4]
for i in range(len(arr)):
    max_ending_here+=arr[i]
    if max_so_far<max_ending_here:
        max_so_far=max_ending_here
    if max_ending_here<0:
        max_ending_here=0

print(max_so_far)
