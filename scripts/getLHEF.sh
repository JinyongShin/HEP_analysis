

for i in $(ls ../Events | grep "decayed") ;do

	cp ../Events/${i}/events.lhe.gz ./${i}.lhe.gz
	echo "${i}/evnts.lhe.gz is coppied"

done

for j in $(ls | grep "gz") ; do

	gzip -d ${j} 
	echo "${j} unzipped"
done
