
import numpy as np

N = 31
A = 2*np.eye(N) - np.eye(N, k=-1) - np.eye(N, k=1)


print(A)

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)


print("  ")
print("  ")
print("  ")
print("  ")


print("Eigenvectors:")
print(eigenvectors)
