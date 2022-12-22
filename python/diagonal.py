def countOfUniqueDirectPaths(numberOfSpots):
    n = numberOfSpots
    if(n<=2):
        print("Invalid input")
    else:
        unique = n + (n*(n-3)/2)
        print (int(unique))
countOfUniqueDirectPaths(4)