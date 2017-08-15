#%%
import pandas as pd
df=pd.read_csv(
        filepath_or_buffer='https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', 
    header=None, 
    sep=',')

df.columns=['Class','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium',
            'Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins',
            'Color intensity','Hue','OD280/OD315 of diluted wines','Proline']
df.dropna(how="all", inplace=True) # drops the empty line at file-end

df.tail()

#%%
X = df.iloc[:,1:14].values
y = df.iloc[:,0].values
#%%
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls
#%%
import plotly 
plotly.tools.set_credentials_file(username='yzwangyuqing', api_key='bn3aASYcP8n0PThahLrC')
   
traces = []

legend = {0:False, 1:False, 2:False, 3:False,4:False,5:False,
          6:False,7:False,8:False,9:False,10:False,11:False,12:True}

colors = {1: 'rgb(31, 119, 180)', 
          2: 'rgb(255, 127, 14)', 
          3: 'rgb(44, 160, 44)'}

for col in range(13):
    for key in colors:
        traces.append(Histogram(x=X[y==key, col], 
                        opacity=0.75,
                        xaxis='x%s' %(col+1),
                        marker=Marker(color=colors[key]),
                        name=key,
                        showlegend=legend[col]))
data = Data(traces)

layout = Layout(barmode='overlay',
                xaxis=XAxis(domain=[0, 0.07], title='Alcohol'),
                xaxis2=XAxis(domain=[0.08, 0.15], title='Malic acid'),
                xaxis3=XAxis(domain=[0.16, 0.23], title='Ash'),
                xaxis4=XAxis(domain=[0.24, 0.31], title='Alcalinity of ash'),
                xaxis5=XAxis(domain=[0.32, 0.39], title='Magnesium'),
                xaxis6=XAxis(domain=[0.4, 0.47], title='Total phenols'),
                xaxis7=XAxis(domain=[0.48, 0.55], title='Flavanoids'),
                xaxis8=XAxis(domain=[0.56, 0.63], title='Nonflavanoid phenols'),
                xaxis9=XAxis(domain=[0.64, 0.71], title='Proanthocyanins'),
                xaxis10=XAxis(domain=[0.72, 0.79], title='Color intensity'),
                xaxis11=XAxis(domain=[0.8, 0.87], title='Hue'),
                xaxis12=XAxis(domain=[0.88, 0.95], title='OD280/OD315 of diluted wines'),
                xaxis13=XAxis(domain=[0.96, 1], title='Proline'),
                yaxis=YAxis(title='count'),
                title='Distribution of wine features from different cultivars ')

fig = Figure(data=data, layout=layout)

py.iplot(fig)

#%%
from sklearn.preprocessing import StandardScaler
X_std = StandardScaler().fit_transform(X)

import numpy as np
mean_vec = np.mean(X_std, axis=0)
cov_mat = (X_std - mean_vec).T.dot((X_std - mean_vec)) / (X_std.shape[0]-1)
print('Covariance matrix \n%s' %cov_mat)


#%%

cov_mat = np.cov(X_std.T)

eig_vals, eig_vecs = np.linalg.eig(cov_mat)

print('Eigenvectors \n%s' %eig_vecs)
print('\nEigenvalues \n%s' %eig_vals)


#%%
u,s,v = np.linalg.svd(X_std.T)
u
#%%

# Make a list of (eigenvalue, eigenvector) tuples
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

# Sort the (eigenvalue, eigenvector) tuples from high to low
eig_pairs.sort()
eig_pairs.reverse()

# Visually confirm that the list is correctly sorted by decreasing eigenvalues
print('Eigenvalues in descending order:')
for i in eig_pairs:
    print(i[0])
    
    #%%
tot = sum(eig_vals)
var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)

trace1 = Bar(
        x=['PC %s' %i for i in range(1,14)],
        y=var_exp,
        showlegend=False)

trace2 = Scatter(
        x=['PC %s' %i for i in range(1,14)], 
        y=cum_var_exp,
        name='cumulative explained variance')

data = Data([trace1, trace2])

layout=Layout(
        yaxis=YAxis(title='Explained variance in percent'),
        title='Explained variance by different principal components')

fig = Figure(data=data, layout=layout)
py.iplot(fig)
#%%
matrix_w = np.hstack((eig_pairs[0][1].reshape(13,1), 
                      eig_pairs[1][1].reshape(13,1)))

print('Matrix W:\n', matrix_w)

#%%
Y = X_std.dot(matrix_w)
traces = []

for name in (1,2,3):

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
py.iplot(fig)

