import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 32
dt = np.sqrt(1/8)
Nt = 50000
alpha = 0.25

# Initialisng A matrix, dimension (N-1)
A = 2*np.eye(N - 1) - np.eye(N - 1, k=-1) - np.eye(N - 1, k=1)

# Extracting eigenproperties
eigvals, eigvecs = np.linalg.eigh(A)
idx = np.argsort(eigvals)
eigvals = eigvals[idx]
eigvecs = eigvecs[:,idx]

omega1 = np.sqrt(eigvals[0])    # For plotting

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
    for i in range(1, n-1):
        F[i] = u[i+1] - 2*u[i] + u[i-1] + alpha*(u[i+1]-u[i])**2 - alpha*(u[i]-u[i-1])**2
    F[n-1] = -2*u[n-1] + u[n-2] + alpha*u[n-1]**2 - alpha*(u[n-1]-u[n-2])**2
    return F

# Defining energy function 
def e(u, v, eigenvecs, eigenvals):
    Q = eigenvecs.T @ u
    P = eigenvecs.T @ v
    E = 0.5 * (P**2 + eigenvals * Q**2)
    return E

# Initial conditions
u = 4*eigvecs[:,0]
v = np.zeros(N-1)
F = f(u,alpha)

E1, E2, E3, E4 = [], [], [], []
time = []

for i in range(Nt):
    u = u + dt*v + 0.5*dt**2*F
    F_new = f(u,alpha)
    v = v + 0.5*dt*(F + F_new)
    F = F_new

    E = e(u,v,eigvecs,eigvals)
    E1.append(E[0])
    E2.append(E[1])
    E3.append(E[2])
    E4.append(E[3])
    time.append(i*dt*omega1/(2*np.pi))

plt.plot(time,100*np.array(E1),label=r"$E_1$")
plt.plot(time,100*np.array(E2),label=r"$E_2$")
plt.plot(time,100*np.array(E3),label=r"$E_3$")
plt.plot(time,100*np.array(E4),label=r"$E_4$")

plt.xlabel(r"$\omega_1$t / 2π")
plt.xlim(0, 160)
plt.ylabel(r"$E_k$ ($\times10^{-2}$)")
plt.legend()
plt.show()
