import numpy as np
import matplotlib as mpl
mpl.use("Agg") 
import matplotlib.pyplot as plt
from yt.pmods import *
#import yt.mods as ytm
import load_dataset as ld

def star_creation(code, redshift):
    ds=ld.load_data(code, redshift)
    dd = ds.all_data()

    pm = dd[('io', 'particle_mass')]
    pi = dd[('io', 'particle_index')]
    if (code=='ramses'):
	ct = dd[('all', 'particle_age')]
	stars=(ct!=0)
	print 'done'
    else:
	ct = dd[('io', 'creation_time')]
    	stars=(ct > 0)

    pm = pm[stars]
    pi = pi[stars]
    ct = ct[stars]


    plt.plot(pi,ct, '.')
    plt.title('Particle Index vs. Creation Time for %s %s' %(code,redshift))
    plt.savefig(str(code)+str(redshift)+"index_vs_creation.png")

    plt.plot(pm,ct, '.')
    plt.title('Particle Mass vs. Creation Time for %s %s' %(code,redshift))
    plt.savefig(str(code)+str(redshift)+"particlemass_vs_creation.png")
