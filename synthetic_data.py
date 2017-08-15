import networkx as nx,numpy as np
def simulate(p,G):
    N = len(G)
    T = [0]*N
    I = set([np.random.choice(range(N))])
    t=0
    while len(I)<N:
        t+=1
        NI = set([])
        for i in I:
            for j in G.neighbors(i):
                if np.random.rand() <p:
                    NI.add(j)
        NI = NI.difference(I)
        for i in NI:
            T[i] = t
        I = I|NI
    return T

N = 100
G = nx.erdos_renyi_graph(N,0.1)

f = open('data/cascades.csv',mode='w')
p = 0.05
for c in range(500):
    T = simulate(p,G)
    f.write(','.join(map(str,T))+'\n')
f.close()