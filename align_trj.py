def ReadList(filename):
  fin = open(filename, "r")
  SelectionList = [line.rstrip() for line in fin]
  return SelectionList

from MDAnalysis import *
from MDAnalysis.analysis.align import *
import sys
import time
import argparse

time_start = time.clock()

parser = argparse.ArgumentParser()
parser.add_argument("-ref", "--reference"  , required = True)
parser.add_argument("-trj", "--trajectory" , required = True)
parser.add_argument("-p"  , "--prefix"     , required = True)
parser.add_argument("-s"  , "--selection"  , required = True)
args = parser.parse_args()

#***Parse here
ref_filename       = args.reference
trj_fileList       = args.trajectory
selectionList_file = args.selection
fout_name          = args.prefix

print "REF FILE NAME   :", ref_filename
print "TRJ FILE NAME   :", trj_fileList
print "SELECTION FILE  :", selectionList_file
print "OUTPUT FILE NAME(rmsd):", fout_name

trjList       = ReadList(trj_fileList)
selectionList = ReadList(selectionList_file)

for i, line in enumerate(trjList):
    print "TRJ LIST  : ", i, line
print "SELECTION LIST: ", selectionList

ref = Universe(ref_filename)
for i, trj_filename in enumerate(trjList):
    print "FILE NAME :", i, trj_filename
    trj = Universe(trj_filename)

    rms_fit_trj(trj,ref, select=(selectionList,selectionList),rmsdfile="%s%s.dat"%(fout_name,i))
    time_elapsed = (time.clock() - time_start)
    print "PROGRESS: ", time_elapsed

print "COMPUATION TIME: ", time_elapsed
