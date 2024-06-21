def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome(n):
    n_str = str(n)
    length = len(n_str)
    half_len = (length + 1) // 2
    first_half = n_str[:half_len]
    if length % 2 == 0:
        palindrome_candidate = first_half + first_half[::-1]
    else:
        palindrome_candidate = first_half + first_half[-2::-1]
    if int(palindrome_candidate) > n:
        return int(palindrome_candidate)
    first_half = str(int(first_half) + 1)
    if length % 2 == 0:
        palindrome_candidate = first_half + first_half[::-1]
    else:
        palindrome_candidate = first_half + first_half[-2::-1]

    return int(palindrome_candidate)

def nearest_high_palindrome(n):
    if is_palindrome(n):
        return n
    else:
        return next_palindrome(n)
n = int(input())
print(nearest_high_palindrome(n))
