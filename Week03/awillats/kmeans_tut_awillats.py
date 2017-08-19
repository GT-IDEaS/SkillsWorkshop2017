import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# tab separator https://stackoverflow.com/questions/27896214/reading-tab-delimited-file-with-pandas-works-on-windows-but-not-on-mac

#basic plottting https://matplotlib.org/users/pyplot_tutorial.html


drive_df = pd.read_csv('data_1024.csv',sep='\t')
#print(drive_df)

dist =drive_df.iloc[:,1].values
speed = drive_df.iloc[:,2].values
xstr = 'Distance traveled'
ystr = 'Time spent speeding'

#plot raw data to confirm import
#plt.plot(dist,speed,'k.')
#plt.xlabel(xstr)
#plt.ylabel(ystr)
#plt.show()

#bundle features together into matrix
#note the list is needed to unpack the zip operation, even though this wasn't specified in the tutorial
X = np.matrix(list(zip(dist,speed)))


nclust = 4

kmeans_out = KMeans(n_clusters=nclust).fit(X)
print(kmeans_out.cluster_centers_)

#i'm using the Paired colormap to get pale and dark versions of the same color
numPaired = 12 #the length of this colormap. Because it's not continuous, you have to use it's actual length... :/
cmap = plt.cm.get_cmap('Paired') #https://matplotlib.org/examples/color/colormaps_reference.html
clr_list = cmap(np.linspace(0,1,numPaired))


#plot the labeled clusters!
for i in range(nclust):
    ix = [kmeans_out.labels_==i]

    #use these to verify colors
    #plt.plot(i,i,'*',color=clr_list[2*i])
    #plt.plot(i,i+.5,'*',color=clr_list[2*i+1])

    plt.plot(dist[ix],speed[ix],'.',color=clr_list[2*i])
    plt.plot(kmeans_out.cluster_centers_[i][0],kmeans_out.cluster_centers_[i][1],'o',color=clr_list[2*i+1],markersize=10)

plt.title("K means on driver data, k={:d}".format(nclust))
plt.xlabel(xstr)
plt.ylabel(ystr)
plt.show()