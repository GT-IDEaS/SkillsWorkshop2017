#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 16:39:17 2017

@author: cchang373
"""

import plotly
plotly.offline.init_notebook_mode()
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

#Loading the Dataset
import pandas as pd
df=pd.read_csv(
        filepath_or_buffer='https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.data',
        header=None,
        sep=',')
df.columns=['class','left_weight','left_distance','right_weight','right_distance']
df.dropna(how="all",inplace=True)#drops the empty line at file-end
#print df.tail() 

X=df.ix[:,1:5].values
y=df.ix[:,0].values
#print X,y

#plotting histograms
traces = []

legend = {0:False, 1:False, 2:False, 3:True}

colors = {'L': 'rgb(31, 119, 180)', 
          'B': 'rgb(255, 127, 14)', 
          'R': 'rgb(44, 160, 44)'}

for col in range(4):
    for key in colors:
        traces.append(Histogram(x=X[y==key, col], 
                        opacity=0.75,
                        xaxis='x%s' %(col+1),
                        marker=Marker(color=colors[key]),
                        name=key,
                        showlegend=legend[col]))

data = Data(traces)

layout = Layout(#barmode='overlay',
                xaxis=XAxis(domain=[0, 0.25], title='left_weight'),
                xaxis2=XAxis(domain=[0.3, 0.5], title='left_distance'),
                xaxis3=XAxis(domain=[0.55, 0.75], title='right_weight'),
                xaxis4=XAxis(domain=[0.8, 1], title='right_distance'),
                yaxis=YAxis(title='count'),
                title='Distribution of the different balance scale')

fig = Figure(data=data, layout=layout)
#plot(fig)

#Standarizing
from sklearn.preprocessing import StandardScaler
X_std = StandardScaler().fit_transform(X)
#Covariance matrix
import numpy as np
mean_vec=np.mean(X_std,axis=0)
cov_mat=(X_std-mean_vec).T.dot((X_std-mean_vec))/(X_std.shape[0]-1)
#print('Covariance matrix \n%s' %cov_mat)

eig_vals,eig_vecs=np.linalg.eig(cov_mat)
#print('Eigenvectors \n%s' %eig_vecs)
#print('\nEigenvalues \n%s' %eig_vals)

#Singular Vector Decomposition
u,s,v=np.linalg.svd(X_std.T)
#print u

#Selecting Principal Componenets
# Make a list of (eigenvalue, eigenvector) tuples
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
print eig_pairs

# Sort the (eigenvalue, eigenvector) tuples from high to low
#eig_pairs.sort()
#eig_pairs.reverse()

tot = sum(eig_vals)
var_exp = [(i / tot)*100 for i in eig_vals]
cum_var_exp = np.cumsum(var_exp)

trace1 = Bar(
        x=['PC %s' %i for i in range(1,5)],
        y=var_exp,
        showlegend=False)

trace2 = Scatter(
        x=['PC %s' %i for i in range(1,5)], 
        y=cum_var_exp,
        name='cumulative explained variance')

data = Data([trace1, trace2])

layout=Layout(
        yaxis=YAxis(title='Explained variance in percent'),
        title='Explained variance by different principal components')

fig = Figure(data=data, layout=layout)
#plot(fig)

matrix_w = np.hstack((eig_pairs[0][1].reshape(4,1), 
                      eig_pairs[1][1].reshape(4,1),
                      eig_pairs[2][1].reshape(4,1),
                      eig_pairs[3][1].reshape(4,1)))

#print('Matrix W:\n%s' %matrix_w)

#Projection onto the new feature space
Y=X_std.dot(matrix_w)
traces = []

for name in ('L', 'B', 'R'):

    trace = Scatter(
        x=Y[y==name,0],
        y=Y[y==name,1],
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
layout = Layout(showlegend=True,
                scene=Scene(xaxis=XAxis(title='PC1'),
                yaxis=YAxis(title='PC2'),))

fig = Figure(data=data, layout=layout)
plot(fig)










































