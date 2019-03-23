#!/usr/bin/env python3

import os

import numpy as np
import pygsp as gsp
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

# plt.rc('font', family='Latin Modern Roman')
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{lmodern}')

fig = plt.figure(figsize = (3, 3))
ax = fig.add_subplot(1, 1, 1)

G = gsp.graphs.ring.Ring(8)
G.plot(edges=True, ax=ax, title='', vertex_color='r', edge_color='b')

circle = plt.Circle((0, 0), radius=1, color='g', fill=False, LineWidth=3)
ax.add_artist(circle)

angle = 45*1.5

line_1 = plt.Line2D([1, 0], [0, 0], linewidth=2, linestyle="-", color="black")
line_2 = plt.Line2D([np.cos(angle/360*2*np.pi), 0], [np.sin(angle/360*2*np.pi), 0], linewidth=2, linestyle = "--", color="black")
ax.add_line(line_1)
ax.add_line(line_2)

angle_plot = Arc((0,0), 0.8, 0.8, 0, 0, angle, color='black', linewidth=2)
ax.add_patch(angle_plot)

ax.text(0.5*np.cos(angle/2/360*2*np.pi), 0.5*np.sin(angle/2/360*2*np.pi), r"$\theta$", fontsize=18)

ax.axis('off')
ax.axis('equal')

fig.tight_layout()
filename = os.path.splitext(os.path.basename(__file__))[0] + '.pdf'
fig.savefig(filename)
