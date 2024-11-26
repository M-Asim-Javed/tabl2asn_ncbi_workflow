# Blast the final protein sequencea agaisnst the UniProt/TrEMBL database and extracted the query and protein names and query match

## python script to manage the blast results in txt file and remove irrelavant information of mapping
```python
def extract_protein_info(input_file, output_file):
    """
    Extract Query, Protein_Name, and Match_Accession from a tab-separated file.

    :param input_file: Path to the input file containing protein data.
    :param output_file: Path to save the filtered output.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Write header
        outfile.write("Query\tProtein_Name\tMatch_Accession\n")

        # Skip the header line in the input file
        next(infile)

        for line in infile:
            # Split line into fields
            fields = line.strip().split("\t")

            # Extract the required fields
            query = fields[0]
            protein_name = fields[2].split("OS=")[0].strip()
            match_accession = fields[2].split("GN=")[1].split(" ")[0].strip()

            # Write to output file
            outfile.write(f"{query}\t{protein_name}\t{match_accession}\n")


# Define file paths
input_file = "filtered_genes.txt"  # Replace with your actual input file
output_file = "filtered_protein_data.txt"  # Replace with your desired output file

# Run the function
extract_protein_info(input_file, output_file)

print(f"Filtered protein information saved to {output_file}")
```
## python script to extract only the query, protein names and matching accesion from the arranged txt file.

```python
def extract_protein_info(input_file, output_file):
    """
    Extract Query, Protein_Name, and Match_Accession from a tab-separated file.

    :param input_file: Path to the input file containing protein data.
    :param output_file: Path to save the filtered output.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Write header
        outfile.write("Query\tProtein_Name\tMatch_Accession\n")

        # Skip the header line in the input file
        next(infile)

        for line in infile:
            # Split line into fields
            fields = line.strip().split("\t")

            # Extract the required fields
            query = fields[0]
            protein_name = fields[2].split("OS=")[0].strip()
            match_accession = fields[2].split("GN=")[1].split(" ")[0].strip()

            # Write to output file
            outfile.write(f"{query}\t{protein_name}\t{match_accession}\n")


# Define file paths
input_file = "filtered_genes.txt"  # Replace with your actual input file
output_file = "filtered_protein_data.txt"  # Replace with your desired output file

# Run the function
extract_protein_info(input_file, output_file)

print(f"Filtered protein information saved to {output_file}")
```
