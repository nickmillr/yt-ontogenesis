import yt
from yt.units import *
from yt.mods import *
import load_dataset as ld
import nearest_halo as nh
import star as s

code='enzo'
z=1.0
halo=54
ds = ld.load_data(code, z)
sphere_center=nh._center_of_mass(code,z,halo)
radius=nh._radius(code,z,halo)
sp = ds.sphere(sphere_center, (int(radius), "kpc"))
dd = sp.quantities()
print dd
