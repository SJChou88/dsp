# Matrix Algebra

import numpy as np

A = np.matrix('1 2 3; 2 7 4')
B = np.matrix('1 -1; 0 1')
C = np.matrix('5 -1; 9 1; 6 0')
D = np.matrix('3 -2 -1; 1 2 3')
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([[1],
             [8],
             [0],
             [5]])

#1.1) 2x3
#1.2) 2x2
#1.3) 3x2
#1.4) 2x3
#1.5) 1x4
#1.6) 4x1

a = 6

print(u + v)
#2.1) [9 7 -4 9]

print(u -v)
#2.2) [3 -3 -2 1]

print (a * u)
#2.3) [36 12 -18 30]

print(np.dot(u,v))
#2.4) 51

print(np.linalg.norm(u))
#2.5) 8.60232526704

#print(A + C)
#3.1) not defined

print(A - np.transpose(C))
#3.2) [[-4 -3 -3] [3 6 4]]

print(np.transpose(C) + 3 * D)
#3.3) [[14 3 3] [2 7 9]]

print(B*A)
#3.4) [[-1 -5 -1] [2 7 4]]

#print(B* np.transpose(A))
#3.5) not defined


