def triangleArea(x,y,r):
    semiparam = (x + y + r)/2 
    area = (semiparam * (semiparam - x)*(semiparam - y)*(semiparam -r) )**(0.5) # calculate the aread
    return area 

print(triangleArea(3,3,3))

