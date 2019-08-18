def euclid(q, p):
    print(q, p)
    if p == 0 or q == 0:
        return q if p == 0 else q
    if p > q:
        return euclid(q, p % q)
    else:
        return euclid(p, q % p)


print(euclid(1111111, 1234567))
