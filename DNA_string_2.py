# Give a short chain of nitrogenous bases
# The script creates the double helix and tells the amount of cytokines, guanines,
# thymines and adenines that there are in it.

print("DNA STRINGS GENERATOR \nWrite a series of letters of nitrogenous bases (CGTA):")
S53 = input().upper()

for e in S53:
    if e == "C":
        S35_1 = S53.replace("C", "1")
for e in S35_1:
    if e == "G":
        S35_2 = S35_1.replace("G", "2")
for e in S35_2:
    if e == "T":
        S35_3 = S35_2.replace("T", "3")
for e in S35_3:
    if e == "A":
        S35_4 = S35_3.replace("A", "4")

for e in S35_4:
    if e == "1":
        S35_G = S35_4.replace("1", "G")
for e in S35_G:
    if e == "2":
        S35_C = S35_G.replace("2", "C")
for e in S35_C:
    if e == "3":
        S35_A = S35_C.replace("3", "A")
for e in S35_A:
    if e == "4":
        S35 = S35_A.replace("4", "T")

print()

print("The double helix of DNA is:")
print("5'- " + S53 + " -3'")
print("3'- " + S35 + " -5'")

if "C" in S53:
    count_C1 = S53.count("C")
if "G" in S53:
    count_G1 = S53.count("G")
if "T" in S53:
    count_T1 = S53.count("T")
if "A" in S53:
    count_A1 = S53.count("A")

print()

print("In the chain given by the user, there are:")
print(count_C1, "cytokines")
print(count_G1, "guanines")
print(count_T1, "thymines")
print(count_A1, "adenines")

if "C" in S35:
    count_C2 = S35.count("C")
if "G" in S35:
    count_G2 = S35.count("G")
if "T" in S35:
    count_T2 = S35.count("T")
if "A" in S35:
    count_A2 = S35.count("A")

print()

print("In the complementary chain, there are:")
print(count_C2, "cytokines")
print(count_G2, "guanines")
print(count_T2, "thymines")
print(count_A2, "adenines")

count_C = count_C1 + count_C2
count_G = count_G1 + count_G2
count_T = count_T1 + count_T2
count_A = count_A1 + count_A2

print()

print("In the double helix of DNA, there are:")
print(count_C, "cytokines")
print(count_G, "guanines")
print(count_T, "thymines")
print(count_A, "adenines")

