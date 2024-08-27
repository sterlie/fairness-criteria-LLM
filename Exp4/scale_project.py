from gensim.models import Word2Vec
import numpy as np
import pandas as pd 
import csv


BoW_dir = ''
df = pd.read_csv(dir, sep=' ', index_col=False)

tokens = df['Word'].tolist()

model_dir = ''
w2v_model = Word2Vec.load(model_dir)

he_embedding = w2v_model.wv["he"]
she_embedding = w2v_model.wv["she"]

n = len(he_embedding)

# use numpy to define two vectors 
v1 = np.array(he_embedding)
v2 = np.array(she_embedding)

displacement = v1-v2

# calculate the midpoint of the displacement
mid = np.dot((displacement), 1/2)

# compute vector, v3, from midpoint to v2
v3 = v2  - mid
v4 = v1 - mid 

# compute magnitude of v3 and the unit vector
norm_v3 = np.sqrt(sum(v3**2))
norm_v4 = np.sqrt(sum(v4**2))

unit_v3 = v3/norm_v3       
unit_v4 = v4/norm_v3       

scalars = []

for id in tokens:
    if id in w2v_model.wv:
        embedding = np.array([w2v_model.wv[id]])

        vec = embedding-mid
        c = np.dot(vec, unit_v3)

        scalars.append((id, round(float(c),3)))


scalars = [t for t in (set(tuple(i) for i in scalars))]
scalars.sort(key=lambda a: a[1])

file_name = ''
with open(file_name,'w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['id','scalar'])
    for row in scalars:
        csv_out.writerow(row)