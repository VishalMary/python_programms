def isprime(n):
    if (n==1):
        return 1
    if (n==2):
        return 1
    for i in range(2,n//2):
        if n%i==0:
            return 0
    return 1
a=int(input())
for i in range(1,a//2):
    if(isprime(i) and isprime(a-i)):
        print("yes")
        break
    else:
        print("No")
