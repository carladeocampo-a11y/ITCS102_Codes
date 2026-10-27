for x in range (5):
    for y in range (5):
        if x + y == 5 -1 or y == x:
            print("*" , end="")
        else:
            print(" " , end="")
    print()

n = int(input("Input size of x"))
for c in range (n):
    for a in range (n):
        if c + a == n -1 or a == c:
            print("*" , end="")
        else:
            print(" ", end="")
    print()
    