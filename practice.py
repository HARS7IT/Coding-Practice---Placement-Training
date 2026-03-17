def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter the number: "))
print(factorial(n))



def check_palindrome(s,start,end):
    if s[start]>=s[end]:
        return True
    if s[start]!=s[end]:
        return False
    return check_palindrome(s,start+1,end-1)
s=str(input("Enter the string:"))
print(check_palindrome(s,s[start],s[end]))