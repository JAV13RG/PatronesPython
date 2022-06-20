print("Hollow Triangle Pattern:")
n = 5
for i in range(1, n + 1):
    for j in range(i):
        if j == 0 or j == i - 1:
            print("x", end = " ")
        else:
            if i != n:
                print(" ", end = " ")
            else:
                print("x", end = " ")
    print()
