"""
yt catalog function

Note: this program cannot be run in parallel without adjustments.

"""

#-----------------------------------------------------------------------------
# Created: July, 11 2014, Author: Nicholas Miller.
#
# Used for yt users to produce halo catalogs of simulation data.
#
# Use instructions below, distributed July, 2014.
#-----------------------------------------------------------------------------

import get_snapshot_name as snapshot
from yt import *
from yt.units import kpc
from yt.analysis_modules.halo_analysis.api import HaloCatalog


# Creates HaloCatalog (if already created used load file)
def make_catalog(code, z, finder = 'hop', output_dir="halo_catalogs/catalog"):
	"""Creates HaloCatalog with no filters or callbacks
	contains; particle_identifier, particle_mass, 
	particle_position_x, particle_position_y, particle_position_z,
        virial_radius
        for all halos in selected code.

        The virial mass is calculated, using the built in `Halo.virial_info`
        functionality.  The mass is then returned.

        Parameters
        ----------
        code : string
            Input code in ' ' or " ", 
	    No Default.
        z: integer
            The number related to the redshift you wish to observe.
            No Default.
	finder : string
	    The only method tested to run in yt at the time of this 
	    development was 'hop', but if changed so the 'Rockstar
	    works, input finder in ' ' or " ".
	    Default = 'hop'
	output_dir : string
	    Input where you want the catalog file to export too.
	    Default = "halo_catalogs/catalog"
	

        Returns
        -------
        catalog file = catalog.0.h5
            Found in the output file inputted or at default location
            if not specified.

        Examples
        --------
        >>> make_catalog('enzo', 1)
        """
	datapath = snapshot.get_snapshot_name(code,z)
	data_pf = load(datapath)
		# With version of yt that was used when this script was written 
		# finder_kwargs was required to be set as follows	
	hc = HaloCatalog(data_pf=data_pf, finder_method=finder, finder_kwargs={}, output_dir=output_dir)
	hc.create()
	print "Your catalog has been created at" + str(output_dir)


def load_catalog(code,redshift):
	catalog_dir='/home/nmiller/THE/halo_catalogs/catalog/'
	code_catalog=(catalog_dir+str(code))
	redshift_dir=(code_catalog+'/redshift'+str(redshift))
	file_dir=(redshift_dir+'/redshift'+str(redshift)+'.0.h5')
	
	hpf = load(str(file_dir))
    	hc = HaloCatalog(halos_pf=hpf, output_dir="halo_catalogs/catalog")
    	return hc.load()
	
	


#---------- UPDATE ----------
# This could be made into a class so that you are able to
# funcs: 	Make catalog
#		Load catalog
#		Add filter
#		Add Callbacks
