# Create a PCR simulator than amplifies a given DNA sequence through multiples reaction cycles.

import random

# Function to perform a single PCR reaction
def pcr_reaction(dna_sequence, temperature):
    amplified = ""
    for base in dna_sequence:
        if random.random() < 0.5:  # Probability of denaturation
            amplified += denaturalize(base)
        else:
            amplified += base
    return amplified

# Function to denature a DNA base
def denaturalize(base):
    if base == "A":
        return "T"
    elif base == "T":
        return "A"
    elif base == "G":
        return "C"
    elif base == "C":
        return "G"

# Initial DNA sequence
initial_sequence = input("Write a series of letters of nitrogenous bases (CGTA): ")

# Number of PCR cycles
cycles = 30

# PCR simulation
for cycle in range(cycles):
    initial_sequence = pcr_reaction(initial_sequence, temperature = 94)  # We assume a denaturation temperature of 94°C

# Final result after PCR cycles
print("Amplified sequence after", cycles, "PCR cycles:", initial_sequence)
