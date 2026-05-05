for i in range(7):
    for j in range(8):
        if ((i in {0,6}) and (j in {0,6})):
            print("*",end=" ")
        elif ((i in {1}) and (j in {0,1,5,6})):
            print("*",end=" ")
        elif ((i in {1}) and (j in {0,2,4,6})):
            print("*",end=" ")
        elif ((i in {2}) and (j in {0,3,6})):
            print("*",end=" ")
        elif ((i in {3}) and (j in {0,3,6})):
            print("*",end=" ")
        elif ((i in {4,5,6}) and (j in {0,6})):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 
