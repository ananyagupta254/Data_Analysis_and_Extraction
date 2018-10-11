# Cleaning raw data in the file
# Regular expression to extract data from the given file

import re #to import file of regular expressions
#to open files
fp = open("geoprofiles_result_LC.txt", 'r') # to read file with given filename
wf = open("geoprofiles_result_LC_cleaned_using_RegEx.txt", 'w') # to write file 
# to write headings on the first line of newly created file
data = ('SI#\tGene\tGDS\tOrganism\tsample no.\n')
wf.write(data)
wf.flush()
print(data)

SI = 1 # initialization of SI#
fp.readline()
#looping to iterate through whole lines
for line in fp:
    # to find the gene name from the line and given pattern
    pattern1 = r'(\d+\.\s)(\w+\-*\w+)'#pattern of "[0-9] followed by . followed by space followed by [a-zA-Z0-9]
    temp1 = re.search(pattern1, line) # search the pattern in the given sequence
    line = fp.readline()
    pattern2 = r'(Annotation:\s)(\w+\-*\w+)'
    
    if re.match(pattern2, line):
        gene2 = re.search(pattern2, line).group(2)
    else:
        gene2 = 'Null'
    
    if temp1.group(2) == gene2:
        gene_name = temp1.group(2)
    else:
        gene_name = 'Null'
        print(gene_name)

    #to find the organism name from given sample
    line = fp.readline()
    pattern = r'(Organism:\s)(\w+\s\w+)' 
    org_name = re.search(pattern, line).group(2)
    print(org_name)

    #to find the GDS number from the given sample
    line = fp.readline()
    pattern = r'(GDS\d+)'
    GDS_num = re.search(pattern, line).group(1)
    print(GDS_num)

    #to find the number of samples
    line = fp.readline()
    pattern = r'(\d+)(\ssamples)'
    sample_num = re.search(pattern, line).group(1)
    print(sample_num)
   
    result = '{0}\t{1}\t{2}\t{3}\t{4}\n'.format(SI, gene_name, GDS_num, org_name, sample_num)
    print(result)
    wf.write(result)
    wf.flush()
    SI += 1
    fp.readline()
    fp.readline()
fp.close()
wf.close()
    

    
    
