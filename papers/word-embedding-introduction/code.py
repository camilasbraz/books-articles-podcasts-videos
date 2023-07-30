from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('cbow_s300.txt')

carro = model['carro']
print(carro)

import numpy as np

def dist_euclidiana(u,v):
  return np.linalg.norm(u - v)

caminhao = model['caminhão']
laranja = model['laranja']
veiculo = model['veículo']

d1 = dist_euclidiana(carro, caminhao)
d2 = dist_euclidiana(carro, laranja)
d3 = dist_euclidiana(carro, veiculo)

print("d1 = ", d1)
print("d2 = ", d2)
print("d3 = ", d3)

def similaridade_cossenos(u,v):
  return np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v))

s1 = similaridade_cossenos(carro, caminhao)
s2 = similaridade_cossenos(carro, laranja)
s3 = similaridade_cossenos(carro, veiculo)

print("s1 = ", s1)
print("s2 = ", s2)
print("s3 = ", s3)


def analogia(x1,x2,y1):
  y2 = model.most_similar(positive = [y1, x2], negative = [x1])
  return y2

arvore = model['arvore']
folha = model['folha']
tronco = model['tronco']

#raiz

print(analogia(arvore, folha, tronco))
