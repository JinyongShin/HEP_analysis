for i in $(ls | grep "hepmc") ; do
	/home/jyshin/530SPACE/MG5_aMC_v2_8_2/Delphes/DelphesHepMC /home/jyshin/530SPACE/MG5_aMC_v2_8_2/Delphes/cards/delphes_card_CMS.tcl ${i%.*}.root ${i} 
	#echo ${i%.*}.root
done

