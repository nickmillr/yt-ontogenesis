import numpy as np
import matplotlib as mpl
mpl.use("Agg") 
import matplotlib.pyplot as plt
#from yt.pmods import *
from yt.mods import *
import load_dataset as ld

#only works for ramses

def star_prop(dd, property=None):
    pm = dd[('io', 'particle_mass')]
    pi = dd[('io', 'particle_index')]
    ct = dd[('io', 'particle_age')]

    stars = (ct != 0)
	#total mass here 
    pm = pm[stars]
    pi = pi[stars]
    ct = ct[stars]
    
    if (property=='pm'):    # Masses
	return pm
    elif (property=='pi'):    # Stars index
	return pi
    elif (property=='ct'):    # Stars age
	return ct
    else: 
	return pm,pi,ct


def star_creation(code, redshift):
    ds=ld.load_data(code, redshift)
    dd = ds.all_data()
    pm,pi,ct = star_prop(dd) 

    plt.plot(pi,ct, '.')
    plt.title('Particle Index vs. Creation Time for %s %s' %(code,redshift))
    plt.savefig(str(code)+str(redshift)+"index_vs_creation.png")

    plt.plot(pm,ct, '.')
    plt.title('Particle Mass vs. Creation Time for %s %s' %(code,redshift))
    plt.savefig(str(code)+str(redshift)+"particlemass_vs_creation.png")
