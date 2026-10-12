import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def clustering_objective(data, clustering, reps):
    J_obj = 0
    for i in range(len(data)):
        J_obj += np.linalg.norm(data[i] - reps[int(clustering[i]) - 1])**2
    return J_obj/len(data)

def update_cluster(data, reps):
    new_clustering = np.zeros(len(data))
    for i in range(len(data)):
        distance = np.zeros(len(reps))
        for j in range(len(reps)):
            distance[j] = np.linalg.norm(data[i] - reps[j])
        new_clustering[i] = np.argmin(distance) + 1
    return new_clustering

def update_reps(data, clustering):
    new_reps = []
    for i in range(int(max(clustering))):
        sum = np.zeros(len(data[0]))
        count = 0
        for j in range(len(data)):
            if clustering[j] == (i + 1):
                sum = sum + data[j]
                count += 1
            if count > 0:
                new_reps.append(sum/count)
    return np.array(new_reps)

def kmeans_alg(data, reps, show_steps=True):
    J_obj = []
    clustering = update_cluster(data, reps)
    J_obj.append(clustering_objective(data, clustering, reps))

    if show_steps:
        new_reps = update_reps(data, clustering)
        print("Iteration", len(J_obj) - 1, ":\n (Update Cluster)")
        print("C = ", clustering)
        print("Z = ", reps)
        print("J^clust = ", clustering_objective(data, clustering, new_reps), "\n")

    clustering = update_cluster(data, new_reps)
    J_obj.append(clustering_objective(data, clustering, new_reps))

    if show_steps:
        print("(Update Cluster)")
        print("C = ", clustering)
        print("Z = ", reps)
        print("J^clust = ", J_obj[-1], "\n")
    
    if len(new_reps) == len(reps):
        if np.linalg.norm(np.array(new_reps) - np.array(reps)) < 1e-6:
            Stop = True
        else:
            reps = new_reps
    else:
        reps = new_reps

    return new_reps, clustering, J_obj, len(J_obj) - 1

