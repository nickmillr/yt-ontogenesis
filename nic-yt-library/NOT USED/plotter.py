#position = [0.3861618, 0.46086884, 0.49156952]


Basically recreating the original plots. this isnt needed

class Plots():
 """Provides simplified methods for calling a variety of common plots used in yt.
    
    
    Parameters
    ----------
    halos_pf : str
        Dataset created by a halo finder.  If None, a halo finder should be 
        provided with the finder_method keyword.
    data_pf : str
        Dataset created by a simulation.
    data_source : data container
        Data container associated with either the halos_pf or the data_pf.
    finder_method : str
        Halo finder to be used if no halos_pf is given.
    output_dir : str
        The top level directory into which analysis output will be written.
        Default: "."
    finder_kwargs : dict
        Arguments to pass to the halo finder if finder_method is given.

    Examples
    --------

    # create profiles or overdensity vs. radius for each halo and save to disk
    >>> from yt.mods import *
    >>> from yt.analysis_modules.halo_analysis.api import *
    >>> data_pf = load("DD0064/DD0064")
    >>> halos_pf = load("rockstar_halos/halos_64.0.bin",
    ...                 output_dir="halo_catalogs/catalog_0064")
    >>> hc = HaloCatalog(data_pf=data_pf, halos_pf=halos_pf)
    # filter out halos with mass < 1e13 Msun
    >>> hc.add_filter("quantity_value", "particle_mass", ">", 1e13, "Msun")
    # create a sphere object with radius of 2 times the virial_radius field
    >>> hc.add_callback("sphere", factor=2.0, radius_field="virial_radius")
    # make radial profiles
    >>> hc.add_callback("profile", "radius", [("gas", "overdensity")],
    ...                 weight_field="cell_volume", accumulation=True)
    # save the profiles to disk
    >>> hc.add_callback("save_profiles", output_dir="profiles")
    # create the catalog
    >>> hc.create()


    # load in the saved halo catalog and all the profile data
    >>> halos_pf = load("halo_catalogs/catalog_0064/catalog_0064.0.h5")
    >>> hc = HaloCatalog(halos_pf=halos_pf,
                         output_dir="halo_catalogs/catalog_0064")
    >>> hc.add_callback("load_profiles", output_dir="profiles")
    >>> hc.load()

    See Also
    --------
    add_callback, add_filter, add_finding_method, add_quantity
    
    """
	def __init__(self):

	def projection_plot(self, dataset, axis, field, center='c', width=None,
		axes_unit=None, weight_field=None, max_level=None, origin='center-window',
                fontsize=18, field_parameters=None, data_source=None, proj_style = "integrate", 
		window_size=8.0, aspect=None, save_name=None, add_marker=None, add_halos=None, 			add_point=None, add_clumps=None ):
	    
	    prj = ProjectionPlot(pf=datset, axis=axis, fields=field, center=center, width=width,
			   axes_unit=axes_unit, weight_field=weight_field, max_level=max_level,
			   origin=origin, fontsize=fontsize, field_parameters=field_parameters, 			   data_source=data_source, proj_style =proj_style, window_size=window_size,
			   aspect=aspect)
	    if add_marker = 
	    if add_halos
	    if add_point
annotate_quiver,annotate_image_line, annotate_magnetic_field, annotate_particles, annotate_sphere, annotate_title
	    if save_name=None:
	    else:
		prj.save(save_name) 



	def profile_plot 
	def slice_plot
annotate_title, annotate_arrow, annotate_contour, annotate_grids, annotate_marker, annotate_streamlines, annotate_text annotate_velocity, annotate_timestamp
