
"""
Finds the Most massive halo near a point and a function to annotate it an produce multiple plots.

"""

#-----------------------------------------------------------------------------
# Created: July 14, 2014, Last Edited: July 14, 2014 Author: Nicholas Miller.
#
# Used for yt users to produce halo catalogs of simulation data.
#
# Use instructions below, distributed July, 2014.
#-----------------------------------------------------------------------------
import yt.mods as ytm
from yt import *
import compose_data as cd
import numpy as np

def _radius(code,z,halo_number):
	radius_file=cd.get_output_file_name(code,attribute='vr',redshift=z)
	data=cd.format_data(load_file=radius_file, file_unit_type='length', tuple_data='no')
	rad = data[halo_number]
	rad = float(rad)*25000.0
	return rad	

def mark_halo(data, halo_center, code, z, halo=None, width_in_kpc=1000, weight=None):
	prj=ProjectionPlot(data, 2, 'density', center=halo_center, width=(int(width_in_kpc),'kpc'), weight_field=weight)
	prj=prj.annotate_point(halo_center, halo, text_args={'size':'x-large'})
	prj=prj.annotate_marker(halo_center)
	prj=prj.save(str(code)+str(halo)+'-xmarker.png')
	
	# add virial radius for correct sphere
	radius = _radius(code,z,halo)
	p = ProjectionPlot(data, 'z', 'density', center=halo_center, width=(int(width_in_kpc), 'kpc'))
	p.annotate_sphere(halo_center, (radius, 'kpc'), {'fill':False})
	p.save(str(code)+str(halo)+'-sphere.png')

def nearest_halo(position, com_file, mass_file):
	com_data=cd.format_data(com_file, file_unit_type='length', tuple_data='list')
	mass_data=cd.format_data(mass_file, file_unit_type='mass', tuple_data='no')
	# See how many of the most massive halos exist
	highmass=cd.find_above(_file=mass_data)
	data_array = np.array(com_data[:len(highmass)]) 
	place=(cd.find_nearest_vector(data_array, position))
	place=list(place)
	data=list(com_data)
	halo=data.index(place)
	
	print "The closest halo is halo %s at %s" %(halo, place)
	return (halo, place) 
	

# ----- UPDATE -----
#have it find most massive in density as well and then future make catalog of miller images from the max dens list s othen you can compare what the max dens list is compared to the loc of halo 

