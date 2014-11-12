import yt
from yt.units import *
import load_dataset as ld
import nearest_halo as nh
import  star as s

def total_mass_sphere(code, redshift, sphere_center, radius):
    # Load the dataset.
    ds = ld.load_data(code, redshift)

    # Create a 1 Mpc radius sphere, centered on the max density.
    sp = ds.sphere(sphere_center, (int(radius), "kpc"))

    # Use the total_quantity derived quantity to sum up the
    # values of the cell_mass and particle_mass fields
    # within the sphere.
    baryon_mass, particle_mass = sp.quantities.total_quantity(["cell_mass", "particle_mass"])
    massfile=(str(code)+str(redshift)+'spheremass.txt')
    ld.check_file(massfile)
    massfile = open(massfile, 'w')
    massfile.write("Total mass in sphere is %0.3e Msun (gas = %0.3e Msun, particles = %0.3e Msun)" % \
      ((baryon_mass + particle_mass).in_units('Msun'), \
       baryon_mass.in_units('Msun'), particle_mass.in_units('Msun')))
    massfile.close()
    return



# stellar mass vs halo mass 
# particle_mass=halo_mass
# make it so you can do all halos
def mstar_mhalo(code,redshift,st=0,end=10):
    ds = ld.load_data(code, redshift)
    result=[]
    for halo in xrange(int(st),int(end)):
	print halo
	sphere_center=nh._center_of_mass(code,redshift,halo)
    	radius=nh._radius(code,redshift,halo)
	sp = ds.sphere(sphere_center, (int(radius), "kpc"))
	stars=s.find_stars(sp)
    	m_star=s.find_M_star(sp)
	star_mass = sum(int(x) for x in m_star)
        baryon_mass, particle_mass = sp.quantities.total_quantity(["cell_mass", "particle_mass"])
	baryon_mass=baryon_mass.in_units('Msun')
	particle_mass=particle_mass.in_units('Msun')
        total_mass=(baryon_mass+particle_mass)
	result.append([halo, total_mass, baryon_mass, particle_mass, star_mass])
    return result














   # plt.ioff()
   # plt.plot(m_star,h_mass, '.')
   # plt.title('Stellar mass vs. Halo Mass for %s %s' %(code,redshift))
   # plt.savefig(str(code)+str(redshift)+"Mstar_vs_Mhalo.png")
    
     

# stellar formation rate against z(time)
#def star_formation_rate():
 #   return


# number density vs stellar mass

# Mstar/Mhalo vs Mhalo

#('deposit', 'all_density') 
#('deposit', 'all_mass')
#('enzo', 'Dark_Matter_Density') 
#('enzo', 'Density')
#('enzo', 'H2II_Density')
#('enzo', 'H2I_Density')
#('enzo', 'HII_Density') 
#('enzo', 'HI_Density') 
#('enzo', 'HM_Density')
#('enzo', 'HeIII_Density')
#('enzo', 'HeII_Density') 
#('enzo', 'HeI_Density')
#('enzo', 'Metal_Density') 
#('enzo', 'Temperature') 
#('gas', 'cell_mass')
#('io', 'particle_index')
#('io', 'particle_mass')
