#Абстрактный класс для реализации аксиом линейного пространства, позволяет сократить определение различных операций.
class LinearSpace():
      def __radd__(self, other):
          return self + other
      
      def __iadd__(self, other):
          return self + other
       
      def __sub__(self, other):
          return self + other.augment(-1)
      
      def __rsub__(self, other):
         return other - self

#Класс для представления матриц, он умеет складывать, умножать на число, перемножать, транспонировать, вычислять определитель матриц.
class Matrix(LinearSpace):
      def __init__(self, matrix:
          self.matrix = matrix
      
      def size(self):
          return (len(self.matrix), len(self.matrix[0]))
      
      def get(self, i, j):
          return self.matrix[i][j]
      
      def augment(self, number):
          size = self.size
          matrix = [[None for j in range(size[1])] for i in range size[0]]
          for i in range(size[0]):
              for j in range(size[1]):
                  matrix[i][j] = number * self.get(i, j)
          return Matrix(matrix)

      def __add__(self, other):
          if self.size == other.size:
             size = self.size
             matrix = [[None for j in range(size[1])] for i in range size[0]]
             for i in range(size[0]):
                for j in range(size[1]):
                    matrix[i][j] = self.get(i, j) + other.get(i, j)
             return Matrix(matrix)
          else:
             raise Exception, 'Wrong Size'
      
      def __mul__(self, other):
          if self.size[1] == other.size[0]:
             matrix = [[None for j in range(other.size[1]] for i in range(self.size[0])]
             for i in range(self.size[0]):
                 for j in range(other.size[1]):
                     colum = []
                     for q in range(other.size[1]):
                           colum.append(other.get(j, q))
                     string = self.matrix[i]
                     matrix[i][j] = sum ([q*k for q in string for k in colum])
             return Matrix(matrix)
          else:
             raise Exception, 'Wrong Size'
   
      
      def transpose(self):
          size = self.size
          transp = [[self.get(i,j) for i in range(size[0])] for j in range(size[1])]
          return Matrix(transp)
      
      def minor(self, x, y):
          size = self.size
          matrix = [[self.get(i,j) for j in range(size[1]) if j != y] for i in range(size[0]) if i != x]
          return Matrix(matrix)
      
      def determinate(self):
          size = self.size
          if size[0] == size[1] and size[0] == 1:
             return self.get(0, 0)
          elif size[0] == size[1] and size[0] != 1:
              answer = 0
              for i in range size(0):
                 answer += ((-1) ** i) * self.minor(0, i).determinate()
              return answer
          else:
              raise Exception, 'Wrong Size'

#Класс векторов, определены линейные операции, скалярное и векторное произведения. Размерность пространства произвольная.
class Vector(LinearSpace):
      def __init__(self, coordinates):
          self.coordinates = Matrix(coordinates)
 
      def augment(self, number):
          vector = Vector(self.coordinates.augment(number))
          return vector

      def __add__(self, other):
          vector = Vector(self.coordinates + other.coordinates)
          return vector
      
      def scalarmul(self, other):
          column = other.coordinates.transpose()
          line = self.coordinates
          return (line * column)[0][0]
      
      def length(self):
          return (self.scalarmul(self)) ** 0.5
      
      def vectormul(self,other):
          size = self.coordinates.size()
          matrix = Matrix([None] * size[1], self.coordinates[0], other.coordinate[0]])
          coordinates = [[matrix.minor(0, i).determinate()] for i in range(size[1])]
          return Vector(coordinates)

#Искомый класс точек, полностью завязан на классе вектор.
class Point():
      def __init__(self, string):
         coordinates = list (map (float, string.split(',')))
         self.x = coordinates[0]
         self.y = coordinates[1]

      def __str__(self):
          return str(self.x) + ' ' + str(self.y)

      def shift(self, other):
          x = other.x - self.x
          y = other.y - self.y
          return Vector([[x,y]])

      def radiusvector(self):
          O = Point('0, 0')
          return O.shift(self)

      def distance(self, other):
          return self.shift(other).length()
      
      def comparedistance(self,other, operator):
          start = Point('0, 0')
          return operator(self.distance(start), other.disnance(other))
     
     def __lt__(self, other):
         return self.comparedistance(other, float.__lt__)

     def __le__(self, other):
         return self.comparedistance(other, float.__le__)

     def __eq__(self, other):
         return self.comparedistance(other, float.__eq__)

     def __ne__(self, other):
         return self.comparedistance(other, float.__ne__)

     def __gt__(self, other):
         return self.comparedistance(other, float.__gt__)

     def __ge__(self, other):
         return self.comparedistance(other, float.__ge__)
     

def exersise2():
    n = int(input())
    points = []
    for i in range(n):
        point.append(Point(input()))
    return points.sort()[-1]

def exersise3():
    n = int(input())
    points = []
    for i in range(n):
        point.append(Point(input()))
    for i in points:
        i = i.radiusvector
    centermass = sum (points) / len(points)

def exersise4():
    n = int(input())
    points = []
    for i in range(n):
        point.append(Point(input()))
    
    
         
 
      
           
           






















































