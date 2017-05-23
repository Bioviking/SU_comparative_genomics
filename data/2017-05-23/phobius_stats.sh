export phobius=/afs/pdc.kth.se/home/e/erison/Public/bin/phobius/1.01/phobius

for filename in *.fa.txt.pfa
do
    if [ ! -f out_phob_$filename.txt ] ; then
        $phobius -short ./$filename > out_phob_$filename.txt   
    fi
    done
done
