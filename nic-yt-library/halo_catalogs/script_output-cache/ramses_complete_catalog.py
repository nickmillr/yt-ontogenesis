# This will create a comprehesive catalog for all redshifts of Ramses data
# Ran: July 11, 2015, Author Nicholas Miller

from get_snapshot_name import *
import create_catalog as cc

code = 'ramses' 
code_dir,file_wild=RyanMW_wildcard_files(code)
f=open(code_dir+'redshift.txt','r')
zarray = []
for line in f:
        column=line.split()
        zarray.append(float(column[0]))
f.close()
zarray=np.array(zarray)
for r in zarray:
    cc.make_catalog(code=code,z=int(r), output_dir=('halo_catalogs/catalog/ramses/redshift' +str(r)))
    print "redshift catalog %s completed" % r
print "%s catalog have been made, Bye now." % len(zarray)

