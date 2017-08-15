#!/usr/bin/env python

#https://www.datascience.com/blog/introduction-to-k-means-clustering-algorithm-learn-data-science-tutorials

import numpy as np
from matplotlib import pyplot
#import numpy.core.multiarray
from sklearn.cluster import KMeans
import pandas as pd

### For the purposes of this example, we store feature data from our
### dataframe `df`, in the `f1` and `f2` arrays. We combine this into
### a feature matrix `X` before entering it into the algorithm.

# Read input file .csv 
df = pd.read_csv(
    filepath_or_buffer='faithful.csv', sep=',')

#print (df)
f1 = df['eruptions'].values
f2 = df['waiting'].values

data=np.matrix(zip(f1,f2))
k=2
kmeans = KMeans(n_clusters=k).fit(data)

#The cluster labels are returned in kmeans.labels_. 
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

#plot clustering
for i in range(k):
    # select only data observations with cluster label == i
    ds = data[np.where(labels==i)]
    # plot the data observations
    pyplot.plot(ds[:,0],ds[:,1],'o')
    # plot the centroids
    lines = pyplot.plot(centroids[i,0],centroids[i,1],'kx')
    # make the centroid x's bigger
    pyplot.setp(lines,ms=15.0)
    pyplot.setp(lines,mew=2.0)
pyplot.show()

#Step 4: Iterate Over Several Values of K
#kmeans = KMeans(n_clusters=4).fit(X)












