

for i in $(ls ../Events | grep "decayed") ;do

	cp ../Events/${i}/events_PYTHIA8_0.hepmc.gz ./${i}.hepmc.gz
	echo "${i}/events_PYTHIA8_0.hepmc.gz is coppied"

done

for j in $(ls | grep "gz") ; do

	gzip -d ${j} 
	echo "${j} unzipped"
done
