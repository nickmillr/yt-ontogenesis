# <Make property txt files>

from yt.mods import *
from yt import *
from yt.units import kpc
import matplotlib.pyplot as plt
import os
from yt.analysis_modules.halo_analysis.api import HaloCatalog
from yt.analysis_modules.halo_finding.api import *
import compose_data as cd
import load_dataset as ld


def property_file(code,redshift,property_attribute):
    # if this is run on its own the propery must be in the form of 				      	    those listed in possible_properties.txt    
    data_pf = ld.load_data(code,redshift)
    halo_list = HaloFinder(data_pf)
    # make the file
    halofile = open(property_attribute+'.txt', 'w')
    if (property_attribute=='center_of_mass'):
	for halo in halo_list:
    		halofile.write(str(halo.center_of_mass()) + "\n")
    elif (property_attribute=='total_mass'): 
	for halo in halo_list:
    		halofile.write(str(halo.total_mass()) + "\n")
    elif (property_attribute=='maximum_density'): 
	for halo in halo_list:
    		halofile.write(str(halo.maximum_density()) + "\n")
    elif (property_attribute=='particle_size'): 
	for halo in halo_list:
    		halofile.write(str(halo.get_size()) + "\n")
    elif (property_attribute=='max_radius'):
	for halo in halo_list:
    		halofile.write(str(halo.maximum_radius()) + "\n")
    elif (property_attribute =='virial_mass'): 
	for halo in halo_list:
    		halofile.write(str(halo.virial_mass()) + "\n")
    elif (property_attribute=='virial_radius'): 
	for halo in halo_list:
    		halofile.write(str(halo.virial_radius()) + "\n")
    elif (property_attribute=='maximum_density_location'):
	for halo in halo_list:
    		halofile.write(str(halo.maximum_density_location()) + "\n")
    halofile.close()
    return

def get_properties():
    prop_dir = '/home/nmiller/library/output_files/code_properties/'
    f=open(prop_dir+'possible_properties.txt','r')
    proparray = []
    for line in f:
	column=line.split()
        proparray.append(column[0])
    f.close()
    proparray=np.array(proparray)
    return proparray

def check_dir(directory):
    if not os.path.exists(directory):
	os.makedirs(directory)

def make_ouput_files(code):
    save_dir = '/home/nmiller/library/output_files/code_properties/'
    proparray=get_properties()
    # Check/make code directory
    directory = (save_dir + str(code))
    check_dir(directory)
    # for each redshift, make each property
    zarray = cd.get_redshifts(code)
    for r in zarray:
	for p in proparray:
	    completeName = os.path.join(directory, 'redshift'+str(r))
	    print completeName
	    check_dir(completeName)
	    os.chdir(completeName)
	    property_file(code,r,p)
    	print "Output for %s %s is completed" % (code, p)
    print "%s completed" % code


