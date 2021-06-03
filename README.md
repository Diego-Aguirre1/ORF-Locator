# Open Reading Frame Locator

This program finds open reading frames (ORFs) in a DNA sequence. An Open Reading Frame begins with the "ATG" start codon and ends with one of three stop codons: "TAG", "TGA", or "TAA".

![alt text](https://github.com/Diego-Aguirre1/ORF-Locator/blob/main/demo/demo.gif)

It returns the locations of the start and stop codon along with the length of the ORF. You may also change the searching frame of the sequence from 1, 2, or 3. 

You may upload a .FASTA or .txt file of a nucleotide sequence to determine the amount of ORFs. For this example, I have used the SARS-CoV-2 viral sequence from NCBI (https://www.ncbi.nlm.nih.gov/nuccore/NC_045512). 

To download the sequence:
1. Click on **Send to**
2. **Complete Record**
3. **File**
4. **Format**
5. **FASTA**
6. **Create File**