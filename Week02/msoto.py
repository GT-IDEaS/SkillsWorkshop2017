#!/usr/bin/env python

import pandas as pd

# Read input file .csv 
df = pd.read_csv(
    filepath_or_buffer='https://archive.ics.uci.edu/ml/machine-learning-databases/blood-transfusion/transfusion.data', 
    header=None, 
    sep=',')

#define column names:
df.columns=['Recency', 'time', 'blood_count', 'months', 'Gender']
df.dropna(how="all", inplace=True) # drops the empty line at file-end
df.tail()

# split data table into data X and class labels y
X = df.ix[1:,0:4].values
y = df.ix[1:,4].values

#Standardizing
from sklearn.preprocessing import StandardScaler
X_std = StandardScaler().fit_transform(X)

from sklearn.decomposition import PCA as sklearnPCA
sklearn_pca = sklearnPCA(n_components=2)
Y_sklearn = sklearn_pca.fit_transform(X)

import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls

traces = []
for name in ('1', '0'):

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


## To plot offline and save it in .png
import plotly.offline as offline
import plotly.graph_objs as go

offline.plot({'data':data, 'layout':layout}, image='png')



















