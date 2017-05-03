cd ~/Documents/projects/SU_comparative_genomics/data/2017-05-03/grp7/
blastall -p blastp -d /path/uniprot -i 05.fa.txt
blastall -p blastp -d /path/uniprot -i 09.fa.txt
blastall -p blastp -d /path/uniprot -i 11.fa.txt
blastall -p blastp -d /path/uniprot -i 12.fa.txt
blastall -p blastp -d /path/uniprot -i 28.fa.txt

#Know when the iterations are done we will echo:
echo 'BLAST run is complete'

# Move all the files from the data_files folder to a psiblast_output folder (as desired)
cd ~/Documents/projects/SU_comparative_genomics/results/2017-05-03/


mv *.pssm ~/Documents/projects/SU_comparative_genomics/results/2017-05-03/
