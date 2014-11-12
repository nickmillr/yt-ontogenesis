
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
from yt import *
import compose_data as cd
import numpy as np

# Find the halo number
def _halo_number(code,z,center):
	com_file=cd.get_output_file_name(code,attribute='com',redshift=z)
	com_data=cd.format_data(load_file=com_file, file_unit_type='length', tuple_data='list')
	data=list(com_data)
	halo=data.index(place)
	return halo

# Find radius of a halo
def _radius(code,z,halo_number):
	radius_file=cd.get_output_file_name(code,attribute='vr',redshift=z)
	data=cd.format_data(load_file=radius_file, file_unit_type='length', tuple_data='no')
	rad = data[halo_number]
	rad = float(rad)*25000.0
	return rad

# Find the center of mass of a halo
def _center_of_mass(code,z,halo_number):
	com_file=cd.get_output_file_name(code,attribute='com',redshift=z)
	data=cd.format_data(load_file=com_file, file_unit_type='length', tuple_data='list')
        com = data[halo_number]
	return com

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

def particles_in_halo(halo, halolist):
	for halo in halo_list:
    		print halo["particle_index"]
    		print halo["particle_position_x"] # in simulation units	

# ----- UPDATE -----
#have it find most massive in density as well and then future make catalog of miller images from the max dens list s othen you can compare what the max dens list is compared to the loc of halo 

