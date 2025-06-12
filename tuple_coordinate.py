#You are given a tuple of coordinates (x, y) representing a point. Write a function that returns the quadrant of the point.
def tuple_coordinate(input_tuple):
    if input_tuple[0]==0 and input_tuple[1]==0:
        return "origin"
    elif input_tuple[0]>0 and input_tuple[1]>0:
        return "first quadrant"
    elif input_tuple[0]<0 and input_tuple[1]>0:
        return "second quadrant"
    elif input_tuple[0]<0 and input_tuple[1]<0:
        return "third quadrant"
    elif input_tuple[0]>0 and input_tuple[1]<0:
        return "fourth quadrant"
print(tuple_coordinate((1,-1)))

    
    
