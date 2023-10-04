# Let's find how much material do we need to make a solution for a MFC, working with acetic acid or glucose

print("-" * 130)
print("Keep in mind that for these calculations the International System will be used, so the volumes will be in cubic meters (m3),")
print("the masses in kilograms (Kg) and the densities in kilograms per cubic meter (Kg/m3). Likewise, for decimals, the point (.) will be used but not the comma (,).")
print()
print("NOTE: to end the program, enter the number zero (0) when it asks you to enter any data.")
print("To enter numbers in scientific notation, enter the reduced number followed by *10** followed by the corresponding exponent number; examples:")
print("12310.258 = 12.31*10**3")
print("0.0001231 = 12.31*10**-5")
print("-" * 130)
om = float(input("What type of organic material will you use? If it is acetic acid, enter the number 1, and if it is glucose, enter the number 2: "))
# "om" is "organic material"
while om != 0:
    if om == 1:
        vol_aa = float(input("Enter the volume of acetic acid to use (m3): ")) # "vol_aa" iss "volume of acetic acid"
        molar_aa = float(input("Enter the molar concentration of acetic acid to use (M): ")) # M = moles of solute / Liters of solution
        mol_aa = molar_aa * vol_aa
        Ac = 6.02214076*10**23 # "Ac" is "Avogadro's constant"
        # 1 mol is equal to 6.02214076x10^23 units
        mq_aa = mol_aa * Ac # "mq_aa" is "molecules quantity of acetic acid"
        # 1 molecule of acetic acid + 2 of water produce 2 nolecules of CO2 + 8 protons (H+) + 8 electrons (e-)
        mq_w = mq_aa * 2 # "mq_w" is "molecules quantity of water"
        mol_w = mq_w / Ac # "mol_w" is "moles of water"
        # 1 mol of water weighs 1 gram, and 1 gram is equivalent to 1 mL
        vol_w = mol_w * 1000 * 1000 # "vol_w" is "volumen of water"
        # Since the mol_w is multiplied by 1 gram and divided by 1 mol, obtaining the grams, and those grams are equal to the mL
        # So to get the liters, you multiply that mL by 1000, and then multiply again by 1000 to get the m3.
        print("Quantity of H2O needed to {} liters of acetic acid: {} liters.".format(vol_aa, vol_w))
        mq_CO2 = mq_aa * 2 # "mq_CO2" is "molecules quantity of CO2"
        mol_CO2 = mq_CO2 / Ac # "mol_CO2" is " moles of CO2"
        break
    elif om == 2:
        mass = float(input("Enter the mass of glucose to use (kg): "))
        break
    else:
        print("The entered value is neither 1 nor 2. Please enter only one of those two numbers corresponding to the organic matter to be used.")
        om = float(input("What type of organic material will you use? If it is acetic acid, enter the number 1, and if it is glucose, enter the number 2: "))

