score=int(input("Enter your score: "))

if max(score,80) == score and min(score,100) == score:
    print("A grade")

elif max(score,60) == score and min(score,80) == score:
    print("B grade")

elif max(score,40) == score and min(score,60) == score:
    print("C grade")

else:
    print("Fail")
