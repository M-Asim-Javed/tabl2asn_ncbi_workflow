
# Workflow to submit the annoations files to NCBI using tabl2asn

## Convert the gtf file to gff3 file format

```bash
agat_convert_sp_gxf2gxf.pl --gff pb3A_gene.gtf -o pb3A_gene_agat.gff3

```

## To rearrange the gff3 file numerically

#### validate the gff3 file using online validator (https://genometools.org/cgi-bin/gff3validator.cgi)

#### Convert the gff3 file into feature table (.tbl) format for NCBI annotation submission using GAG script (https://genomeannotation.github.io/GAG/)

```bash
python2 gag.py --fasta GCA_036867785.1_ULAVAL_Pb3A_genomic.fsa --gff pb3A_sorted_corrected_annotations.gff3 --out gag_output

```
## To run the table2asn

```bash
./linux64.table2asn -M n -J -c w -euk -t edeLab.sbt -gaps-min 10 -l paired-ends -j "[organism=plasmodiophora brassicae] [isolate=pb3A]" -i ULAVAL_Pb3A_genomic.fsa -locus-tag-prefix PBTT -f pb3A_annotations.tbl -o output_file.sqn -Z -V b
```
