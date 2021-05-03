
mkdir LHEF ROOTF CSVF

source getXsec.sh

source getLHEF.sh

source rename_gen.sh 

source ExAnal.sh

python make_run_xsec_table.py

mv *.lhe LHEF/
mv *.csv CSVF/
mv *.root ROOTF/

echo "BLOjob-gen_level Finished"
