import glob
import uproot
import pandas as pd

## -- Read root fuiles
files = glob.glob('*.root')


## -- Read Tree
print(" Scan TTrees..")
Total_N =0
for idx,f in enumerate(files):
	dat = uproot.open(f)['LHEF']
	file_N = dat.numentries
	Total_N += file_N
	f_name = f.split('/')[-1].split('.')[0]
	print(idx,f_name,file_N)
print("=== Summary === " )
print("Total {0} number of events / {1} files".format(Total_N,len(files)))


