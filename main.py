def dilution():
    print("Enter the three known values, leave the last blank.")
    m1 = input("Input the first molarity.")
    v1 = input("Input the first volume.")
    m2 = input("Input the second molarity.")
    v2 = input("Input the second volume.")
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

calculate = input("What would you like to calculate?\n"
                  "Options:\n"
                  "Dilution (0)\n")
if calculate == "0":
    print(dilution())


