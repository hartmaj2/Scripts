# Tests how many triples of numbers satisfy the equation x^exp + y^exp == z^exp
# where (x,y,z) \in \{low_lim,...,up_lim-1\}

low_lim = 1
up_lim = 10
exp = 3

count = 0
for x in range(low_lim,up_lim):
    for y in range(low_lim,up_lim):
        for z in range(low_lim,up_lim):
            if pow(x,exp) + pow(y,exp) == pow(z,exp):
                count += 1
                print(f"({x},{y},{z})")

print(f"Count: {count}")