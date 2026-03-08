import numpy as np

# Setting N
N = 32

# Initialisng A matrix, dimension (N-1)
A = 2*np.eye(N - 1) - np.eye(N - 1, k=-1) - np.eye(N - 1, k=1)

# Extracting eigenproperties
eigvals, eigvecs = np.linalg.eig(A)

# Analytical eigenvalues for Task 2
n_vals = np.array(list(range(1, N)))
analytical_eigvals = (2 * np.sin(n_vals * np.pi / (2*N)))**2

# Sorting eigenvalues
eigvals_sorted = np.sort(eigvals)
eigvecs_sorted = np.sort(eigvecs)

# Task 2 comparison
print(f"Analytical: {analytical_eigvals}")
print(f"Numerical: {eigvals_sorted}")

# Task 3)
print(eigvecs_sorted)
