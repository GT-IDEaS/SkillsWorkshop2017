
# coding: utf-8

# In[20]:

"""
Attribute Information:

1. Id number: 1 to 214 
2. RI: refractive index 
3. Na: Sodium (unit measurement: weight percent in corresponding oxide, as are attributes 4-10) 
4. Mg: Magnesium 
5. Al: Aluminum 
6. Si: Silicon 
7. K: Potassium 
8. Ca: Calcium 
9. Ba: Barium 
10. Fe: Iron 
11. Type of glass: (class attribute) 
-- 1 building_windows_float_processed 
-- 2 building_windows_non_float_processed 
-- 3 vehicle_windows_float_processed 
-- 4 vehicle_windows_non_float_processed (none in this database) 
-- 5 containers 
-- 6 tableware 
-- 7 headlamps
"""
#data setup section
glassTypeName = {1:"building_windows_float_processed",
                 2:"building_windows_non_float_processed",
                 3:"vehicle_windows_float_processed",
                 4:"vehicle_windows_non_float_processed",
                 5:"containers",
                 6:"tableware",
                 7:"headlamps"};

import pandas as pd
import plotly
plotly.tools.set_credentials_file(username='uthaipon', api_key='uJ2ao98wtpRp6j4uLjRS')
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls

df = pd.read_csv(
    filepath_or_buffer='https://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data', 
    header=None, 
    sep=',')

df.columns=['Id','RI','Na','Mg','Al','Si','K','Ca','Ba','Fe','Glass Type']
df.dropna(how="all", inplace=True) # drops the empty line at file-end

df.tail()


# In[6]:

# split data table into data X and class labels y. Ignore first column because it's just ID

X = df.ix[:,1:10].values
y = df.ix[:,10].values


# In[7]:

y #for me to see the data type of dependent variables. It's in the form of integers


# In[8]:

from sklearn.preprocessing import StandardScaler #standardized the indenpendent variables part
X_std = StandardScaler().fit_transform(X)

import numpy as np
#mean_vec = np.mean(X_std, axis=0)
#cov_mat = (X_std - mean_vec).T.dot((X_std - mean_vec)) / (X_std.shape[0]-1)
#print('Covariance matrix \n%s' %cov_mat)

print('NumPy covariance matrix: \n%s' %np.cov(X_std.T)) 
#in this data set, STD it's 9-by-9 matrix because there are 9 indenpendent variables


# In[10]:

#Next, we perform an eigendecomposition on the covariance matrix:
cov_mat = np.cov(X_std.T)

eig_vals, eig_vecs = np.linalg.eig(cov_mat)

print('Eigenvectors \n%s' %eig_vecs)
print('\nEigenvalues \n%s' %eig_vals)


#check that enginvector has length 1
for ev in eig_vecs:
    np.testing.assert_array_almost_equal(1.0, np.linalg.norm(ev))

# Make a list of (eigenvalue, eigenvector) tuples
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

# Sort the (eigenvalue, eigenvector) tuples from high to low
eig_pairs.sort()
eig_pairs.reverse()

# Visually confirm that the list is correctly sorted by decreasing eigenvalues
print('Eigenvalues in descending order:')
for i in eig_pairs:
    print(i[0])


# In[12]:

#how much can first few dimensions out of nine explain the information?
tot = sum(eig_vals)
var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)

trace1 = Bar(
        x=['PC %s' %i for i in range(1,10)],
        y=var_exp,
        showlegend=False)

trace2 = Scatter(
        x=['PC %s' %i for i in range(1,10)], 
        y=cum_var_exp,
        name='cumulative explained variance')

data = Data([trace1, trace2])

layout=Layout(
        yaxis=YAxis(title='Explained variance in percent'),
        title='Explained variance by different principal components')

fig = Figure(data=data, layout=layout)
py.iplot(fig)


# In[24]:

#take two eigenvectors with top eigenvalues, and list them as matrix of 2 columns, each column is one eigenvector 
matrix_w = np.hstack((eig_pairs[0][1].reshape(9,1), 
                      eig_pairs[1][1].reshape(9,1)))

print('Matrix W:\n', matrix_w)

Y = X_std.dot(matrix_w)

#Y shows what each row (9-dim data point) will project onto 2-dim space defined by W

traces = []

for typeNumber in range(1,8): #typeNumber is what dependent variables look like    
#for each typeNumber, we have one Scatter plot
    trace = Scatter(
        x=Y[y==typeNumber,0],
        y=Y[y==typeNumber,1],
        mode='markers',
        name=str(typeNumber) + ": " + glassTypeName[typeNumber],
        marker=Marker(
            size=12,
            line=Line(
                color='rgba(217, 217, 217, 0.14)',
                width=0.5),
            opacity=0.8))
    traces.append(trace)


