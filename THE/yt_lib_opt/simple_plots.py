
from yt import *
import load_dataset as ld

def simulation_plot(code,redshift):
    ds=ld.load_data(code, redshift)

    ProjectionPlot(ds, 2, 'density', width=(25.0, 'Mpc'),weight_field=None).save(str(code)+str(redshift)+'complete-density-25.png')
    ProjectionPlot(ds, 2, 'temperature', width=(25.0, 'Mpc'),weight_field=None).save(str(code)+str(redshift)+'complete-temperature-25.png')
    
    ProjectionPlot(ds, 2, 'density', width=(45.0, 'Mpc'),weight_field=None).save(str(code)+str(redshift)+'complete-density-45.png')
    ProjectionPlot(ds, 2, 'temperature', width=(45.0, 'Mpc'),weight_field=None).save(str(code)+str(redshift)+'complete-temperature-45.png')

    ProjectionPlot(ds, 2, 'density', width=(25.0, 'Mpc'),weight_field='cell_mass').save(str(code)+str(redshift)+'complete-weight-cellmass-25.png')
    ProjectionPlot(ds, 2, 'density', width=(25.0, 'Mpc'),weight_field='density').save(str(code)+str(redshift)+'complete-weight-density-25.png')
    ProjectionPlot(ds, 2, 'density', width=(25.0, 'Mpc'),weight_field='temperature').save(str(code)+str(redshift)+'complete-weight-temperature-25.png')
    #ProjectionPlot(ds, 2, 'density', width=(25.0, 'Mpc'),weight_field='Pressure').save(str(code)+str(redshift)+'complete-weight-pressure-25.png')
