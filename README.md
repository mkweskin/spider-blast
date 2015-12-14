#Scripts for spider blast hit preparation and parsing

These are scripts used in the preparation and parsing of blastn queries of spider COI barcode sequences.

## blast-parse.py

Takes two input files

- A tab delminiated file ("id_family_genus_species_dup_rem") containing Sequence ID, family, genus, sepcies
- The tab delminated output ("all.out") from a blastn query (use: -outfmt '6 qseqid sseqid evalue bitscore pident') Sequence ID comes after the final _ in the sequence name (e.g. Sequence name is "Hypochilus_thorelli_GBCH2390-08", Sequence ID is GBCH2390-08)

Outputs two tab delminiated tables to stdout:

- information about each hit for each query (excludes when query ID matches hit ID)
- Summary of genus and family matches for each query (not including when query matches hit)

##remove-dups.py

Removes sequences from a larger fasta file. The sequences listed in the exclude variable are already represented in the fasta file with another sample of this species. *requires [biopython](http://biopython.org)*

##split.py

This first reads in a tab delimitated file with genus and family names, then it reads in a list a species/seq codes in the format [family_]genus_species_ID and outputs a tab separated list with ID, family (looked up from genus), genus, species. Family is not present in all codes as input.
