def euclidgcd(a,b):
    if b==0:
        return a
    else:
        return euclidgcd(b,a%b)
a, b=list(map(int, input("Enter numbers to compute gcd: ").split()))
print(f"GCD: {euclidgcd(a,b)}")
