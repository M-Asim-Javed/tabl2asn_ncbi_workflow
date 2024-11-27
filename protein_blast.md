## Downloading and making custom protein blast database using UniprotTrEMBL database using Diamond

```bash
diamond makedb --in uniprot_trembl.fasta -d uniprot_trembl --threads 20


# protein blast again custom database

diamond blastp -q PBTT_proteins_longest_isoform.fasta \
               -d uniprot_trembl.dmnd \
               -o results.tsv \
               -f 6 qseqid sseqid pident length evalue bitscore \
               --threads 40 \
               --evalue 1e-5 \
               --max-target-seqs 1

```
