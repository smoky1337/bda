import sys
import pandas as pd
in_f, out_f = sys.argv[1:]
with open(in_f) as inp:
    lines = inp.readlines()
    lines =  [s.split("\t") for s in lines]
    data = pd.DataFrame(lines, columns = ["id","course","grade"])
    data = data.astype({"id":"int32", "grade":"float"})
    s = data.groupby("id").agg({"course": "count", "grade": "sum"})
with open(out_f, "a+") as out:
    [out.write(f"{i}\t{c}\t{g}\n") for i,c,g in zip(s.index, s.values[:,0], s.values[:,1])]





