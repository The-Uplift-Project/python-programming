# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY A
#  2. INTEGER B
# The function will search for B inside A. Return 1 
# if B is found and 0 if B is not found. 

def search(A, B):
    for i in A:
        # if B <= i[-1]:
        if B in i:
           return 1
    return 0
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    A_rows = int(input().strip())
    A_columns = int(input().strip())

    A = []

    for _ in range(A_rows):
        A.append(list(map(int, input().rstrip().split())))

    B = int(input().strip())

    result = search(A, B)

    fptr.write(str(int(result)) + '\n')

    fptr.close()
