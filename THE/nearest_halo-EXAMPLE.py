
##########################################################################
# nearest_halo-EXAMPLE.py                                                #
# Created: July 14, 2014, Author: Nicholas Miller                        #
# An example of what a script for finding a nearest halo would look like #
##########################################################################

import yt.mods as ytm
from yt import *
from yt_lib_opt import nearest_halo as nh
from yt_lib_opt import load_dataset
from yt_lib_opt import compose_data 
from yt_lib_opt import halo_annotation

data_type = 'enzo'
r = 1.0
ds = load_data(data_type, r)
position=[0.3861618, 0.46086884, 0.49156952]
com_file=get_output_file_name(data_type,'com',r)
#print com_file
mass_file=get_output_file_name(data_type,'tm',r)
#print mass_file
Halo = nh.nearest_halo(position, com_file=com_file,mass_file=mass_file)
circle_halo(data=ds, code=data_type, z=r, halo_center=Halo[1], halo=Halo[0], )


