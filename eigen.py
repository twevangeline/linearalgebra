import scipy as sp
import numpy as np
matrix = np.array([[4.3,8.9],[2.2,3.4]])
norm = sp.linalg.norm(matrix)
print(norm)
print(sp.square([v for row in matrix for v in row]).sum(**(0.5)))
eigvals,eigvecs = sp.linalg.eig(matrix)
print('eigenvalues =',eigvals)
print('eigenvectora = \n',eigvecs)

x = np.random.random()
Q = np.array([[np.cos(x),-np.sin(x)],[np.sin(x),np.cos(x)]])
D = np.diag((-1,1))
eigenD = np.linalg.eigvals(D)
A = np.dot(Q,D)
A = np.dot(A,Q.T)
eigenA =np.linalg.eigvals(A)

from sympy import Matrix
m = Matrix([[10,2,3],[3,12,5],[5,5,8]])
print(m.eigenvals)
print(list(map(complex,m.eigenvals().keys())))
import numpy as np
print(np.linalg.eigenvals(np.array(m.tolist(),dtype=float)))
