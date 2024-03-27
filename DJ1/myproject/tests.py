b = 0  # левая часть больше правой
m = 0  # правая часть больше левой
solv = []
for z in range(0, 50):
    for x in range(-50, 0):
        for y in range(-50, 50):
            l = 1 + x**2 + x**3 + y**2
            r = 9*x*y*z
            if r == l:
                solv.append([x, y, z])
            if l > r:
                b += 1
            else:
                m += 1


print(solv, b, m)