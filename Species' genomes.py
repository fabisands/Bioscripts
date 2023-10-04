# Compare and tell the percentage of coincidence of the genomes 2 species of bacteria: Bacteroides fragilis & Bacteroides melaninogenicus
# The FASTA sequences are taken from NCBI

from Bio import SeqIO

# Methods for reading FASTA files:
    # variable.read() --> puts the file data into one string variable
    # readline() --> one line + incremental reading of the file
    # readlines() --> returns the lines a list of strings
# Method to use: variable.read()

x = open(r'C:\Users\faren\OneDrive - Universidad de la Amazonia\Documents\VSCode files\Py-scripts\Genomes\Clostridium_perfringens.fna', 'r')
a = x.read()
x.close()
b = a[66:]
Clostridium_perfringens = b.replace("\n", "")
C_perfingens_size = len(Clostridium_perfringens)
print("The amount of nucleotides in the Clostridium perfringens genome is", C_perfingens_size)

y = open(r'C:\Users\faren\OneDrive - Universidad de la Amazonia\Documents\VSCode files\Py-scripts\Genomes\Clostridium_septicum.fna', 'r')
c = y.read()
y.close()
d = c[80:]
Clostridium_septicum = d.replace("\n", "")
C_septicum_size = len(Clostridium_septicum)
print("\nThe amount of nucleotides in the Clostridium septicum genome is", C_septicum_size)

# find and print the shortest one

if C_perfingens_size <= C_septicum_size:
    short_one = C_perfingens_size
else:
    short_one = C_septicum_size

print("\nThe first", short_one, "nucleotides of each chain will be taken since that is")
print("the amount to be compared from the shortest genome")

# Do the counting

count = 0
for i in range(C_perfingens_size):
    if Clostridium_perfringens[i] == Clostridium_septicum[i]:
        count += 1

# find and print the percentage of similarity

result = round(((count/short_one)*100), 2)

print("\nThe similarity percentage of the genomes of the Clostridium perfringens and")
print("Clostridium septicum species is", str(result) + "%")

