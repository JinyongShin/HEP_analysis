
mkdir HEPMCF DelRootF

#source getXsec.sh

source getHEPMC.sh

#source rename_shower.sh 

source ShowerExAnal.sh

#python make_run_xsec_table.py

mv *.hepmc HEPMCF/
mv *.root DelRootF/

echo "BLOjob-shower_detector_level Finished"
