a = [1, -1, -2, 2, 3, -4]

n = len(a)
left = 0
right = n-1

while left <= right:
    if a[left]<0 and a[right]<0:
        left+=1
    elif a[left]>0 and a[right]<0:
        a[left], a[right] = a[right], a[left]
        left+=1
        right-=1
    elif a[left]>0 and a[right]<0:
        right-=1
    else:
        left+=1
        right-=1
print(a)