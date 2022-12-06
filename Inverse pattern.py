r = int(input("Enter number of rows you want to print: "))
for i in range(r,0,-1):
    for j in range(0,i):
        print("*",end="")
    print("\n")
