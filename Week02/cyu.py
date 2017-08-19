#!/usr/bin/env python3

"""Principle Component Analysis on data set """

__author__ = "Chuanping Yu"
__date__ = "July 31, 2017"

import pandas as pd
import plotly
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA as sklearnPCA
import numpy as np

plotly.tools.set_credentials_file(username='cyugatech', api_key='k8B6qyhH9B3fujv684CX')

df = pd.read_csv(
    filepath_or_buffer='https://archive.ics.uci.edu/ml/machine-learning-databases/ecoli/ecoli.data',
    header=None,
    sep='\s+')
df.columns = ['SequenceName', 'mcg', 'gvh', 'lip', 'chg', 'aac', 'alm1', 'alm2', 'class']
df.dropna(how="all", inplace=True) # drops the empty line at file-end

df.tail()

X = df.ix[:, 1:8].values
y = df.ix[:, 8].values

X_std = StandardScaler().fit_transform(X)
cov_mat = np.cov(X_std.T)

eig_vals, eig_vecs = np.linalg.eig(cov_mat)

# Make a list of (eigenvalue, eigenvector) tuples
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:, i]) for i in range(len(eig_vals))]

# Sort the (eigenvalue, eigenvector) tuples from high to low
eig_pairs.sort()
eig_pairs.reverse()

# Visually confirm that the list is correctly sorted by decreasing eigenvalues
print('Eigenvalues in descending order:')
for i in eig_pairs:
    print(i[0])

tot = sum(eig_vals)
var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)

trace1 = Bar(
    x=['PC %s' %i for i in range(1, 8)],
    y=var_exp,
    showlegend=False)

trace2 = Scatter(
    x=['PC %s' %i for i in range(1, 8)],
    y=cum_var_exp,
    name='cumulative explained variance')

data = Data([trace1, trace2])

layout = Layout(
    yaxis=YAxis(title='Explained variance in percent'),
    title='Explained variance by different principal components')

fig = Figure(data=data, layout=layout)
py.iplot(fig)

sklearn_pca = sklearnPCA(n_components=5)
Y_sklearn = sklearn_pca.fit_transform(X_std)

traces = []

for name in ('cp', 'im', 'imS', 'imL', 'imU', 'om', 'omL', 'pp'):

    trace = Scatter(
        x=Y_sklearn[y == name, 0],
        y=Y_sklearn[y == name, 1],
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
