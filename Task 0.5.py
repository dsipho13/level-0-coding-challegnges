def area_of_triangle(x,y,r):
    semi_parameter = (x + y + r)/2 
    area = (semi_parameter * (semi_parameter - x)*(semi_parameter - y)*(semi_parameter -r) )**(0.5) # Heron's formula
    return area 

print(area_of_triangle(3,3,3))

