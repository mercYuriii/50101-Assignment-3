# Problem 6
# 
# Yuri Carreira Alflen

# Import math to more easily calc square roots
import math

# open and read file
file = open("points.txt","r")

# count lines
lines = len(file.readlines())

# create lists that will contain properties of each point
point_name = []
x = []
y = []
z = []

# allow file to be reread to we can loop through lines
file.seek(0)

# loop through file lines to collect point data
for line in range(lines):
    # get all properties of point into list
    point = file.readline().split(",")
    # assign each property to it's appropriate bin. ensure correct formatting (strings are strings and floats are floats)
    point_name.append(point[0].strip())
    x.append(float(point[1].strip()))
    y.append(float(point[2].strip()))
    z.append(float(point[3].strip()))

# print(point_name) - TEST
# print(z) - TEST

# Find point closest to origin
# Distance from the origin can be rewritten as sqrt(x^2 + y^2 + z^2) for the given point since the other point be are referencing is 0,0,0
# So the point closest to the origin will have the smallest value when run through that calculation

# Assume the first point is the closest to orgin until proven otherwise in the loop
closest_to_origin = point_name[0]
base_value = math.sqrt(x[0]**2+y[0]**2+z[0]**2)
#print(base_value) - TEST math

for position in range(len(point_name)):
    value = math.sqrt(x[position]**2+y[position]**2+z[position]**2)
    if value < base_value:
        closest_to_origin = point_name[position]
        base_value = value
print(closest_to_origin + ' is the closest point to the origin')

# we now need to find which points are closes to eachother
# in hindsight it likely would have been more efficient to have created one function and used to in both the closest to origin and closest to each other, but I'm short on time
# this may take me longer so skipping the other half of this problem.
    