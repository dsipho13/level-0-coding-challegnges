def area_of_triangle(x,y,r):
    s = (x + y + r)/2 # find the semi-perimeter
    area = (s * (s - x)*(s - y)*(s -r) )**(0.5) # calculate the aread
    return area 

print(area_of_triangle(3,3,3))

