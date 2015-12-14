#!/usr/bin/env python

# Takes two input files
# - A tab delminiated file ("id_family_genus_species_dup_rem") containing Sequence ID, family, genus, sepcies
# - The tab delminated output ("all.out") from a blastn query (use: -outfmt '6 qseqid sseqid evalue bitscore pident')
#   Sequence ID comes after the final _ in the seuqnce name
#   (e.g. Sequence name is "Hypochilus_thorelli_GBCH2390-08", Sequence ID is GBCH2390-08)

# Outputs two tab delminiated tables to stdout:
# - information about each hit for each query (excludes when query ID matches hit ID)
# - Summary of genus and family matches for each query (not including when query matches hit)

import os
import sys
import csv

def main():
    endl = os.linesep
    
    #Read in file with ID, family, genus, species
    IDCodes= {}
    IDCodesFile = "id_family_genus_species_dup_rem"
    with open(IDCodesFile) as tsv:
        for line in csv.reader(tsv, delimiter="\t"):
            if line[0] in IDCodes:
                sys.exit("ERROR: duplicate ID found: "+line[0])
            IDCodes[line[0]]={}
            IDCodes[line[0]]["family"]=line[1]
            IDCodes[line[0]]["genus"]=line[2]
            IDCodes[line[0]]["species"]=line[3]
    #print IDCodes
    
    #Count of each genus and number of IDs into GenusCount
    GenusCount={}
    for ID in IDCodes:
        genus = IDCodes[ID]['genus']
        if genus not in GenusCount:
            GenusCount[genus] = 1
        else:
            GenusCount[genus] = GenusCount[genus] + 1
    #print GenusCount

    #Count of each family and number of IDs into FamilyCount
    FamilyCount={}
    for ID in IDCodes:
        family = IDCodes[ID]['family']
        if family not in FamilyCount:
            FamilyCount[family] = 1
        else:
            FamilyCount[family] = FamilyCount[family] + 1
    #print FamilyCount


    
    #
    #Read in blast output in tabular format (qseqid sseqid evalue bitscore pident)
    #
    
    BLASTOutput = "all.out" #input for this program
    SummaryResults = [] #This will output the summary for each query of number of family/genus hits
    PrevQuery = ""
    
    print "QueryID	QueryFamily	QueryGenus	QuerySpecies	HitRank	SubjectFamily	SubjectGenus	SubjectSpecies	SubjectID	Evalue	Bitscore	Pident	FamilyMatch	GenusMatch	SpeciesMatch"
    with open(BLASTOutput) as tsv:
        for line in csv.reader(tsv, delimiter="\t"):
            #Get Query and Subject IDs (after last _)
            QueryID=line[0].split("_")[-1]
            if QueryID not in IDCodes:
                sys.exit("ERROR: QueryID not found: "+QueryID)

            #Counter of hit number, QueryID will be the same for a series of hits then change with the next query start 
            if QueryID != PrevQuery:
                PrevQuery = QueryID
                HitCount=1
            else:
                HitCount+=1

            SubjectID=line[1].split("_")[-1]
            if SubjectID not in IDCodes:
                sys.exit("ERROR: SubjectID not found: "+SubjectID)
            if len(SummaryResults) == 0 or SummaryResults[-1]["QueryID"] != line[0]:
                SummaryResults.append({})
                SummaryResults[-1]["QueryID"]=line[0]
                SummaryResults[-1]["genus"]=IDCodes[QueryID]["genus"]
                SummaryResults[-1]["family"]=IDCodes[QueryID]["family"]
                SummaryResults[-1]["species"]=IDCodes[QueryID]["species"]
                SummaryResults[-1]["familymatch"]=0
                SummaryResults[-1]["genusmatch"]=0
                SummaryResults[-1]["hitcount"]=0
                SummaryResults[-1]["genuscount"]=GenusCount[SummaryResults[-1]["genus"]]
                SummaryResults[-1]["familycount"]=FamilyCount[SummaryResults[-1]["family"]]
            if SubjectID==QueryID:
                continue
            #Add new columns with family, genus, species
            line.insert(1,IDCodes[QueryID]["family"])
            line.insert(2,IDCodes[QueryID]["genus"])
            line.insert(3,IDCodes[QueryID]["species"])
            line.insert(4,str(HitCount))
            line.insert(5,IDCodes[SubjectID]["family"])
            line.insert(6,IDCodes[SubjectID]["genus"])
            line.insert(7,IDCodes[SubjectID]["species"])
            #Add new column with family match (0 or 1)
            if IDCodes[QueryID]["family"] == IDCodes[SubjectID]["family"]:
                FamilyMatch="1"
                SummaryResults[-1]["familymatch"] += 1
            else:
                FamilyMatch="0"
            #Add new column with genus match (0 or 1)
            if IDCodes[QueryID]["genus"] == IDCodes[SubjectID]["genus"]:
                GenusMatch="1"
                SummaryResults[-1]["genusmatch"] += 1
            else:
                GenusMatch="0"
            line.append(FamilyMatch)
            line.append(GenusMatch)
            
            #Check if species matches
            if IDCodes[QueryID]["genus"]+IDCodes[QueryID]["species"]==IDCodes[SubjectID]["genus"]+IDCodes[SubjectID]["species"]:
                line.append("1")
            else:
                line.append("0")

            print "\t".join(line)
            SummaryResults[-1]["hitcount"]+= 1
    
    #
    # Output the summary table
    #
    
    print "QueryID	QueryFamily	QueryGenus	QuerySpecies	FamilyMatch	GenusMatch	HitCount	FamilyCount	GenusCount"    
    for line in SummaryResults:
        print str(line["QueryID"])+"\t"+str(line["family"])+"\t"+str(line["genus"])+"\t"+str(line["species"])+"\t"+str(line["familymatch"]/float(line["hitcount"]))+"\t"+str(line["genusmatch"]/float(line["hitcount"]))+"\t"+str(line["hitcount"])+"\t"+str(line["familycount"])+"\t"+str(line["genuscount"])


if __name__ == '__main__':
    main()
