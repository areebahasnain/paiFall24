import math

def areaOfTrapezoid(a, b, h):
    return 0.5*(a+b)*h

def areaOfParallelogram(base, height):
    return base*height

def SurfaceAreaOfcylinder(radius, height):
    return (2*math.pi*radius*height) + (2*math.pi*radius*radius)

def VolumeOfCylinder(radius, height):
    return math.pi*radius*radius*height

print("Area of Trapezoid: ",areaOfTrapezoid(2,3,5))
print("Area of Paralleogram: ", areaOfParallelogram(4,5))
print("Surface Area of Cylinder: ", SurfaceAreaOfcylinder(3,6))
print("Volume of Cylinder: ", VolumeOfCylinder(3,6))

