import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans

from sklearn.preprocessing import StandardScaler


# tab separator https://stackoverflow.com/questions/27896214/reading-tab-delimited-file-with-pandas-works-on-windows-but-not-on-mac
#basic plottting https://matplotlib.org/users/pyplot_tutorial.html

# The original dataset consists of 5 different folders, each with 100 files, with each file representing a single subject/person. Each file is a recording of brain activity for 23.6 seconds. The corresponding time-series is sampled into 4097 data points. Each data point is the value of the EEG recording at a different point in time.
#
# The response variable is y in column 179
#
# y contains the category of the 178-dimensional input vector. Specifically y in {1, 2, 3, 4, 5}
#
# 5- eyes open, means when they were recording the EEG signal of the brain the patient had their eyes open
# 4- eyes closed, means when they were recording the EEG signal the patient had their eyes closed
# 3- Yes they identify where the region of the tumor was in the brain and recording the EEG activity from the healthy brain area
# 2- They recorder the EEG from the area where the tumor was located
#
# All subjects falling in classes 2, 3, 4, and 5 are subjects who did not have epileptic seizure
#
# 1- Recording of seizure activity
#
# The Explanatory variables X1, X2, ..., X178
#
# Each 178-dimensional vector contained in a row, represents a randomly selected 1-second long sample picked from the single file. Recall that
# each file is a recording of brain activity for 23.6 seconds. The corresponding time-series is sampled into 4097 data points.

alpha = 50

data_source = 'cloud'

if data_source == 'epilepsy':
    df = pd.read_csv('epilepsy_data.csv')
    colors = {'Seizure': (31, 119, 180,alpha),
              'state2': (14, 12, 255,alpha),
              'state3': (255, 255, 14, alpha),
              'eyes closed': (50, 50, 75, alpha),
              'eyes open': (200, 200, 250,alpha)}

if data_source == 'cloud':
    df = pd.read_csv('cloud.csv',engine='python',sep='\s+',skiprows=53,nrows =1078-54)
    colors = {'x',(50,190,17,alpha)}
    # colors = {'Seizure': (31, 119, 180,alpha),
    #           'state2': (14, 12, 255,alpha),
    #           'state3': (255, 255, 14, alpha),
    #           'eyes closed': (50, 50, 75, alpha),
    #           'eyes open': (200, 200, 250,alpha)}

#df = pd.read_csv('data_1024.csv',sep='\t')


print(np.shape(df))
print(df.head(2))

#clip off first and last column
X = df.ix[:,:].values
#print(X)
y = df.ix[:,-1].values

if data_source=='cloud':
    y = 0*y
#print(y)

#enforce zero mean unit variance
X_std = StandardScaler().fit_transform(X)

n_pca=10
from sklearn.decomposition import PCA as sklearnPCA
sklearn_pca = sklearnPCA(n_components=n_pca)
pY = sklearn_pca.fit_transform(X_std)





pve = 100*sklearn_pca.explained_variance_ratio_
cumu_pve = np.cumsum(pve)



#formatting from https://stackoverflow.com/questions/1566936/easy-pretty-printing-of-floats-in-python
print("percent variances explained by components:",["{0:0.2f}%".format(i) for i in pve])

# fig0 = plt.figure()
# ax0 = fig0.add_subplot(111)
# ax0.plot(np.linspace(1,len(cumu_pve),len(cumu_pve)),cumu_pve,'k-o')
# plt.xlabel('num PCs')
# plt.ylabel('cumulative var explained [%]')
# plt.show()



print(np.shape(pY))
print(np.shape(y))
#
# if data_source == 'cloud':
#     plt.plot(pY[:,0],pY[:,1],'o')
# else:
#     #if n_pca==2:
#     for ci, labl in enumerate(colors.keys()):
#         print(ci)
#         rgbc_ = tuple(ti / 255 for ti in colors[labl])
#         # print(y==ci+1)
#         plt.plot(pY[y == ci + 1, 0], pY[y == ci + 1, 1], 'o', color=rgbc_)
#     plt.legend(colors.keys())
# plt.xlabel('PC1')
# plt.ylabel('PC2')
#
# plt.show()
#
# if n_pca>2:
#
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#
#     if data_source=='cloud':
#         ax.scatter(pY[:,0], pY[:, 1], pY[:, 2], marker='o')
#
#     else:
#         for ci, labl in enumerate(colors.keys()):
#             print(ci)
#             rgbc_ = tuple(ti / 255 for ti in colors[labl])
#             # print(y==ci+1)
#
#             match_i = (y == ci+1);
#
#             ax.scatter(pY[match_i, 0], pY[match_i, 1], pY[match_i,2], marker='o', c=rgbc_)
#         plt.legend(colors.keys())
#     plt.xlabel('PC1')
#     plt.ylabel('PC2')
#     ax.set_zlabel('PC3')
#
#     ax.view_init(60, 30)
#
#     plt.show()



nclust = 6
kmeans_out = KMeans(n_clusters=nclust).fit(pY[:,0:3])
print(kmeans_out.cluster_centers_)

numPaired = 12
cmap = plt.cm.get_cmap('Paired') #https://matplotlib.org/examples/color/colormaps_reference.html

clr_list = cmap(np.linspace(0,1,numPaired))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(nclust):
    ix = [kmeans_out.labels_==i]


    ix = np.reshape(ix,(np.shape(ix)[1],))
    #ix=np.transpose(ix)
    print(np.shape(ix))
    print(ix)


    ax.scatter(pY[ix,0],pY[ix,1],pY[ix,2],'.',color=clr_list[2*i+1])
    #plt.scatter(kmeans_out.cluster_centers_[i][0],kmeans_out.cluster_centers_[i][1],kmeans_out.cluster_centers_[i][2],marker='o',c=clr_list[2*i+1])

plt.title("K means on {:s} data, k={:d}".format(data_source,nclust))
plt.xlabel('PC1')
plt.ylabel('PC2')
ax.set_zlabel('PC3')
plt.show()

