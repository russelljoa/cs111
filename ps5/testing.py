def mystery(x, vals):
    for i in range(len(vals)):
        vals[i] *= 2
    x += 5

    # what do things look like in memory at this point?
    return x

x = 2
v1 = [1, 2, 3]
v2 = v1[:]
v3 = v1
mystery(x, v1)

print(x)
print(v1)
print(v2)
print(v3)