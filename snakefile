import os
import re

IDS=['C:\Users\cmust\Desktop\BigData\exercises2\coursesTaken\coursesTaken\coursesTaken-A.csv']
chrs=range(1,10000)

rule all:
    input: expand("{id}_{chr}.csv", chr=chrs, id=IDS)

rule splitByChr:
    input:
        "{id}.csv"
    output:
        "{id}_{chr}.csv"
    shell:
        "bcftools view -H {input} -r {wildcards.chr} > {output}"




#question 4

rule plot_quals:
    input all:
        "C:\Users\cmust\Desktop\BigData\exercises2\coursesTaken\coursesTaken\.csv"
    output all:
        ""C:\Users\cmust\Desktop\BigData\exercises2\coursesTaken\coursesTaken\plot_.pdf""
    script:
        "scripts/plot-quals.py"



import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pysam import VariantFile

quals = [record.qual for record in VariantFile(snakemake.input[0])]
quals2 = [record.qual for record in VariantFile(snakemake.input[1])]

plt.hist(quals)
plt.hist(quals2)
plt.savefig(snakemake.output[0])
plt.savefig(snakemake.output[1])                