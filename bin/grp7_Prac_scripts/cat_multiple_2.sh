grep ">./05.fa.txt_orf00935_rev" $(find . -name 'Cluster_*') > 05genes.txt

grep ">./09.fa.txt_" $(find . -name 'Cluster_*') > 09genes.txt
grep ">./11.fa.txt_" $(find . -name 'Cluster_*') > 11genes.txt
grep ">./12.fa.txt_" $(find . -name 'Cluster_*') > 12genes.txt






find . -name 'Cluster_*'


find . -name 'Cluster_*'
for filename in [Cluster_]*.txt
do
    python multigene_cat.py
done
