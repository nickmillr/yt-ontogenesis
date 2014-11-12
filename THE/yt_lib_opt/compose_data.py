"""
Simple Functions for yt data analysis

"""

#-----------------------------------------------------------------------------
# Created: July 11, 2014, Last Edited: July 14, 2014 Author: Nicholas Miller.
#
# Used for yt users for analysis of simulation data.
#
# Use instructions below, distributed July, 2014.
#-----------------------------------------------------------------------------
import numpy as np
import os as os
from get_snapshot_name import *
import load_dataset as ld

def remove_massunit(s): # removes (Msun)
    return s[:-5]

def remove_lengthunit(s): # removes (code_length)
    return s[:-12]


def format_data(load_file, file_unit_type='length', tuple_data='no'):
    r"""Sorts and Trims data loaded from output profiles
	Formats the data so that it can be easily inputted into yt functions   
    
    Parameters
    ----------
    load_file : file name/location
        Something containing a set af values to sort. 
    file_unit_type : str 
        If the data in the file contains units
    tuple_data : yes/no/list
	For position data and groupings
	list is a special feature for certain types of data sets that need
	     a list rather than tuple to manipulate
    
    Examples
    --------
    >>> data = format_data('/home/Desktop/center_of_mass_file.txt', 'length', tuple_data='yes')
    
    """
    data_file = open(load_file, 'r')
    data = [line.strip() for line in data_file]
    if (file_unit_type=='length'):
	data = [remove_lengthunit(s) for s in data]
	data = tupler(data,tuple_data)
	return data
    elif (file_unit_type=='mass'):
	data = [remove_massunit(s) for s in data]
	return data
    elif (file_unit_type==None):
	data = tupler(data,tuple_data)
	return data
    else: 
	raise TypeError, 'file_type was expecting either length or mass unit type'    

def tupler(data,tuple_data):    
    if (tuple_data=='no'):
	return data
    elif (tuple_data=='yes'):
	data = [tuple(map(float,i[2:-1].split())) for i in data]
	return data
    elif (tuple_data=='list'):
	data = [list(map(float,i[2:-1].split())) for i in data]
	return data
    else: 
	raise ValueError, 'tuple_data accepts: no, yes, or list' 


def find_nearest_vector(array, value):
    idx = np.array([np.linalg.norm(x+y+z) for (x,y,z) in array-value]).argmin()
    return array[idx]


def find_above(_file, limit='1e11'):
    r"""Returns a list of elements in file that are above the supplied limit    
    
    Parameters
    ----------
    _file : list, or open file
        Something containing a set af values to sort. 
    limit : str of an exponetial
        input as '1eXX'
    
    Examples
    --------
    >>> mostmassive = find_above(massfile, '1e13')
    
    """
    result =[]
    num = 0
    for value in _file:
	if (float(value) >= float(limit)):
	    result.append(value) 
    return result


def redshift_file(redshift):
	#z_path = ld.find_dir('redshift'+str(redshift))
	z_path = ('redshift'+str(redshift)+'/')
	return z_path

def attribute_file(attribute):
    if (attribute=='centerofmass' or attribute=='com'):
    	file_wild='center_of_mass.txt'
	return file_wild
    if (attribute=='totalmass' or attribute=='tm'): 
    	file_wild='total_mass.txt'
	return file_wild
    if (attribute=='maxdensity' or attribute=='md'): 
    	file_wild='maximum_density.txt'
	return file_wild
    if (attribute=='particlesize' or attribute=='ps'): 
    	file_wild='particle_size.txt'
	return file_wild
    if (attribute=='maxradius' or attribute=='mr'):
    	file_wild='max_radius.txt'
	return file_wild
    if (attribute =='virialmass' or attribute=='vm'): 
    	file_wild='virial_mass.txt'
	return file_wild
    if (attribute=='virialradius' or attribute=='vr'): 
    	file_wild='virial_radius.txt'
	return file_wild
    if (attribute=='maxdensitylocation' or attribute=='mdl'):
    	file_wild='max_density_location.txt'
	return file_wild
    else: 
    	raise ValueError, "You have not entered a known attribute. Please try again using a common attribute." 

def get_output_file_name(code,attribute,redshift):
    r"""Returns the file name for a given attribute.
    
    Parameters
    ----------
    code : str
        Type of code used in anaylsis. 
    attribute : str
        Choices for attributes: centerofmass -or- com, totalmass -or- tm, 
		maxdensity -or- md, particlesize -or- ps, maxradius -or- mr,
		virialmass -or- vm, virialradius -or- vr, maxdensitylocation -or- mdl. 
    redshift : int or str
        Redshift value for file.     

    Examples
    --------
    >>> get_output_file_name(enzo,com,1.0)
    
    """
    #this should be done with a dictionary
    library_dir="/home/nmiller/nic-yt-library/output_files/"
    output_dir=library_dir+"code_properties/"
    codes=os.listdir(output_dir)
    if (code=='enzo'):
	code_dir=output_dir+'enzo/'
	red_dir=redshift_file(redshift)
	file_wild=(attribute_file(attribute))
	return code_dir+red_dir+file_wild
    if (code=='ramses'):
        code_dir=output_dir+'ramses/'
	red_dir=redshift_file(redshift)
	file_wild=(attribute_file(attribute))
	return code_dir+red_dir+file_wild
		
def get_redshifts(code):
    code_dir,file_wild=RyanMW_wildcard_files(code)
    f=open(code_dir+'redshift.txt','r')
    zarray = []
    for line in f:
        column=line.split()
        zarray.append(float(column[0]))
    f.close()
    zarray=np.array(zarray)
    print "There are %s redshift files for %s" % (len(zarray), code)
    return zarray






