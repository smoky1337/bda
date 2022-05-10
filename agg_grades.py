import sys
import os
inp_fs, out_f = sys.argv[1:]

inputs = {}
for files in os.listdir(inp_fs):
    with open(os.path.join(inp_fs,files)) as f:
        lines = f.readlines()
        info = [line.split("\t") for line in lines]
        
        for s in info:
           if s[0] in inputs:
                p = inputs[s[0]]
                inputs[s[0]] = {"courses": p["courses"] + float(s[1]), "grade": p["grade"] + float(s[2])}
           else:
                inputs[s[0]] = {"courses": float(s[1]), "grade":float(s[2])}
        
    break # because we can't get the workflow running  
    
for s in inputs:
    t = inputs[s]
    avg = t["grade"] / t["courses"]
    inputs[s] = avg

with open(out_f, "a+") as f:
    for s in inputs:
        f.write(f"{s}\t{inputs[s]}\n")
