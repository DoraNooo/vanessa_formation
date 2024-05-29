from Bio import SeqIO

with open("test.fastq") as handle:
    for record in SeqIO.parse(handle, "fastq"):
        print(str(record.seq))
        print(record.id)