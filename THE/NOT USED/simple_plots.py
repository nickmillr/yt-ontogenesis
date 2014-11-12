from yt import *
import load_dataset as ld

def simulation_plot(code,redshift):
    ds=ld.load_data(code, redshift)

    ProjectionPlot(ds, 2, 'density', width=(25.0, 'mpc'),weight_field=None).save(str(code)+str(redshift)+'complete-density.png')
    ProjectionPlot(ds, 2, 'temperature', width=(25.0, 'mpc'),weight_field=None).save(str(code)+str(redshift)+'complete-temperature.png')
    
