
```python
import re

def is_valid_locus_tag(locus_tag):
    """
    Check if the locus tag starts with PBTT_ and is within the valid range.
    Valid locus tags are between PBTT_00001 and PBTT_10521.
    """
    # Check if the tag starts with "PBTT_"
    if not locus_tag.startswith("PBTT_"):
        return False
    
    # Extract the numerical part and check if it's within range
    try:
        tag_number = int(locus_tag.split("_")[1])
        if 1 <= tag_number <= 10521:
            return True
    except (IndexError, ValueError):
        return False

    return False

def process_tbl_file(input_tbl_file, output_tbl_file):
    """
    Process the input .tbl file and remove lines with invalid locus tags.
    Only keep lines with valid locus tags (PBTT_00001 to PBTT_10521).
    """
    with open(input_tbl_file, 'r') as infile, open(output_tbl_file, 'w') as outfile:
        # Read the file line by line
        for line in infile:
            # Match lines that contain gene names like "gene-XXX"
            match = re.search(r'gene-\d+', line)
            if match:
                # Extract the gene ID
                gene_id = match.group(0)
                # Check if it's a valid PBTT_ locus tag
                if not gene_id.startswith('PBTT_'):
                    print(f"Removing invalid gene: {gene_id}")
                    continue  # Skip the line if it's an invalid gene ID
                else:
                    outfile.write(line)
            else:
                outfile.write(line)  # Write other lines as they are

    print(f"Processed file saved to {output_tbl_file}")

# Input and output file paths
input_tbl_file = 'feature_table_file.tbl'  # Replace with the path to your input .tbl file
output_tbl_file = 'corrected_locus_tag.tbl'  # Replace with the path to the cleaned output .tbl file

# Run the script to clean the .tbl file
process_tbl_file(input_tbl_file, output_tbl_file)
```
