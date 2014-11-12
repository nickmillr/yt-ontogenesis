##############################################################################
# This will create a comprehesive catalog for all redshifts of entered data  # 
# Ran: July 10, 2015, Author: Nicholas Miller, Edited: July 15, 2014         #
##############################################################################

from yt_lib_opt import get_snapshot_name
from yt_lib_opt import create_catalog as cc
from yt_lib_opt import compose_data as cd

code = raw_input("What code do you wish to catalog? ")
#print "locating %s code" % code 
zarray = cd.get_redshifts(code)
ans = raw_input("Would you like to continue, %s catalogs will be made (y/n): " % len(zarray))
if ans == 'y' or 'yes':
	for r in zarray:
	    #print ('halo_catalogs/catalog/' +code +'/redshift' +str(r))
	    cc.make_catalog(code=code,z=int(r), output_dir=('halo_catalogs/catalog/' +code +'/redshift' +str(r)))
	    print "redshift catalog %s completed" % r
	print "%s catalog have been made, Bye now." % len(zarray)
else:
	if ans == 'n' or 'no': 
	    print "well then ..."
	else:
	    raise ValueError("invalid answer, y/n or yes/no")
