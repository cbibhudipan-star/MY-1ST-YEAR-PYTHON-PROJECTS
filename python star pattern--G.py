for i in range(8):
    for j in range(6):
        if ((i in {0}) and (j in {2,3})):
            print("*",end=" ")
        elif ((i in {1}) and (j in {1,4})):
              print("*",end=" ")
        elif ((i in {2}) and (j in {0,5})):
              print("*",end=" ")
        elif ((i in {3}) and (j in {0})):
              print("*",end=" ")
        elif ((i in {4}) and (j in {0,3,4,5})):
              print("*",end=" ")
        elif ((i in {5}) and (j in {0,3,5})):
              print("*",end=" ")
        elif ((i in {6}) and (j in {1,3,5})):
              print("*",end=" ")
        elif ((i in {7}) and (j in {2,5})):
              print("*",end=" ")
        else:
              print(" ",end=" ")
    print()
