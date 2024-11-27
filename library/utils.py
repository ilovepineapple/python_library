def is_palindrome(string):
    return string == string[::-1]

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
