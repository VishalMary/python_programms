def reversef(n,rev):
    if(n==0):
        return rev
    rev=(rev*10)+(n%10)
    return reversef(n//10,rev)
    
n=int(input())
check=reversef(n,0)
if(n==check):
    print("palindrome")
else:
    print("not palindrome")