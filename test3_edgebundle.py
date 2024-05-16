# https://github.com/pavlin-policar/FDEB
import numpy as np
import networkx as nx

from fdeb import fdeb

import matplotlib.pyplot as plt
import matplotlib.collections as collections
import pandas as pd

# # Setup embedding and graph
# g = nx.karate_club_graph()
# x = np.array(list(nx.spring_layout(g).values()))
# adj = nx.to_scipy_sparse_array(g).tocoo()
data = pd.read_pickle('D:/研究生/研一/空间分析软件/测试数据/test_sample_pk')
edges=[]
x=[]
count=0
for index, row in data.iterrows():
    if count==10000:
        break
    edges.append([[row['o_lng'],row['o_lat']],[row['d_lng'],row['d_lat']]])
    count+=1
for index, row in data.iterrows():
    x.append([row['o_lng'],row['o_lat']])
    x.append([row['d_lng'],row['d_lat']])
edges=np.array(edges)    
x=np.array(x)
# Extract edges from embedding and adjacency matrix
# edges = np.stack([x[adj.row], x[adj.col]], axis=1)
print(edges.shape)


# Compute FDEB
edges_fdeb = fdeb(edges)

# Plot results
fig, ax = plt.subplots(ncols=2, figsize=(8, 4), dpi=150)

collection = collections.LineCollection(edges, color="k", alpha=0.05)
ax[0].add_collection(collection)
ax[0].scatter(x[:, 0], x[:, 1], c="tab:red", s=3, zorder=3)

collection = collections.LineCollection(edges_fdeb, color="k", alpha=0.05)
ax[1].add_collection(collection)
ax[1].scatter(x[:, 0], x[:, 1], c="tab:red", s=3, zorder=3)

plt.show()
