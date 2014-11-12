########################
#   This script will   #
#    annotate halos    #
########################

from yt import *
from yt.units import kpc
import load_dataset as ld
import create_catalog as cc
import nearest_halo as nh
from yt.analysis_modules.halo_analysis.api import HaloCatalog

# Load the data then plot Enzo halo plot
def halo_annotations(code,redshift, multiple_widths='yes',all_axis='no'):
    data_pf = ld.load_data(code, redshift)
    catalog_dir='/home/nmiller/THE/halo_catalogs/catalog/'
    code_catalog=(catalog_dir+str(code))
    redshift_dir=(code_catalog+'/redshift'+str(redshift))
    file_dir=(redshift_dir+'/redshift'+str(redshift)+'.0.h5')
	
    hpf = load(str(file_dir))
    hc = HaloCatalog(halos_pf=hpf, output_dir="halo_catalogs/catalog")
    hc.load

    EnzoC = ( 0.3861618 ,  0.46086884,  0.49156952)

    if (multiple_widths=='yes'):
	ProjectionPlot(data_pf, 'z', 'density', center=EnzoC).annotate_halos(hc).annotate_title(str(code)+str(redshift)+'Halos').save(str(code)+str(redshift)+'Halos.png')
	ProjectionPlot(data_pf, 'z', 'density', center=EnzoC, width=(10000,'kpc')).annotate_halos(hc).annotate_title(str(code)+str(redshift)+'Halos').save(str(code)+str(redshift)+'Halos_width10k.png')
	ProjectionPlot(data_pf, 'z', 'density', center=EnzoC, width=(3000,'kpc')).annotate_halos(hc).annotate_title(str(code)+str(redshift)+'Halos').save(str(code)+str(redshift)+'Halos_width3k.png')
	ProjectionPlot(data_pf, 'z', 'density', center=EnzoC, width=(600,'kpc')).annotate_halos(hc).annotate_title(str(code)+str(redshift)+'Halos').save(str(code)+str(redshift)+'Halos_width600.png')

    else:
	ProjectionPlot(data_pf, 'z', 'density', center=EnzoC).annotate_halos(hc).annotate_title(str(code)+str(redshift)+'Halos').save(str(code)+str(redshift)+'Halos.png')
   
    if (all_axis=='yes'):
	ProjectionPlot(data_pf, 'z', 'density', center=EnzoC).annotate_halos(hc).annotate_title(str(code)+str(redshift)+'Halos').save(str(code)+str(redshift)+'Halos_z.png')
	ProjectionPlot(data_pf, 'x', 'density', center=EnzoC).annotate_halos(hc).annotate_title(str(code)+str(redshift)+'Halos').save(str(code)+str(redshift)+'Halos_x.png')
	ProjectionPlot(data_pf, 'y', 'density', center=EnzoC).annotate_halos(hc).annotate_title(str(code)+str(redshift)+'Halos').save(str(code)+str(redshift)+'Halos_y.png')

    else:
	return

def plot_halo_sphere(code, redshift, halo_number, width=400):
    ds=ld.load_data(code, redshift)
    radius=nh._radius(code,redshift,halo_number)
    center=nh._center_of_mass(code,z,halo_number)
    halo_sphere = ds.sphere(center, (float(radius), "kpc"))
    ProjectionPlot(ds, 'density', width=(int(width), "kpc"), center='max', weight_field=None, data_source=halo_sphere).save('Halo'+str(halo_number)+'.png')


def circle_halo(data, halo_center, code, z, halo=None, width_in_kpc=1000, weight=None):
	prj=ProjectionPlot(data, 2, 'density', center=halo_center, width=(int(width_in_kpc),'kpc'), weight_field=weight)
	prj.annotate_point(halo_center, halo, text_args={'size':'x-large'})
	prj.annotate_marker(halo_center)
	prj.save(str(code)+str(halo)+'-xmarker.png')
	
	# add virial radius for correct sphere
	radius = _radius(code,z,halo)
	p = ProjectionPlot(data, 'z', 'density', center=halo_center, width=(int(width_in_kpc), 'kpc'))
	p.annotate_sphere(halo_center, (radius, 'kpc'), {'fill':False})
	p.save(str(code)+str(halo)+'-sphere.png')
