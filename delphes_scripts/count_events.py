import uproot3
import glob

f = open('dirlist','r')
dirlist = f.read().splitlines()
print("Directories to count : ",dirlist)

nef = open('Num_of_Delpy_Events.txt','w')
efl = open('Empty_File_list.txt','w')

for dirname in dirlist:
	file_path = "./" + dirname
	file_name = file_path + "/Del_Out/"+"*.root"
	HT_list = glob.glob(file_name)
	print("Start counting " + dirname)

	num_events = 0
	empt_list = list()

	for f in HT_list:
		file_ = uproot3.open(f)
		if len(file_) == 2:
			tree = file_['Delphes']
			num_events += len(tree)
		else:
			empt_list.append(f)
			dat_efl = "{0}\n".format(f)
			efl.write(dat_efl)
	print("Num events of " + dirname + " is " , num_events)
	print("Empty files : " , empt_list)
	data = "{0},{1}\n".format(dirname,num_events)
	nef.write(data)
nef.close()
efl.close()
#file_path = "/x4/cms/jyshin/condorDelPyOut/"
#file_name = file_path + "DelPy_events_" + "*.root"
#HT_list = glob.glob(file_name)
#print("start" )
#
#sum_ = 0
#empt_list = list()
#for f in HT_list:
#	file_ = uproot3.open(f)
#	if len(file_) ==2:
#		tree = file_['Delphes']
#		sum_ += len(tree)
#	else:
#		empt_list.append(f)
#print(sum_)
#print(empt_list)
#



#HT50_list = glob.glob(path_HT50)
#
#sum_=0
#for f in HT50_list:
#	tree = uproot.open(f)
#	
#	sum_ += len(tree)
#print(sum_)
