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

calculate = int(input("\nWhat would you like to calculate?\n\n"
                  "Dilution (0)\n"))
if calculate == 0:
    print(dilution())


