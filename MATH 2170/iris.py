import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import random
plt.style.use('seaborn-v0_8-whitegrid')

iris_names = load_iris()['target_names']
iris_types = load_iris()['target']

iris_feature = load_iris()['feature_names']
iris_data = np.array(load_iris()['data'])

x = np.linspace(-2, 3, 10)  #Used to create an evenly spaced sequence in the 
                            #interval (-2 to 3). There will be (10) spaces.
plt.xlim(-2,3)              #Sets the x-axis boundaries for the graph
plt.ylim(-2,3)              #Sets the y-axis boundaries for the graph
plt.scatter( iris_data[:,0],iris_data[:,1]) #Plots all the vectors in X
#plt.show() 

k = 3
rand = random.randint(1, 100)

kmeans = KMeans(n_clusters=k, random_state=rand, n_init=rand).fit(iris_data) 
labels = kmeans.labels_        #the cluster assignment vector
reps = kmeans.cluster_centers_ #the cluster representatives
J_clust = kmeans.inertia_      #the cluster objective
print(J_clust)


grps = [[iris_data[i,:] for i in range(len(iris_data)) if labels[i]==j] for j in range(k)]
for i in range(k):
    plt.scatter([c[0] for c in grps[i]],[c[1] for c in grps[i]])
plt.xlim(-2,3)
plt.ylim(-2,3)
plt.show()

################################################################
# Task 1:
# My prediction is that the flowers will cluster relatively 
# close to each other, similar to the example.
# The reason I state this is due to the fact that the data 
# shouldn't change the clustering. It should be
# extremely similar to one another.
################################################################


################################################################
# Task 2:
# It seems like it is a good clustering. It's getting some 
# compact clusters, and I feel like that's a good thing.
print(labels)
print(iris_types) 
# The 0's and 1's seem to be flipped, and there are some 0's
# and/or 1's among the 2's. This means that there are various 
# errors in the clustering that I had done.
#################################################################