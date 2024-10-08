# Cheking the presence and absence of start amino acid methionine (M) from the protein .fa file

from Bio import SeqIO

def find_missing_start_codon(fasta_file, output_file):
    """Find protein sequences that do not start with Methionine (M)"""
    missing_start_codon = []

    # Read the protein sequences from the FASTA file
    with open(fasta_file, 'r') as infile:
        for record in SeqIO.parse(infile, 'fasta'):
            seq_id = record.id
            sequence = str(record.seq)

            # Check if the first character of the sequence is not 'M'
            if not sequence.startswith('M'):
                missing_start_codon.append(seq_id)

    # Write the IDs of sequences without 'M' to the output file
    with open(output_file, 'w') as outfile:
        for seq_id in missing_start_codon:
            outfile.write(f"{seq_id}\n")

    print(f"Found {len(missing_start_codon)} sequences without a start codon 'M'.")
    print(f"Results saved to {output_file}")

# Input and output file paths
input_fasta_file = 'braker.aa'  # Replace with your input FASTA file
output_file = 'braker_missing_start_codon.txt'  # Replace with your desired output file

# Run the script
find_missing_start_codon(input_fasta_file, output_file)
