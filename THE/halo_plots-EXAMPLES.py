from yt_lib_opt import halo_annotation as ha

def main():
    ha.halo_annotations('enzo',1.0,multiple_widths='yes',all_axis='yes')
    ha.halo_annotations('ramses',1.0,multiple_widths='yes',all_axis='yes')
main()
