match = 1

india_total = 0
england_total = 0
australia_total = 0

while match <= 3:
    print(f"\nMatch", match)

    india = int(input("Enter India's score: "))
    england = int(input("Enter England's score: "))
    australia = int(input("Enter Australia's score: "))

    india_total += india
    england_total += england
    australia_total += australia

    match += 1

print("\n--- Total Scores ---")
print("India:", india_total)
print("England:", england_total)
print("Australia:", australia_total)

# Finding max score
if india_total > england_total and india_total > australia_total:
    print("\nIndia has the highest score.")
elif england_total > india_total and england_total > australia_total:
    print("\nEngland has the highest score.")
elif australia_total > india_total and australia_total > england_total:
    print("\nAustralia has the highest score.")
else:
    print("\nTwo or more teams have equal highest score.")
