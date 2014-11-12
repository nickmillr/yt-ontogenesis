# <Make property txt files>

from yt.mods import *
from yt import *
from yt.units import kpc
import matplotlib.pyplot as plt

from yt.analysis_modules.halo_analysis.api import HaloCatalog
from yt.analysis_modules.halo_finding.api import *

data_pf = load('/home/share/astro/Data/scylla/Ryan_MW/enzo/r0038/redshift0038')
halo_list = HaloFinder(data_pf)

### Center of Mass
halofile = open("center_of_mass.txt", 'w')

for halo in halo_list:
	# the center of mass for the halo.
    halofile.write(str(halo.center_of_mass()) + "\n")

halofile.close()


### Maximun Density Location
halofile = open("maximum_density_location.txt", 'w')

for halo in halo_list:
	# the location of the maximum density particle in the HOP halo.
    halofile.write(str(halo.maximum_density_location()) + "\n")

halofile.close()


### Total Mass
halofile = open("total_mass.txt", 'w')

for halo in halo_list:
	# the mass of the halo in Msol (not Msol/h).
    halofile.write(str(halo.total_mass()) + "\n")

halofile.close()


### Bulk Velocity
halofile = open("bulk_velocity.txt", 'w')

for halo in halo_list:
	# the velocity of the center of mass of the halo in simulation units.
    halofile.write(str(halo.bulk_velocity()) + "\n")

halofile.close()


### Max Radius
halofile = open("maximum_radius.txt", 'w')

for halo in halo_list:
	# the distance from the center of mass to the most distant particle in the halo in simulation units.
    halofile.write(str(halo.maximum_radius()) + "\n")

halofile.close()


### Size
halofile = open("particle_size.txt", 'w')

for halo in halo_list:
	# the number of particles in the halo.
    halofile.write(str(halo.get_size()) + "\n")

halofile.close()


### Virial Mass
halofile = open("virial_mass.txt", 'w')

for halo in halo_list:
	# Finds the virial mass for a halo using just the particles. This is inferior to the full Halo Profiler extension (Halo Profiling), but useful nonetheless in some cases. Returns the mass in Msol, or -1 if the halo is not virialized. Defaults: virial_overdensity=200.0 and bins=300.
    halofile.write(str(halo.virial_mass()) + "\n")

halofile.close()


### Virial radius
halofile = open("virial_radius.txt", 'w')

for halo in halo_list:
	# Finds the virial radius of the halo using just the particles. Returns the radius in code units, or -1 if the halo is not virialized. Defaults: virial_overdensity=200.0 and bins=300.
    halofile.write(str(halo.virial_radius()) + "\n")

halofile.close()
