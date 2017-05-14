for filename in [k_out_Cluster_]*.fa
do
    belvu -o tree $filename > belvu_$filename.txt
done
