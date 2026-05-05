for row in range(9):
    for col in range(5):
        if ((row in {0,8}) and (col in {2,3})):
            print("*",end=" ")
        elif ((row in {1,7})and (col in {1,4})):
            print("*",end=" ")
        elif ((row in {2,6}) and (col in {0,4})):
            print("*",end=" ")
        elif ((row in {3,4,5}) and (col in {0})):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
