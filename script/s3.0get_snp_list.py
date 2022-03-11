# argv[1]:fastGWAA(gcta) argv[2]:output_path argv[3]:pvalue
import os
from sys import argv
import csv
pvalue = float(argv[3])
snp_list=[]
with open(argv[1]) as f:
    reader =csv.reader(f,delimiter='\t')
    header = next(reader)
    for i,line in enumerate(reader):
        d = dict(zip(header,line))
        if int(d['CHR'])<=22:
            if float(d["P"])<=pvalue:
                snp_list.append(d["SNP"])
print(pvalue,len(snp_list))
with open(argv[2],"w") as fw:
    for snp in snp_list:
        fw.write(snp+"\n")
print("Done")