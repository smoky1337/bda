import sys
in_f, out_f = sys.argv[1:]
with open(in_f) as inp:
    lines = inp.readlines()

    lines =  [s.split("\t") for s in lines]
    lines = [t[0] for t in lines]

count = len(set(lines))
with open(out_f, "a+") as out:
    out.write(str(count))