data = Data(traces)
layout = Layout(showlegend=True,
                scene=Scene(xaxis=XAxis(title='PC1'),
                yaxis=YAxis(title='PC2'),))

fig = Figure(data=data, layout=layout)
py.iplot(fig)


# In[26]:

#now let's try three. 
#take three eigenvectors with top eigenvalues, and list them as matrix of 3 columns, each column is one eigenvector 
matrix_w = np.hstack((eig_pairs[0][1].reshape(9,1), 
                      eig_pairs[1][1].reshape(9,1),
                      eig_pairs[2][1].reshape(9,1)))

print('Matrix W:\n', matrix_w)

Y = X_std.dot(matrix_w)

#Y shows what each row (9-dim data point) will project onto 2-dim space defined by W

traces = []

for typeNumber in range(1,8): #typeNumber is what dependent variables look like    
#for each typeNumber, we have one Scatter plot
    trace = Scatter3d(
        x=Y[y==typeNumber,0],
        y=Y[y==typeNumber,1],
        z=Y[y==typeNumber,2],
        mode='markers',
        name=str(typeNumber) + ": " + glassTypeName[typeNumber],
        marker=Marker(
            size=12,
            line=Line(
                color='rgba(217, 217, 217, 0.14)',
                width=0.5),
            opacity=0.8))
    traces.append(trace)


data = Data(traces)
layout = Layout(showlegend=True,
                scene=Scene(xaxis=XAxis(title='PC1'),
                yaxis=YAxis(title='PC2'),))

fig = Figure(data=data, layout=layout)
py.iplot(fig)


# In[30]:

#for fun, let's also try 1-D
#take one eigenvectors with top eigenvalues, and list them as matrix of 1 columns, each column is one eigenvector 
matrix_w = np.hstack((eig_pairs[0][1].reshape(9,1),
                      np.zeros(9).reshape(9,1)))

print('Matrix W:\n', matrix_w)

Y = X_std.dot(matrix_w)

#Y shows what each row (9-dim data point) will project onto 2-dim space defined by W

traces = []

for typeNumber in range(1,8): #typeNumber is what dependent variables look like    
#for each typeNumber, we have one Scatter plot
    trace = Scatter(
        x=Y[y==typeNumber,0],
        y=Y[y==typeNumber,1],
        mode='markers',
        name=str(typeNumber) + ": " + glassTypeName[typeNumber],
        marker=Marker(
            size=12,
            line=Line(
                color='rgba(217, 217, 217, 0.14)',
                width=0.5),
            opacity=0.8))
    traces.append(trace)


data = Data(traces)
layout = Layout(showlegend=True,
                scene=Scene(xaxis=XAxis(title='PC1'),
                yaxis=YAxis(title='PC2'),))

fig = Figure(data=data, layout=layout)
py.iplot(fig)


# In[21]:

#anything below here is by using sklearn. Should look the same as my own version, which is so (up to symmetric transformation)

from sklearn.decomposition import PCA as sklearnPCA
sklearn_pca = sklearnPCA(n_components=2)
Y_sklearn = sklearn_pca.fit_transform(X_std)

traces = []

for name in range(1,8): #because the dependent variables are 1,2,...,7, so just use list of numbers as 'name' of class

    trace = Scatter(
        x=Y_sklearn[y==name,0],
        y=Y_sklearn[y==name,1],
        mode='markers',
        name=name,
        marker=Marker(
            size=12,
            line=Line(
                color='rgba(217, 217, 217, 0.14)',
                width=0.5),
            opacity=0.8))
    traces.append(trace)


data = Data(traces)
layout = Layout(xaxis=XAxis(title='PC1', showline=False),
                yaxis=YAxis(title='PC2', showline=False))
fig = Figure(data=data, layout=layout)
py.iplot(fig)


# In[22]:

sklearn_pca = sklearnPCA(n_components=3) #now try 3 components
Y_sklearn = sklearn_pca.fit_transform(X_std)

traces = []

for name in range(1,8): #because the dependent variables are 1,2,...,7, so just use list of numbers as 'name' of class

    trace = Scatter3d(
        x=Y_sklearn[y==name,0],
        y=Y_sklearn[y==name,1],
        z=Y_sklearn[y==name,2],
        mode='markers',
        name=name,
        marker=Marker(
            size=12,
            line=Line(
                color='rgba(217, 217, 217, 0.14)',
                width=0.5),
            opacity=0.8))
    traces.append(trace)


data = Data(traces)
layout = Layout(xaxis=XAxis(title='PC1', showline=False),
                yaxis=YAxis(title='PC2', showline=False))
fig = Figure(data=data, layout=layout)
py.iplot(fig)


# In[ ]:



