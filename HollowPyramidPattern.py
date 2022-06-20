print("Hollow Pyramid Pattern:")
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end = " ")
    for k in range(2 * i + 1):
        if k == 0 or k == 2 * i:
            print("x", end = " ")
        else:
            if i == n - 1:
                print("x", end = " ")
            else:
                print(" ", end = " ")
    print()