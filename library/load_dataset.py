from yt import *
from get_snapshot_name import *
import os as os

def load_data(code, redshift):
    file_name=get_snapshot_name(code=code,z=redshift)
    ds=load(file_name)
    return ds

def current_directory():
    return os.getcwd()

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
