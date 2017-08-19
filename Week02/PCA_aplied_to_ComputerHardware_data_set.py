# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 13:28:49 2017

@author: Aster
"""

#=========================================================================
# Preparing the Iris Dataset
#=========================================================================
import pandas as pd

df = pd.read_csv(
    filepath_or_buffer='https://archive.ics.uci.edu/ml/machine-learning-databases/cpu-performance/machine.data', 
    header=None, 
    sep=',')

df.columns=['vendor_name','Model_Name', 'MYCT', 'MMIN', 'MMAX', 'CACH','CHMIN','CHMAX','PRP','ERP']
df.dropna(how="all", inplace=True) # drops the empty line at file-end

df.tail()

# split data table into data X and class labels y

X = df.ix[:,3:12].values
y = df.ix[:,0].values


#--------------------------------------
# Standardizing 
#--------------------------------------
from sklearn.preprocessing import StandardScaler
X_std = StandardScaler().fit_transform(X)


#=========================================================================
#Eigendecomposition - Computing Eigenvectors and Eigenvalues
#=========================================================================

#--------------------------------------
#Covariance Matrix
#--------------------------------------

import numpy as np
mean_vec = np.mean(X_std, axis=0)
cov_mat = (X_std - mean_vec).T.dot((X_std - mean_vec)) / (X_std.shape[0]-1)
# or
cov_mat = np.cov(X_std.T)

print('Covariance matrix: \n%s' %cov_mat)

eig_vals, eig_vecs = np.linalg.eig(cov_mat)

print('Eigenvectors \n%s' %eig_vecs)
print('\nEigenvalues \n%s' %eig_vals)


#--------------------------------------
#Correlation Matrix
#--------------------------------------
# The eigendecomposition of the covariance matrix (if the input data was standardized) yields the same results as a eigendecomposition on the correlation matrix, since the correlation matrix can be understood as the normalized covariance matrix.
'''
Eigendecomposition of the standardized data based on the correlation matrix:
'''
cor_mat1 = np.corrcoef(X_std.T)
eig_vals, eig_vecs = np.linalg.eig(cor_mat1)

print('Eigenvectors \n%s' %eig_vecs)
print('\nEigenvalues \n%s' %eig_vals)

'''
Eigendecomposition of the raw data based on the correlation matrix:
'''
cor_mat2 = np.corrcoef(X.T)
eig_vals, eig_vecs = np.linalg.eig(cor_mat2)

print('Eigenvectors \n%s' %eig_vecs)
print('\nEigenvalues \n%s' %eig_vals)


#--------------------------------------
#Singular Vector Decomposition
#--------------------------------------
# Most PCA implementations perform a Singular Vector Decomposition (SVD) to improve the computational efficiency.
u,s,v = np.linalg.svd(X_std.T)
u

#=========================================================================
# Selecting Principal Components
#=========================================================================

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
    
print(eig_pairs)

matrix_w = np.hstack((eig_pairs[0][1].reshape(7,1), 
                      eig_pairs[1][1].reshape(7,1),
                      eig_pairs[2][1].reshape(7,1),
                      eig_pairs[3][1].reshape(7,1)))

print('Matrix W:\n', matrix_w)


#=========================================================================
#Projection Onto the New Feature Space
#=========================================================================

Y = X_std.dot(matrix_w)

