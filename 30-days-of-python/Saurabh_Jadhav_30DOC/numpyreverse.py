import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr.reverse()
    
    num_arr = numpy.array(arr,float)
    #print(num_arr)
    return num_arr
arr = input().strip().split(' ')
result = arrays(arr)
print(result)