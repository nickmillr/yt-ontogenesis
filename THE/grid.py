# annotate grids

from yt import *
from yt_lib_opt import load_dataset as ld


def plot(code,redshift):
	EnzoC = (0.3861618,0.46086884,0.49156952)
	ds=ld.load_data(code, redshift)
	#ProjectionPlot(ds, 2, 'density', width=(1000, 'kpc'),weight_field=None).annotate_grids().save(str(code)+str(redshift)+'centeredgrid.png')
	SlicePlot(ds,'z', 'density', center=EnzoC, width=(1000, 'kpc')).annotate_grids().save(str(code)+str(redshift)+'centeredgrid.png')

def main():
	plot(code='ramses',redshift=1.0)
	plot(code='enzo',redshift=1.0)
main()

