'''
This first reads in a tab delimitated file with genus and family names, then it reads in a list a species/seq codes in the format
[family_]genus_species_ID and outputs a tab separated list with ID, family (looked up from genus), genus, species. Family is not
present in all codes as input.
'''


import fileinput
import os
import sys

def main():
    endl = os.linesep
        
    familyfile="genus_family"
    genusFamily = {}
    with open(familyfile) as f:
        for line in f:
           (key, val) = line.strip(endl).split('\t')
           if key in genusFamily:
               sys.exit("ERROR: duplicate genus names found in file: "+familyfile)
           genusFamily[key] = val
    #print genusFamily

    for line in fileinput.input():
        genus = line.strip(endl).split("_")[-3]
        species = line.strip(endl).split("_")[-2]
        seqid = line.strip(endl).split("_")[-1]
        if genus not in genusFamily:
               sys.exit("ERROR: Genus name found that was not in the genus-family lookup list. Problem genus: "+genus+" Full line: "+line)
        print seqid+"\t"+genusFamily[genus]+"\t"+genus+"\t"+species
        #print len(line.strip(endl).split("_"))  #Use for printing number of fields split to find mis-splits by eye
        
if __name__ == '__main__':
    main()
