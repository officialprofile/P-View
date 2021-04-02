from vpython import *


with open('pdb108d.ent') as raw_data:
    lines = raw_data.readlines()

data = [line.split() for line in lines if line[:4] == 'ATOM']
title_raw = [line.split() for line in lines if line[:5] == 'TITLE']


title = ''
for i in range(len(title_raw)):
    if i == 0:
        title += ' '.join(title_raw[i][1:])
    else:
        title += ' '.join(title_raw[i][2:])

x, y, z = [float(i[6]) for i in data], [float(i[7]) for i in data], [float(i[8]) for i in data]
atoms = [i[-1] for i in data]

mass = {'H':1, 'He':4, 'C':12, 'O': 16, 'N':14, 'P':31}
colors = {'H':vector(0,0,0), 'He':vector(1,0,0), 'C':vector(0,1,0), 'O':vector(0,0,1), 'N':vector(1,0,1), 'P':vector(0,1,1)}

scene.background = vector(1, 1, 1)

for i in range(len(x)):
    if mass[atoms[i]]>1: #including hydrogen seems too heavy for gpu
        sphere(pos=vector(x[i], y[i], z[i]), radius=0.03*mass[atoms[i]], color = colors[atoms[i]])