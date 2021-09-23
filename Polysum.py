import math

def polysum(n, s):
   """
   Input: n -> number of sides.
          s -> length of each side.
   Output: Returns the sum of Polygons area
           and square of the perimeter 
   """

   areaOfPolygon = (0.25*n*s**2)/math.tan(math.pi/n)
   perimeterOfPolygon = n*s

   # sum the area and square of the perimeter
   sum = areaOfPolygon + perimeterOfPolygon**2
   
   return round(sum, 4)