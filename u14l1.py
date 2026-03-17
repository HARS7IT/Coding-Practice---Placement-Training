from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()

    freq=Counter(s)
    odd_count=0

    for count in freq.values():
        if count %  2 !=0:   
            odd_count+=1

    print(max(0, odd_count-1))
        