from yt.mods import *
from yt.analysis_modules.halo_finding.api import *
import load_dataset

pf = load_data(enzo, 1.0)
haloes = HaloFinder(pf)
haloes.dump("basename")

###############################################################
#  To load off disk now after this scipt is run, the do this: #
#        from yt.mods import *                                #
#        from yt.analysis_modules.halo_finding.api import *   #
#        pf = load("data0001")                                #
#        haloes = LoadHaloes(pf, "basename")                  #
###############################################################

# This creates three very large 'basename' files '.out', '.txt' and .'h5'

# <link>
# http://yt-project.org/docs/dev-3.0/analyzing/analysis_modules/running_halofinder.html?highlight=halo_list

