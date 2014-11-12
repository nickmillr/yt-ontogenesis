from yt import *
import load_dataset as ld


code='ramses'
redshift=1.0
ds=ld.load_data(code, redshift)
dd = ds.all_data()
pa = dd[('all', 'particle_age')]
print pa
