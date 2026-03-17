#reverse string:
def reverse_string(s):
    left, right =  0, len(s) - 1
    s=list(s)
    while left < right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return "".join(s)
    
print(reverse_string("hello"))


#find missing number:
def find_missing(arr, n):
    total=n*(n+1)//2
    sum_arr=sum(arr)
    return total - sum_arr

#check palindrome:
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left]!=s[right]:
            return False
        left +=1
        right-=1
    return True
print(is_palindrome("madam"))
print(is_palindrome("hello"))

#longest substring:
def longest_substring(s):
    char_set = set()
    left=0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left+=1

        char_set.add(s[right])
        max_length=max(max_length, right - left + 1)

    return max_length
print(longest_substring("abcabcbb"))
print(longest_substring("bbbbb"))

#maximum profit in stock trading:

def max_profit(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


# Example:
prices = [7, 1, 5, 3, 6, 4]
print("Maximum Profit:", max_profit(prices))
