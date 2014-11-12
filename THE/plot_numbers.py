from yt import * 
from yt.mods import * 
import numpy as np
from yt_lib_opt import mass_functions as mf

def main():
   # you can input a range as a list: halos=[0,15]  
   a=mf.mstar_mhalo('ramses',1.0,halos=[640,650])
main()
