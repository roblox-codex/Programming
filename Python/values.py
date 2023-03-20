def thing(x, y):
    z = 0
    k = 0
    for i in range(len(x)):
        if x[i] == -y[i]:
            z += x[i]
            k += 1
    print(f"k={k} z={z}")

a = [-2, 3, 5, -7, -10, 8, 6, -4]
b = [2, -3, 5, 7, 10, -8, 6, 4]
thing(a, b)

// Output: k=4 z=40
