#This program calculates RMSD using MDAnalysis module.

USAGE 

*Specify atoms, residues or regions that you wanna fit and calculate RMSD in "selection_list.inp" like: 

----------------------------- 
resid 1410-1935 and backbone 
resid 1936-3262 and backbone 
resid 3597-4729 and backbone 
----------------------------- 
The desctiption is based on the VMD syntax. 

*Specyfy paths for trajectory files 
*You can use align.py like: 
python align_trj.py -ref PATH_OF_REFERENCE_STRUCTURE 
                    -trj PATH_OF_INPUT_DESCRIBING_PATHS_FOR_TRAJECTORY_FILES \ 
                   --selection PATH_OF_INPUT_FOR_SELECTION \ 
                   --prefix "NAME_OF_OUTPUT_FILE_THAT_ILLUSTRATES_RMSD_VALUES_OF_EACH_STRUCTURE" 


