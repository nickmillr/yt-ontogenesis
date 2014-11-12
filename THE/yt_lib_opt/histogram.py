from yt import *
import numpy as np  
import matplotlib as mpl
mpl.use("Agg") 
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm

import compose_data as cd
import output_halo_properties as hp


#from yt.mods import *
from yt.pmods import *

def bar_histogram(code,r,bins=30)
	
    #loads the file containing the masses for code
    mass_file = cd.get_output_file_name(code=code,attribute='tm',redshift=r)
    #remove units from data with 'Msun' unit attached
    mass_data = cd.format_data(load_file=mass_file, file_unit_type='mass', tuple_data='no')
    x = [float(i) for i in mass_data]
    #Take the log base 10 of the masses
    logx = np.log10(x)

    ######################################
    # Plot with solid bars and curve fit #
    ######################################

    plt.figure(figsize=(15,10))

    # best fit of data
    (mu, sigma) = norm.fit(logx)

    # the histogram of the data (n=logx bins=bins)
    n, bins, patches = plt.hist(logx, int(bins), normed=1, facecolor='green', alpha=0.75)

    # add a 'best fit' line
    y = mlab.normpdf(bins, mu, sigma)
    l = plt.plot(bins, y, 'r--', linewidth=2)

    #plot
    plt.xlabel('Msun')
    plt.ylabel('RFrequency')
    plt.title('Histogram of Mass distribution for %s %s' %(code,r))
    plt.grid(True)
    plt.savefig(str(code)+str(r)+str(bins)+'barhist.png')


def log_histogram(code,r,bins=30):

    #loads the file containing the masses for code
    mass_file = cd.get_output_file_name(code=code,attribute='tm',redshift=r)
    #remove units from data with 'Msun' unit attached
    mass_data = cd.format_data(load_file=mass_file, file_unit_type='mass', tuple_data='no')
    x = [float(i) for i in mass_data]
    #Take the log base 10 of the masses
    logx = np.log10(x)

    #######################################
    # Plot with dashed bars and curve fit #
    #######################################
    
    plt.figure(figsize=(15,10))
    
    # best fit of data
    (mu, sigma) = norm.fit(logx)

    # the histogram of the data (n=logx bins=bins)
    n, bins, patches = plt.hist(logx, int(bins), normed=1, facecolor='green', alpha=0.75)

    # add a 'best fit' line
    y = mlab.normpdf( bins, mu, sigma)
    l = plt.plot(bins, y, 'r--', linewidth=2)

    #plot
    plt.xlabel('Msun')
    plt.ylabel('RFrequency')
    plt.title('Histogram of Mass distribution for %s %s' %(code,r))
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(left=0, right=14)
    plt.grid(True)
    plt.savefig(str(code)+str(r)+str(bins)+'loghist.png')

def multiple_data_hist(code_list, same_plot='yes')
    r"""" 
	Insert list of code and redshift [('enzo', 1.0), ('ramses', 1.0), ('enzo', 2.0)] 
    """"
    code = []
    redshift = []
    for i in xrange(0,len(code_list)):
	x=(list(code_r[i]))
	code.append(x[0])
	redshift.append(x[1])
	
    if (same_plot=='yes'):
	print "you havent made this func yet nick"

    elif (same_plot=='no'):
	for j in xrange(0,len(code_list)):
	    log_histogram(code=code[j],r=redshift[j])
	    bar_histogram(code=code[j],r=redshift[j])	
	return


