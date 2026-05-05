for i in range(7):
    for j in range(4):
        if ((i in {0,3}) and (j in {0,1,2,3})):
            print("*",end=" ")
        elif((i in {1,2,4,5,6}) and (j in {0})):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
