""" 
Find an Euclidian distance between (2, 3) and (10, 8)

"""

x1 = 2
x2 = 10 

y1 = 3 
y2 = 8 

d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(round(d, 3))
print(round(d, 1))

''' 
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.

'''
r = float(input('Enter the circle radius: '))
print(r)
pi = 3.14
area_of_circle = pi * r ** 2 
print('The area of the circle is ', round(area_of_circle, 2))

circum_of_circle = 2 * pi * r

print('The circumference of the circle is ', round(circum_of_circle, 2))

""" 
Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
"""

b = float(input('Enter base: '))
h = float(input('Enter height: '))

area = 0.5 * b * h
print('The area of the triangle is', area)