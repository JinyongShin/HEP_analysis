
touch rename.csv

for i in $(ls | grep "lhe") ; do
        echo "${i} renaming "

        var1=$(cat $i | grep "MXd" | awk '{ print $2 }')
        var2=$(cat $i | grep "MY0" | awk '{ print $2 }')

        var3=$(echo $var1 | sed "s/[eE]\+/\*10\*\*/" | sed "s/\.000000//" )
        var4=$(echo $var2 | sed "s/[eE]\+.*//" | sed "s/\.000000//" )

        var3=$(echo "$(($var3))")
        var4=$(echo "$(($var4))")

#	var5=$(cat $i | grep "= nevents" | awk '{print $1 }')

        mv $i MXd_${var3}_MY0_${var4}.lhe
	echo "${i} , $(ls MXd_${var3}_MY0_${var4}.lhe)" >> rename.csv
#        echo "${i} , $(ls MXd_${var3}_MY0_${var4}.lhe) , nevents=${var5}" >> rename.csv

done

