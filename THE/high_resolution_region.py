import numpy as np  
from yt_lib_opt import compose_data as cd

stat_file = open('enzofile.txt','r')
CoM_file = cd.get_output_file_name('enzo','com',1.0)
CoM_data = cd.format_data(CoM_file, file_unit_type='length', tuple_data='list')

print len(CoM_data)

file_lines=[]
for line in stat_file:
    l=line.split()
    file_lines.append(l)

variables = file_lines[0]
spacing = file_lines[1]
file_lines.remove(variables)
file_lines.remove(spacing)

#### Making a dictionary ####
data = {}
h,tm,bm,pm,sm=[],[],[],[],[]
for x in xrange(0,len(file_lines)):
    halo=file_lines[x][0][1:-1]
    total_mass=file_lines[x][1]
    baryon_mass=file_lines[x][3]
    particle_mass=file_lines[x][5]
    star_mass=file_lines[x][7][:-1]
    
    h.append(halo)
    tm.append(total_mass)
    bm.append(baryon_mass)
    pm.append(particle_mass)
    sm.append(star_mass)

data = {str(variables[0][:-1]):h,
        str(variables[1][:-1]):tm,
        str(variables[2][:-1]):bm,
        str(variables[3][:-1]):pm,
        str(variables[4]):sm}

haloswithstellarmass=[]
for mass in sm:
    if (mass!='0'):
        haloswithstellarmass.append(sm.index(mass))

centers=[]
for halos in haloswithstellarmass:
    #print halos
    centers.append(CoM_data[halos])

#print centers[1][0]
#print
#print len(centers)
print len(haloswithstellarmass)

x,y,z=[],[],[]
for i in xrange(0,len(haloswithstellarmass)):
    x.append(centers[int(i)][0])
    y.append(centers[int(i)][1])
    z.append(centers[int(i)][2])

#print x

xmin,xmax = min(x),max(x)
ymin,ymax = min(y),max(y)
zmin,zmax = min(z),max(z)

#print xmax,xmin
#print ymax,ymin
#print zmax,zmin

x_range = xmax-xmin
y_range = ymax-ymin
z_range = zmax-zmin

inrange=[]
for values in CoM_data:
    if ((values[0] > xmin) and (values[0] < xmax)) and ((values[1] > ymin) and (values[1] < ymax)) and ((values[2] > zmin) and (values[2] < zmax)):
	inrange.append(values)

print len(inrange)


comrange=[]
for values in CoM_data:
    if (values[0] > xmin):
	if (values[0] < xmax):
	    if (values[1] > ymin): 
		if (values[1] < ymax):
                    if (values[2] > zmin): 
			if (values[2] < zmax):
			    #print "yes"
			    comrange.append(values)
    #else:
	#print 'no'
print len(comrange)



