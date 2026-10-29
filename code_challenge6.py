a = int(input("Enter size ---> "))
z = 0
for x in range(a):
    if z != a:
        for y in range(x + 1):
            if z != a:
                z += 1
                print(z , end= " ")
            elif z == a:
                print(" ", end=" ")
        print(" ")
