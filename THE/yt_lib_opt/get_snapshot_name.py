import os as os
import glob as glob
import numpy as np
import yt.mods as ytm

def RyanMW_wildcard_files(code):
    #this should be done with a dictionary
    scylla_dir="/home/share/astro/Data/scylla/"
    rmw_dir=scylla_dir+"Ryan_MW/"
    codes=os.listdir(rmw_dir)
    if (code=='arepo'):
        code_dir=rmw_dir+"arepo/"
        file_wild=code_dir+"snapdir_???/snap_???.0.hdf5"
    if (code=='art'):
        code_dir=rmw_dir+"art/"
        file_wild=code_dir+"10MpcBox_csf512_a?.???.d"
    if (code=='changa'):
        code_dir=rmw_dir+"changa/"
        file_wild=code_dir+"TipsyGalaxy/galaxy.00300"
    if (code=='enzo'):
        code_dir=rmw_dir+'enzo/'
        file_wild=code_dir+'r00??/redshift00??'
    if (code=='gadget'):
        code_dir=rmw_dir+"gadget/"
        file_wild=code_dir+"snapdir_???/snapshot_???.0.hdf5"
    if (code=='ramses'):
        code_dir=rmw_dir+'ramses/'
        file_wild=code_dir+'output_00???/info_00???.txt'

    return(code_dir,file_wild)

def make_redshift_file(code):
    code_dir,file_wild=RyanMW_wildcard_files(code)
    files=sorted(glob.glob(file_wild))
    ts=ytm.DatasetSeries.from_filenames(file_wild)
    zfile=code_dir+"redshift.txt"
    f=open(zfile,'w')    
    fstart=len(code_dir)
    for i in xrange(len(ts)):
        z=ts[i].current_redshift
        z=np.absolute(np.round(100*z)/100.)
        f.write("{:2.2f}".format(z)+"   "+files[i][fstart:]+"\n")

    f.close()
    print "redshift.text written for "+code


def get_snapshot_name(code,z):
    #returns the file name for the given code and redshift
    code_dir,file_wild=RyanMW_wildcard_files(code)
    f=open(code_dir+'redshift.txt','r')
    zarray=[]
    names=[]
    for line in f:
        column=line.split()
        zarray.append(float(column[0]))
        names.append(column[1])

    f.close()
    zarray=np.array(zarray)
    idx=np.abs(zarray-z).argmin()
    fz=zarray[idx]
    if (np.abs(fz-z) > 0.1):
        print "Redshift {0} not found, using redshift {1} instead".format(z,fz)
    return code_dir+names[idx]
