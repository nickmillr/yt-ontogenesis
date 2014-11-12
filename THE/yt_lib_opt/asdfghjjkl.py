from yt import * 
from yt.mods import * 
import numpy as np
import load_dataset as ld
import nearest_halo as nh
import compose_data as cd

code='ramses'
redshift=1.0
result =[]

	
    #except ValueError:
	#return None  

ds = ld.load_data(code, redshift)
file_name=cd.get_output_file_name(code,'com',redshift)
file_com=open(file_name,'r')
number_halos=[] 
for line in file_com:
    l=line.split()
    number_halos.append(l)
print len(number_halos)
halo = 0

_file=open('ramsesfile.txt','w')
_file.write('halo, total_mass, baryon_mass, particle_mass, star_mass \n')
_file.write('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n')

while halo != len(number_halos): 
    try:
    #for halo in xrange(640,len(number_halos)):
	print halo
        sphere_center=nh._center_of_mass(code,redshift,halo)
        radius=nh._radius(code,redshift,halo)
        sp = ds.sphere(sphere_center, (int(radius), "kpc"))

       # pm = sp[('io', 'particle_mass')]
       # pi = sp[('io', 'particle_index')]
       # ct = sp[('all', 'particle_age')]

 #       stars = (ct != 0)
	
  #      pm = pm[stars]
   #     pi = pi[stars]
    #    ct = ct[stars]

     #   m_star=pm.in_units('Msun')
      #  star_mass = np.sum(m_star)
       # print star_mass
        #star_mass=star_mass.in_units('Msun')
        baryon_mass, particle_mass = sp.quantities.total_quantity(["cell_mass", "particle_mass"])
        baryon_mass=baryon_mass.in_units('Msun')
        particle_mass=particle_mass.in_units('Msun')
        total_mass=(baryon_mass+particle_mass)
        a=[halo, total_mass, baryon_mass, particle_mass]
	result.append([halo, total_mass, baryon_mass, particle_mass])
	halo+=1
	_file.write(str(a)+'\n')
    except:
	_file.write(str(halo)+'failed'+'\n')
	print halo+1
	halo+=1
	
_file.close()
