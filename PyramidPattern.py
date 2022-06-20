print("Pyramid Pattern:")
npp = 5
for i in range(npp):
    for j in range(npp - i - 1):
        print(" ", end = " ")
    for k in range(2 * i + 1):
        print("x", end = " ")
    print()