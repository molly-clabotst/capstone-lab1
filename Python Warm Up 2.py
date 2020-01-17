numClass = input("How many classes are you taking this sememster? ")
classNames = []

print(numClass)
for num in range(0, int(numClass)):
    cless = input("Enter your class name: ")
    classNames.append(cless)

print("\nThe classes you are taking are:")
print()

for clesh in classNames:
    print(clesh)
print()