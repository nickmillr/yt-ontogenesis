import numpy as np
import matplotlib as mpl
mpl.use("Agg") 
import matplotlib.pyplot as plt
#from yt.pmods import *
from yt.mods import *
import load_dataset as ld

def star_prop(dd):
    pm = dd[('io', 'particle_mass')]
    pi = dd[('io', 'particle_index')]
    ct = dd[('io', 'creation_time')]

    stars = (ct > 0)

    pm = pm[stars]
    pi = pi[stars]
    ct = ct[stars]
    return pm,pi,ct

def find_stars(dd):
    stars=star_prop(dd)
    pi=stars[1]
    return pi

def find_M_star(dd):
    stars=star_prop(dd)
    pm=stars[0]
    return pm    

def star_creation(code, redshift):
    ds=ld.load_data(code, redshift)
    dd = ds.all_data()
    stars = star_prop(dd) 

    pm = stars[0]
    pi = stars[1]
    ct = stars[2]

    plt.plot(pi,ct, '.')
    plt.title('Particle Index vs. Creation Time for %s %s' %(code,redshift))
    plt.savefig(str(code)+str(redshift)+"index_vs_creation.png")

    plt.plot(pm,ct, '.')
    plt.title('Particle Mass vs. Creation Time for %s %s' %(code,redshift))
    plt.savefig(str(code)+str(redshift)+"particlemass_vs_creation.png")
