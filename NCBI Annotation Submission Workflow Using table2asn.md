
# NCBI Annotation Submission Workflow Using `table2asn`

This guide provides a streamlined workflow to prepare and submit genome annotations to NCBI using the `table2asn` utility. It includes steps to convert annotation formats, validate and sort features, and generate NCBI-compliant `.tbl` and `.sqn` files.

---

## Step 1: Convert GTF to GFF3 Format

Use AGAT (`agat_convert_sp_gxf2gxf.pl`) to convert your GTF annotation file into a GFF3-compliant format:

```bash
agat_convert_sp_gxf2gxf.pl --gff pb3A_gene.gtf -o pb3A_gene_agat.gff3
```

---

## Step 2: Validate and Sort the GFF3 File

Before proceeding, validate your `.gff3` file format:

* Online validator: [GenomeTools GFF3 Validator](https://genometools.org/cgi-bin/gff3validator.cgi)

If required, sort the GFF3 file numerically by gene coordinates to maintain structure consistency. This is especially important for downstream tools.

---

---
# Important Note!
## You can use either a GFF3 file or a feature table (.tbl) as input for table2asn, depending on your choice and can skip the .tbl options.
---
## Step 3: Generate a Feature Table (`.tbl`) Using GAG

This step is useful if you plan to submit the annotation separately to NCBI.

### Install GAG

Follow instructions from the GAG GitHub repository:
[https://genomeannotation.github.io/GAG/](https://genomeannotation.github.io/GAG/)

### Run GAG

```bash
python2 gag.py \
  --fasta GCA_036867785.1_ULAVAL_Pb3A_genomic.fsa \
  --gff pb3A_sorted_corrected_annotations.gff3 \
  --out gag_output
```

This will generate the `.tbl` file required by `table2asn`.

---

## Step 4: Install `table2asn`

```bash
wget ftp://ftp.ncbi.nlm.nih.gov/asn1-converters/by_program/table2asn/linux64.table2asn.gz
gunzip linux64.table2asn.gz
chmod +x linux64.table2asn
./linux64.table2asn --help
```

---

## Step 5: Run `table2asn` to Create the `.sqn` File

Use the command below to generate a Sequin (`.sqn`) file for submission:

```bash
./linux64.table2asn \
  -M n \
  -J \
  -c w \
  -euk \
  -t edeLab.sbt \
  -gaps-min 10 \
  -l paired-ends \
  -j "[organism=Plasmodiophora brassicae] [isolate=Pb3A]" \
  -i ULAVAL_Pb3A_genomic.fsa \
  -locus-tag-prefix PBTT \
  -f pb3A_annotations.tbl \
  -o output_file.sqn \
  -Z \
  -V b
```
# To get an .sbt above (submission template) file for use with table2asn, follow these steps:

---
Submission Portal

Go to the NCBI Submission Portal.

Start a new Genome Submission.

Fill out the requested metadata (organism name, isolate, sequencing platform, etc.).

Once you complete the metadata form, download the .sbt template file generated for your submission.

This will contain standardized fields like submitter, contact info, source modifiers, and qualifiers.
---
# Explanation of Common table2asn

```bash
-M n              # Do not modify the input files
-J                # Exclude gene features if no corresponding mRNA or CDS present
-c w              # Compliance level: w allows warnings, but generates output
-euk              # Indicates the genome is eukaryotic
-t edeLab.sbt     # Submission template (.sbt) file path
-gaps-min 10      # Minimum gap length before representing gaps with gap features
-l paired-ends    # Sequencing technology used
-j                # Source modifiers in square brackets (e.g., organism name, isolate)
-i                # Input FASTA file
-locus-tag-prefix # Prefix to prepend to locus tags
-f                # Feature table file (.tbl)
-o                # Output .sqn file
-Z                # Suppress automatic editing of some features
-V b              # Validation level: b for basic (output .val file with errors/warnings)

```
---

## Final Notes

* Ensure all locus tags are unique and properly formatted.
* Make sure the `.fsa`, `.tbl`, and `.sbt` files are consistent.
* Check the `.sqn` file using `tbl2asn` logs for validation errors or warnings.

For questions or issues, refer to the [NCBI Submission Guide](https://www.ncbi.nlm.nih.gov/genbank/genomesubmit/).
