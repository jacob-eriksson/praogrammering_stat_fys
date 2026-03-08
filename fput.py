import numpy as np

# Parameters
N = 32
dt = np.sqrt(1/8)
N_t = 50000
K = M = 1

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
print(f"Analytical: {analytical_eigvals[:4]}...\n")
print(f"Numerical: {eigvals_sorted[:4]}...")

# Defining force function (Task 3)
def f(u, alpha):
    n = len(u) - 1
    F = np.zeros_like(u)
    F[1] = u[2] - 2*u[1] + alpha*(u[2] - u[1])**2 - alpha*u[1]**2
    for i in range(2, n-1):
        F[i] = u[i+1] - 2*u[i] + u[i-1] + alpha*(u[i+1]-u[i])**2 - alpha*(u[i]-u[i-1])**2
    F[n-1] = -2*u[n-1] + u[n-2] + alpha*u[n-1]**2 - alpha*(u[n-1]-u[n-2])**2
    return F

# Defining energy function 
def e(u, v, eigenvecs, eigenvals):

    # Linear part (H_0)
    Q = eigenvecs.T @ u
    P = eigenvecs.T @ v
    E0 = 0.5 * np.sum(P**2 + eigenvals * Q**2)

    # Non-linear part (H_1)
