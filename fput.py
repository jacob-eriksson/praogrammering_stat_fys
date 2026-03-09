import numpy as np

# Parameters
N = 32

# Initialisng A matrix, dimension (N-1)
A = 2*np.eye(N - 1) - np.eye(N - 1, k=-1) - np.eye(N - 1, k=1)

# Extracting eigenproperties
eigvals, eigvecs = np.linalg.eigh(A)
idx = np.argsort(eigvals)
eigvals = eigvals[idx]
eigvecs = eigvecs[:,idx]

# Analytical eigenvalues for Task 2
n_vals = np.array(list(range(1, N)))
analytical_eigvals = (2 * np.sin(n_vals * np.pi / (2*N)))**2

# Task 2 comparison
print(f"Analytical: {analytical_eigvals[:4]}...\n")
print(f"Numerical: {eigvals[:4]}...")

# Defining force function (Task 3)
def f(u, alpha):
    n = len(u)
    F = np.zeros(n)
    F[0] = u[1] - 2*u[0] + alpha*(u[1] - u[0])**2 - alpha*u[0]**2
    for i in range(1, n):
        F[i] = u[i+1] - 2*u[i] + u[i-1] + alpha*(u[i+1]-u[i])**2 - alpha*(u[i]-u[i-1])**2
    F[n] = -2*u[n] + u[n-1] + alpha*u[n]**2 - alpha*(u[n]-u[n-1])**2
    return F

# Defining energy function 
def e(u, v, eigenvecs, eigenvals):

    # Linear part (H_0)
    Q = eigenvecs.T @ u
    P = eigenvecs.T @ v
    E = 0.5 * (P**2 + eigenvals * Q**2)

    return E

# Parameters
dt = np.sqrt(1/8)
Nt = 50000
alpha = 0.25

# Initial conditions
u = 4*eigvecs[:,0]
v = np.zeros(N-1)
F = f(u,alpha)


omega1 = np.sqrt(eigvals[0])

for i in range(Nt):
    u = u + dt*v + 0.5*dt**2*F
    F_new = f(u,alpha)
    v = v + 0.5*dt*(F + F_new)
    F = F_new
