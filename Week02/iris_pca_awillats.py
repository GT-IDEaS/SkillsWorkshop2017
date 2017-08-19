import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


df = pd.read_csv(filepath_or_buffer='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
    header=None,
    sep=',')
df.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
df.dropna(how="all", inplace=True) # drops the empty line at file-end

print(df.tail())

#regressors
X = df.ix[:,0:4].values
#classes
y = df.ix[:,4].values


num_features = 4;

alpha = 150;

colors = {'Iris-setosa': (31, 119, 180,alpha),
          'Iris-versicolor': (255, 127, 14,alpha),
          'Iris-virginica': (44, 160, 44,alpha)}


# feature plotting
# for si in range(num_features):
#     plt.subplot(1,num_features,si+1)
#     for ci,labl in enumerate(colors.keys()):
#
#         #map 255 color to 0-1 color
#         rgbc_ = tuple(ti/255 for ti in colors[labl])
#
#         plt.hist(X[y==labl,si],5,color=rgbc_)
            #https://matplotlib.org/devdocs/gallery/pyplots/pyplot_text.html#sphx-glr-gallery-pyplots-pyplot-text-py
#
#     if (si==num_features-1): plt.legend(colors.keys(),loc='upper right')
#     plt.ylabel(df.columns[si])
# plt.show()



#enforce zero mean unit variance
X_std = StandardScaler().fit_transform(X)


mean_vec = np.mean(X_std, axis=0)
cov_mat = (X_std - mean_vec).T.dot((X_std - mean_vec)) / (X_std.shape[0]-1)
print('Covariance matrix \n%s' %cov_mat)

cov_mat = np.cov(X_std.T)
print('Covariance matrix \n%s' %cov_mat)

eig_vals, eig_vecs = np.linalg.eig(cov_mat)

print('Eigenvectors \n%s' %eig_vecs)
print('\nEigenvalues \n%s' %eig_vals)


#confirm SVD gives the same thing
u,s,v = np.linalg.svd(X_std.T)
print(u)

#make sure all eigenvectors are unit magnitude
for ev in eig_vecs:
    np.testing.assert_array_almost_equal(1.0, np.linalg.norm(ev))
print('Everything ok!')


# Make a list of (eigenvalue, eigenvector) tuples
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

# Sort the (eigenvalue, eigenvector) tuples from high to low
eig_pairs.sort()
eig_pairs.reverse()

# Visually confirm that the list is correctly sorted by decreasing eigenvalues
print('Eigenvalues in descending order:')
for i in eig_pairs:
    print(i[0])

tot = sum(eig_vals)
var_exp = [(i / tot) * 100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)

print("Cumulative variance explained by components",cum_var_exp)



#select how many eigenvectors to actually use
num_ev = 2
print("\n\n\nChoosing {:d} eigenvectors, which together explain {:2.1f}% of the variance".format(num_ev,cum_var_exp[num_ev]))


matrix_w = eig_pairs[0][1].reshape(num_features,1)

print(matrix_w)
for i in range(1,num_ev):
    matrix_w = np.hstack((matrix_w,
                          eig_pairs[i][1].reshape(num_features,1)))

print(matrix_w)

pY = X_std.dot(matrix_w)


#un-comment this section to verify that the "manual" approach works
from sklearn.decomposition import PCA as sklearnPCA
sklearn_pca = sklearnPCA(n_components=2)
pY = sklearn_pca.fit_transform(X_std)
print(sklearn_pca.explained_variance_ratio_)

# print(np.shape(pY))
# print(np.shape(y))
# print(y)

if num_ev==2:
    for ci,labl in enumerate(colors.keys()):
        rgbc_ = tuple(ti/255 for ti in colors[labl])
        plt.plot(pY[y==labl,0],pY[y==labl,1],'o',color=rgbc_)
    plt.legend(colors.keys())
    plt.xlabel('PC1')
    plt.ylabel('PC2')

    plt.show()



