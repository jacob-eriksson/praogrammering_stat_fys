#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:32:21 2026

@author: jacob
"""
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
def get_forces(positions_list, alpha):
    forces = []
    forces.append(0)
    
    index = 1
    while index < 32:
        force = positions_list[index+1] - 2*positions_list[index] + positions_list[index-1] + alpha*(positions_list[index+1]-positions_list[index])**2 - alpha*(positions_list[index]-positions_list[index-1])**2
        forces.append(force)
        index += 1
    
    forces.append(0)
    
    return forces
# Defining energy function 



def new_positions(position_list, velocities_list, delta_t, index):
    #fixa att definiera alpha
    alpha = 1
    forces = get_forces(position_list, alpha)
    new_positions = np.zeros(33)
    new_velocities = np.zeros(33)
    
    new_positions[0] = 0
    new_velocities[0] = 0
    index = 0
    while index < 32:
        new_positions[index] = position_list[index] + velocities_list[index] * delta_t 
        new_velocities[index] = velocities[index] + ((forces[index] / 1) * delta_t)
        index += 1
        
    new_positions[32] = 0
    new_velocities[32] = 0

    return [new_positions, new_velocities]



use_vector = eigvecs[0]

index = 0
positions = [0]
while index < 32:
    position = 4 * use_vector[index]
    positions.append(position)
    index += 1

positions.append(0)
velocities = np.zeros(33)   





    
