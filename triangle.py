import math
def Triangle(a,b,c):
   cos_C=(a**2+b**2-c**2)/(2*a*b)
   cos_A=(b**2+c**2-a**2)/(2*b*c)
   cos_B=(a**2+c**2-b**2)/(2*a*c)
   A_radius = math.cos(cos_A)
   B_radius = math.cos(cos_B)
   C_radius = math.cos(cos_C)
    
   A_deg = math.degrees(A_radius)
   B_deg = math.degrees(B_radius)
   C_deg = math.degrees(C_radius)
    
   return A_deg, B_deg, C_deg
   
print(Triangle(2,8,4))