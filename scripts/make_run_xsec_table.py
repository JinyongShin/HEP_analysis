
import pandas as pd


### Revise rename.csv file to run_param.csv ###
f = open("rename.csv","r")

rf = f.read()

rf = rf.split('\n')

rf = ','.join(rf)

rf = rf.split(',')

rf = '.lhe'.join(rf)

rf = rf.split('.lhe')

run = "run"

runlist = list()
parmlist = list()

for i in rf:
	if run in i:
		runlist.append(i)
	else :
		parmlist.append(i)

parmlist = ' '.join(parmlist).split()

fr = open("run_param.csv","w+")
fr.write("Num_run , param_info\n")

for x in range(0,len(parmlist)):
        fr.write(runlist[x]+","+parmlist[x]+"\n" )

fr.close()


### reading csv file to match Xsection ###

name_info = pd.read_csv("run_param.csv")
xsec_info = pd.read_csv("Xsection.csv")

combined = pd.merge(name_info,xsec_info)

print(combined)

combined.to_csv("run_xsec.csv")
