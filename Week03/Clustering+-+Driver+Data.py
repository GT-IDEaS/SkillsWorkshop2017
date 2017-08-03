
# coding: utf-8

# In[3]:

import pandas as pd
import plotly
plotly.tools.set_credentials_file(username='uthaipon', api_key='uJ2ao98wtpRp6j4uLjRS')
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls

df = pd.read_csv(
    filepath_or_buffer='https://raw.githubusercontent.com/datascienceinc/learn-data-science/master/Introduction-to-K-means-Clustering/Data/data_1024.csv', 
    header=None, 
    sep='\t') #separate columns by tab, not by ','

df.columns=['Id','Distance_Feature','Speeding_Feature']
df.dropna(how="all", inplace=True) # drops the empty line at file-end

df.tail()


# In[17]:

import numpy as np
from sklearn.cluster import KMeans

"""
### For the purposes of this example, we store feature data from our
### dataframe `df`, in the `f1` and `f2` arrays. We combine this into
### a feature matrix `X` before entering it into the algorithm.
f1 = df['Distance_Feature'].values
f2 = df['Speeding_Feature'].values
print(f1)
print(f2)
X=np.matrix(zip(f1,f2))
"""

X = df.ix[1:,1:3] #ignore the first column of data and first row
X.head()


# In[22]:

#I want to get the number in the pandas frame, so make it an array first
table = X.values;

#2 clusters
dim = 2;

kmeans = KMeans(n_clusters=dim).fit(X)
#print(kmeans.labels_)

traces = []
for groupNumber in range(dim):

    trace = Scatter(
        x=table[kmeans.labels_==groupNumber,0], 
        y=table[kmeans.labels_==groupNumber,1],
        mode='markers',
        name="Group" + str(groupNumber+1),
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


# In[23]:

#4 clusters
dim = 4;

kmeans = KMeans(n_clusters=dim).fit(X)
#print(kmeans.labels_)

traces = []
for groupNumber in range(dim):

    trace = Scatter(
        x=table[kmeans.labels_==groupNumber,0], 
        y=table[kmeans.labels_==groupNumber,1],
        mode='markers',
        name="Group" + str(groupNumber+1),
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



