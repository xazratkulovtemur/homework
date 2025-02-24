import math

class Vector:
    def __init__(self, x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self, other):
        
        return Vector(self.x+other.x, self.y+other.y, self.z+other.x)

    def __sub__(self, other):
        
        return Vector(self.x-other.x,self.y-other.y,self.z-other.z )

    def dot_value(self, other):
        
        return self.x*other.x+self.y*other.y+self.z*other.z

    def __mul__(self, scalar):  
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def magnitude(self):
        return math.sqrt((self.x)**2 + self.y**2 + self.z**2)
    
    def normalize(self):  
        length = self.magnitude()
        if length == 0:
            return Vector(0, 0, 0)  # Prevent division by zero
        return Vector(self.x / length, self.y / length, self.z / length)
    def __str__(self):  # Fixed string representation
        return f"Vector({self.x}, {self.y}, {self.z})"
    

   
v1=Vector(2,3,4)
v2=Vector(3,4,5)
v3=v1+v2
v4=v1-v2
v5=v1 * 3
dot_value=v1.dot_value(v2)
v1_magnitude=v1.magnitude()
normalized_v1=v1.normalize()

print(f"Vector 1: {v1}, \nVector 2:{v2}\n")
print('*'*50)
print(f"Addition of Vector 1 and Vector 2: {v3}" )
print('*'*50)
print(f"Substraction of Vector 1 and Vector 2: {v4}" )
print('*'*50)
print(f"Dot product of two vectors: {dot_value}")
print('*'*50)
print(f"Scalar Multipication of two vectors: {v5}")
print('*'*50)
print(f"Magnitute of vector 1: {v1_magnitude}")
print('*'*50)
print(f"Normalization of Vector 1: {normalized_v1}")

