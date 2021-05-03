
for i in $(ls | grep "lhe") ; do

        var1=$(cat $i | grep "MXd" | awk '{ print $2 }')
        var2=$(cat $i | grep "MY0" | awk '{ print $2 }')

        var3=$(echo $var1 | sed "s/[eE]\+/\*10\*\*/" | sed "s/\.000000//" )
        var4=$(echo $var2 | sed "s/[eE]\+.*//" | sed "s/\.000000//" )

        var3=$(echo "$(($var3))")
        var4=$(echo "$(($var4))")

        echo "${i}  >>>  MXd_${var3}_MY0_${var4}.root"
        /home/jyshin/530SPACE/MG5_aMC_v2_8_2/ExRootAnalysis/ExRootLHEFConverter ${i} MXd_${var3}_MY0_${var4}.root

done

