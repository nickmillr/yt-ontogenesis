# This will create a comprehesive catalog for all redshifts of Enzo data
# Ran: July 10, 2015, Author: Nicholas Miller, Edited: July 15, 2014

from get_snapshot_name import *
import create_catalog as cc
import compose_data as cd

code = 'enzo' 
zarray = cd.get_redshifts(code)
for r in zarray:
    cc.make_catalog(code=code,z=int(r), output_dir=('halo_catalogs/catalog/enzo/redshift' +str(r)))
    print "redshift catalog %s completed" % r
print "%s catalog have been made, Bye now." % len(zarray)

