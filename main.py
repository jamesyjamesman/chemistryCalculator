import periodictable

def dilution():
    print("Enter the three known values, leave the last blank.")
    m1 = input("Input the first molarity.\n")
    v1 = input("Input the first volume.\n")
    m2 = input("Input the second molarity.\n")
    v2 = input("Input the second volume.\n")
    if not m1.isnumeric():
        v1 = int(v1)
        m2 = int(m2)
        v2 = int(v2)
        return m2 * v2 / v1
    if not v1.isnumeric():
        m1 = int(m1)
        m2 = int(m2)
        v2 = int(v2)
        return m2 * v2 / m1
    if not m2.isnumeric():
        m1 = int(m1)
        v1 = int(v1)
        v2 = int(v2)
        return m1 * v1 / v2
    if not v2.isnumeric():
        m1 = int(m1)
        v1 = int(v1)
        m2 = int(m2)
        return m1 * v1 / m2
    else:
        return "Too many values submitted!"

def find_molar_mass():
    done = False
    molar_masses = []
    while not done:
        atomic_number = input("Enter the atomic number of the element you'd like to convert.\n")
        atomic_mass =  periodictable.elements[int(atomic_number)].mass
        amount = int(input("Enter the amount to convert.\n"))
        molar_mass = atomic_mass * amount
        molar_masses.append(molar_mass)
        if input("done? (y/n)\n").lower() == "y":
            done = True
    return molar_masses

calculate = int(input("\nWhat would you like to calculate?\n\n"
                  "Dilution (0)\n"
                  "Find molar mass (1)\n"))
if calculate == 0:
    print(dilution())
if calculate == 1:
    print(f"That molecule has {round(sum(find_molar_mass()), 3)} g/mol.")


