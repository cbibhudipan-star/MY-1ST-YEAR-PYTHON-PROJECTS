for i in range(5):
    for j in range(4):
        if ((i in {0,2,4}) and (j in {0,1,2,3})):
            print("*",end=" ")
        elif ((i in {1,3}) and (j in {0,5})):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
