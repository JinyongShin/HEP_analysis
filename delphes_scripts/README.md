### Analysis for simulated Events After Detector simulation.

count_events.py


	--> This code considers the case where the file is stored in the Del_Out directory
	under the directories in the list you made.

	--> requirements : uproot3

	--> usage

		1. You need to make list of your directories which contain your root files.
		name the list file as 'dirlist'(or change code.).
			
		2. count_events.py , dirlist , dir must be in same directory.
		3. If you are ready, just run this code ! (python count_events.py)

		4. Number of Events for each directories will be printed.
   		Also, Num_of_Delpy_Events.txt  and Empty_File_list.txt will be created.
   		Num_of_Delpy_Events.txt : directory names,number of events in the directory
   		Empty_File_list.txt : list of empty root files. 
