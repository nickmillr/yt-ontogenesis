from yt import * 
from yt.mods import * 
import numpy as np
from yt_lib_opt import mass_functions as mf

def main():
   # you can input a range as a list: halos=[0,15]  
   a=mf.mstar_mhalo('ramses',1.0,halos=[961,1259])
   _file=open('ramsesfile1259.txt','w')
   _file.write('halo, total_mass, baryon_mass, particle_mass, star_mass \n')
   _file.write('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n')
   for x in xrange(0, len(a)):
	_file.write(str(a[x])+'\n')
   _file.close()

main()
