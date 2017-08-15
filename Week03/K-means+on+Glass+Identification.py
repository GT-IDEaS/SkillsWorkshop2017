
# coding: utf-8

# In[1]:

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


# In[12]:

# split data table into data X and class labels y. Ignore first column because it's just ID

X = df.ix[:,1:10].values
y = df.ix[:,10].values
from sklearn.preprocessing import StandardScaler #standardized the indenpendent variables part
X_std = StandardScaler().fit_transform(X)

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


# In[7]:

#now start to cluster
from sklearn.cluster import KMeans


# In[8]:

#print(kmeans.labels_)


# In[36]:

""" below it does not work. Want to reuse for many number of clusters choices. Don't know why...

def plotClustersFig(dim):
    kmeans = KMeans(n_clusters=dim).fit(Y_sklearn)

    #plot the clusters. Same as plotly above but instead of 7 glass types, do 2 clusters
    traces = []

    for groupNumber in range(dim):

        trace = Scatter(
            x=Y_sklearn[kmeans.labels_==groupNumber,0],
            y=Y_sklearn[kmeans.labels_==groupNumber,1],
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
    return fig;
    
plotClustersFig(2)
py.iplot(fig)

"""


# In[1]:

#try 2 clusters
dim = 2;

kmeans = KMeans(n_clusters=dim).fit(Y_sklearn)

#plot the clusters. Same as plotly above but instead of 7 glass types, do 2 clusters
traces = []

for groupNumber in range(dim):

    trace = Scatter(
        x=Y_sklearn[kmeans.labels_==groupNumber,0],
        y=Y_sklearn[kmeans.labels_==groupNumber,1],
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


# In[33]:

#try 3 clusters
dim = 3;

kmeans = KMeans(n_clusters=dim).fit(Y_sklearn)

#plot the clusters. Same as plotly above but instead of 7 glass types, do 2 clusters
traces = []

for groupNumber in range(dim):

    trace = Scatter(
        x=Y_sklearn[kmeans.labels_==groupNumber,0],
        y=Y_sklearn[kmeans.labels_==groupNumber,1],
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


# In[34]:

#try 4 clusters
dim = 4;

kmeans = KMeans(n_clusters=dim).fit(Y_sklearn)

#plot the clusters. Same as plotly above but instead of 7 glass types, do 2 clusters
traces = []

for groupNumber in range(dim):

    trace = Scatter(
        x=Y_sklearn[kmeans.labels_==groupNumber,0],
        y=Y_sklearn[kmeans.labels_==groupNumber,1],
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


# In[35]:

#try 5 clusters
dim = 5;

kmeans = KMeans(n_clusters=dim).fit(Y_sklearn)

#plot the clusters. Same as plotly above but instead of 7 glass types, do 2 clusters
traces = []

for groupNumber in range(dim):

    trace = Scatter(
        x=Y_sklearn[kmeans.labels_==groupNumber,0],
        y=Y_sklearn[kmeans.labels_==groupNumber,1],
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


# In[37]:

dim = 6;

kmeans = KMeans(n_clusters=dim).fit(Y_sklearn)

#plot the clusters. Same as plotly above but instead of 7 glass types, do 2 clusters
traces = []

for groupNumber in range(dim):

    trace = Scatter(
        x=Y_sklearn[kmeans.labels_==groupNumber,0],
        y=Y_sklearn[kmeans.labels_==groupNumber,1],
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


# In[38]:

dim = 7;

kmeans = KMeans(n_clusters=dim).fit(Y_sklearn)

#plot the clusters. Same as plotly above but instead of 7 glass types, do 2 clusters
traces = []

for groupNumber in range(dim):

    trace = Scatter(
        x=Y_sklearn[kmeans.labels_==groupNumber,0],
        y=Y_sklearn[kmeans.labels_==groupNumber,1],
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


# In[39]:

dim = 8;

kmeans = KMeans(n_clusters=dim).fit(Y_sklearn)

#plot the clusters. Same as plotly above but instead of 7 glass types, do 2 clusters
traces = []

for groupNumber in range(dim):

    trace = Scatter(
        x=Y_sklearn[kmeans.labels_==groupNumber,0],
        y=Y_sklearn[kmeans.labels_==groupNumber,1],
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


# In[40]:

dim = 9;

kmeans = KMeans(n_clusters=dim).fit(Y_sklearn)

#plot the clusters. Same as plotly above but instead of 7 glass types, do 2 clusters
traces = []

for groupNumber in range(dim):

    trace = Scatter(
        x=Y_sklearn[kmeans.labels_==groupNumber,0],
        y=Y_sklearn[kmeans.labels_==groupNumber,1],
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


# In[41]:

dim = 10;

kmeans = KMeans(n_clusters=dim).fit(Y_sklearn)

#plot the clusters. Same as plotly above but instead of 7 glass types, do 2 clusters
traces = []

for groupNumber in range(dim):

    trace = Scatter(
        x=Y_sklearn[kmeans.labels_==groupNumber,0],
        y=Y_sklearn[kmeans.labels_==groupNumber,1],
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



