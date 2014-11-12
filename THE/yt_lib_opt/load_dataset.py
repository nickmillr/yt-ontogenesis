"""
for loading yt and directory commands

"""

#-----------------------------------------------------------------------------
# Created: July 13, 2014, Last Edited: July 14, 2014 Author: Nicholas Miller.
#
# Used for yt users to load simulation data for analysis.
#
# Use instructions below, distributed July, 2014.
#-----------------------------------------------------------------------------
from yt import *
from get_snapshot_name import *
import os as os

def load_data(code, redshift):
    file_name=get_snapshot_name(code=code,z=redshift)
    ds=load(file_name)
    return ds

def current_directory():
    return os.getcwd()

def check_dir(directory):
    if not os.path.exists(directory):
	os.makedirs(directory)
    return

def check_file(_file_):
    if os.path.exists(_file_):
	"You will overwrite the previous %s file" % _file_
	ans = raw_input('do you wish to proceed? ')
	if (ans=='y') or (ans=='yes'):	
	    return "It has been done."
	else:
	    print 'Well darn.'
	    quit()

def find_file(file_name):
    print file_name
    for dirname, dirnames, filenames in os.walk('.'):
	#print path to all filenames.
	for filename in filenames:
	    if file_name == filename:
		print os.path.join(dirname, filename)
		return os.path.join(dirname, filename)
    
     #return os.path.dirname(os.path.realpath(_file_))

def find_dir(dir_name):
    for dirname, dirnames, filenames in os.walk('.'):
    	# print path to all subdirectories first.
    	for subdirname in dirnames:	 
	    if subdirname == dir_name:
		return os.path.join(dirname, subdirname)
