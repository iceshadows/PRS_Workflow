'''
argv[1] : UKB pheno
argv[2] :field ID
'''
import pandas as pd
import csv
from sys import argv
import os
import numpy as np
rs = {
    "sid":[],
    "code":[]
}
with open(argv[1],"r") as f:
    reader = csv.reader(f)
    header = next(reader)
    fields =[]
    for field in header:
        if argv[2]+"-" in field:
            fields.append(field)
    for i,r in enumerate(reader):
        if i % 100==0:
                print(i,"/","502462")
        for field in fields:
            field = header.index(field)
            coding = r[field]
            eid = r[0]
            if coding !="":
                #print(coding,eid)
                rs["sid"].append(eid)
                rs["code"].append(coding)
            else:
                pass
df = pd.DataFrame(rs)
df.to_csv(os.path.join("../",argv[2]+".csv"),index=None)
# np.savez_compressed(argv[2]+".npz",sid=rs["sid"],code=rs["code"])
print("Done")
