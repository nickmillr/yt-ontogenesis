from yt import * 
from yt.mods import * 
import numpy as np
from yt_lib_opt import mass_functions as mf

def main():

   a=mf.mstar_mhalo('enzo',1.0,st=8801,end=8801)
   _file=open('file2.txt','w')
   _file.write('halo, total_mass, baryon_mass, particle_mass, star_mass \n')
   _file.write('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n')
   for x in xrange(0, len(a)):
	_file.write(str(a[x])+'\n')
   _file.close()

main()
