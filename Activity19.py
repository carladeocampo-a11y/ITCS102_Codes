isSmart = True

while isSmart == True:
    x = bool(input("Are you smart? (True / False)"))

    if x == True:
        print("Continuing Loop")
        continue
    else:
        break